

from typing import Optional
from pydantic.fields import Field
from pydantic.main import BaseModel


class ChannelBase(BaseModel):
    name: str
    description: str
    image_link: str
    channel_url: str
    category_id: Optional[str]
    status: Optional[str]

class ChannelInDB(ChannelBase):
    id : str = Field(..., alias='_id')