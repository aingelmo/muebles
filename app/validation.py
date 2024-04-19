from typing import List

from pydantic import BaseModel


class UniqueItemId(BaseModel):
    """Unique item id validation model."""

    name: str
    doc_id: int


class Material(BaseModel):
    """Material validation model."""

    name: str
    price: int


class Dimension(BaseModel):
    """Dimension validation model."""

    width: int
    length: int
    thickness: int
    price: int


class Finishing(BaseModel):
    """Finishing validation model."""

    name: str
    price: int


class Item(BaseModel):
    """item validation model."""

    materials: List[Material]
    description: str
    dimensions: List[Dimension]
    id: int
    finishings: List[Finishing]
    name: str
