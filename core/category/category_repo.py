from typing import List, Protocol

from core.category.category import CategoryBase, CategoryInDB
from core.channel.channel import ChannelInDB

class CategoryRepo(Protocol):
    
    async def create_category(self, new_cat: CategoryBase) -> CategoryInDB:
        pass

    async def get_category_by_id(self, cat_id: str) -> CategoryInDB:
        pass

    async def update_category(self, cat_id: str, cat_update: CategoryBase) -> CategoryInDB:
        pass

    async def delete_category(self, cat_id: str) -> bool:
        pass

    async def get_category_channels_related(self, cat_id: str) -> List[ChannelInDB]:
        pass