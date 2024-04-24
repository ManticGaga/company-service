from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException

app = FastAPI(openapi_url="/api/v1/companies/openapi.json", docs_url="/api/v1/companies/docs")

companies_router = APIRouter()

companies = [
    {'companies_id': 1,
     'name': 'SpaceX',
     'description': 'Founded by Elon Musk, SpaceX is an American aerospace manufacturer and space transportation company.',
     'staff': '8,000+ employees',
     'age': 'Space exploration, satellite manufacturing, rocket engineering'},
    {'companies_id': 2,
     'name': 'Boeing',
     'description': 'Boeing is an American multinational corporation that designs, manufactures, and sells airplanes, rotorcraft, rockets, satellites, telecommunications equipment, and missiles worldwide.',
     'staff': '150,000+ employees',
     'age': 'Aerospace, defense, rotorcraft'},
    {'companies_id': 3,
     'name': 'Lockheed Martin',
     'description': 'Lockheed Martin is an American aerospace, defense, arms, security, and advanced technologies company.',
     'staff': '110,000+ employees',
     'age': 'Aerospace, defense, security, advanced technologies'},
    {'companies_id': 4,
     'name': 'Airbus',
     'description': 'Airbus SE is a European multinational aerospace corporation that designs, manufactures, and sells civil and military aeronautical products worldwide.',
     'staff': '130,000+ employees',
     'age': 'Aerospace, defense, helicopters'},
    {'companies_id': 5,
     'name': 'Northrop Grumman',
     'description': 'Northrop Grumman Corporation is an American multinational aerospace and defense technology company.',
     'staff': '90,000+ employees',
     'age': 'Aerospace, defense, technology'}
]


@companies_router.get("/")
async def read_companies():
    return companies


@companies_router.get("/{companies_id}")
async def read_companie(companies_id: int):
    for companie in companies:
        if companie['companies_id'] == companies_id:
            return companie
    return None


app.include_router(companies_router, prefix='/api/v1/companies', tags=['companies'])

if __name__ == '__main__':
    import uvicorn
    import os

    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
