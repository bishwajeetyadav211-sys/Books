from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import geopy.distance

from app.db.database import get_db
from app.schemas.address import AddressCreate, AddressUpdate, AddressResponse
from app.routers import address_crud
from app.models.address import Address

router = APIRouter(prefix="/addresses", tags=["Addresses"])

@router.post("/", response_model=AddressResponse)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    return address_crud.create_address(db=db, address=address)

@router.get("/nearby", response_model=List[AddressResponse])
def get_nearby_addresses(lat: float, lon: float, distance: float, db: Session = Depends(get_db)):
    addresses = address_crud.list_addresses(db, skip=0, limit=10000)
    nearby_addresses = []
    
    for addr in addresses:
        if addr.latitude is not None and addr.longitude is not None:
            dist = geopy.distance.distance((lat, lon), (addr.latitude, addr.longitude)).km
            if dist <= distance:
                nearby_addresses.append(addr)
                
    return nearby_addresses

@router.get("/", response_model=List[AddressResponse])
def list_addresses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return address_crud.list_addresses(db=db, skip=skip, limit=limit)

@router.get("/{address_id}", response_model=AddressResponse)
def get_address(address_id: int, db: Session = Depends(get_db)):
    db_address = address_crud.get_address_by_id(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@router.put("/{address_id}", response_model=AddressResponse)
def update_address(address_id: int, address_update: AddressUpdate, db: Session = Depends(get_db)):
    db_address = address_crud.update_address(db=db, address_id=address_id, address_update=address_update)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@router.delete("/{address_id}", response_model=AddressResponse)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    db_address = address_crud.delete_address(db=db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address
