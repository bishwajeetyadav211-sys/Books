from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class AddressBase(BaseModel):
    name: str
    latitude: float
    longitude: float

class AddressCreate(AddressBase):
    pass

class AddressUpdate(BaseModel):
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class AddressResponse(AddressBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
