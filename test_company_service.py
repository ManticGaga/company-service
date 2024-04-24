import requests


def test_get_all_companies(url: str):
    res = requests.get(url).json()
    assert (res == [{'companies_id': 1,
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
     'age': 'Aerospace, defense, technology'}])


def test_get_companie_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {'companies_id': 1,
     'name': 'SpaceX',
     'description': 'Founded by Elon Musk, SpaceX is an American aerospace manufacturer and space transportation company.',
     'staff': '8,000+ employees',
     'age': 'Space exploration, satellite manufacturing, rocket engineering'})


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/companies/'
    test_get_companie_by_id(URL + '1')
    test_get_all_companies(URL)
