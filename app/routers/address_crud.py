from sqlalchemy.orm import Session
from app.models.address import Address
from app.schemas.address import AddressCreate, AddressUpdate

def create_address(db: Session, address: AddressCreate):
    db_address = Address(**address.model_dump())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def get_address_by_id(db: Session, address_id: int):
    return db.query(Address).filter(Address.id == address_id).first()

def list_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Address).offset(skip).limit(limit).all()

def update_address(db: Session, address_id: int, address_update: AddressUpdate):
    db_address = get_address_by_id(db, address_id)
    if not db_address:
        return None
    
    update_data = address_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_address, key, value)
        
    db.commit()
    db.refresh(db_address)
    return db_address

def delete_address(db: Session, address_id: int):
    db_address = get_address_by_id(db, address_id)
    if db_address:
        db.delete(db_address)
        db.commit()
    return db_address
