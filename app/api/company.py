from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import CompanyOut, CompanyIn, CompanyUpdate
from app.api import db_manager
from app.api.service import is_label_present

company = APIRouter()

@company.post('/', response_model=CompanyIn, status_code=201)
async def create_company(payload: CompanyIn):
    for label_id in payload.labels_id:
        if not is_label_present(label_id):
            raise HTTPException(status_code=404, detail=f"Label with given id:{label_id} not found")

    company_id = await db_manager.add_company(payload)
    response = {
        'id': company_id,
        **payload.dict()
    }

    return response

@company.get('/', response_model=List[CompanyOut])
async def get_companies():
    return await db_manager.get_all_companies()

@company.get('/{id}/', response_model=CompanyOut)
async def get_company(id: int):
    company = await db_manager.get_company(id)
    if not company:
        raise HTTPException(status_code=404, detail="company not found")
    return company

@company.put('/{id}/', response_model=CompanyOut)
async def update_company(id: int, payload: CompanyUpdate):
    company = await db_manager.get_company(id)
    if not company:
        raise HTTPException(status_code=404, detail="Label not found")

    update_data = payload.dict(exclude_unset=True)

    if 'labels_id' in update_data:
        for label_id in payload.labels_id:
            if not is_label_present(label_id):
                raise HTTPException(status_code=404, detail=f"Label with given id:{label_id} not found")

    company_in_db = CompanyIn(**company)

    updated_company = company_in_db.copy(update=update_data)

    return await db_manager.update_company(id, updated_company)

@company.delete('/{id}/', response_model=None)
async def delete_company(id: int):
    company = await db_manager.get_company(id)
    if not company:
        raise HTTPException(status_code=404, detail="company not found")
    return await db_manager.delete_company(id)