from typing import Optional
from pydantic import BaseModel, Field
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    description: str
    image_link: str

class CategoryInDB(CategoryBase):
    id : str = Field(..., alias="_id")


