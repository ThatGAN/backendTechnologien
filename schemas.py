from typing import List, Union

from pydantic import BaseModel


class TruckBase(BaseModel):
    id_behind: int
    id_in_front: int
    is_leader: bool
    speed: int


class TruckCreate(TruckBase):
    pass


class Truck(TruckBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True







class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    trucks: List[Truck] = []

    class Config:
        orm_mode = True