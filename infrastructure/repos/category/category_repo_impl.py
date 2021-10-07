from core.category.category import *
from core.channel.channel import *
from typing import List
from infrastructure.database import db
from bson import ObjectId
from configs.environment import DATABASE_NAME, category_collection_name

async def create_category(new_cat: CategoryBase) -> CategoryInDB:
    try:
        row = await db.client[DATABASE_NAME][category_collection_name].insert_one(new_cat.dict())
        if row.inserted_id:
            return await get_category_by_id(str(row.inserted_id))
    except Exception as e:
        raise e

async def get_category_by_id(cat_id: str) -> CategoryInDB:
    try:
        row = await db.client[DATABASE_NAME][category_collection_name].find_one({"_id": ObjectId(cat_id)})
        if row:
            row['_id'] = str(row['_id'])
            return CategoryInDB(**row)
        return None
    except Exception as e:
        raise e

async def update_category(cat_id: str, cat_update: CategoryBase) -> CategoryInDB:
    try:
        row = await db.client[DATABASE_NAME][category_collection_name].find_one({"_id": ObjectId(cat_id)})
        if row:
            row['name'] = cat_update.name if cat_update.name else row['name']
            row['description'] = cat_update.description if cat_update.description else row['description']
            row['image_link'] = cat_update.image_link if cat_update.image_link else row['image_link'] 
            res = await db.client[DATABASE_NAME][category_collection_name].replace_one({"_id": row['_id']}, row, upsert= True)
            
            return CategoryInDB(**row)
        return None
    except Exception as e:
        raise e

async def delete_category(cat_id: str) -> bool:
    pass

async def get_category_channels_related(cat_id: str) -> List[ChannelInDB]:
    pass