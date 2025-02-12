# app/queries/big_commerce_queries.py
from graphene import Field, Int, ObjectType
from app.schemas.types import BigCommerceType, BigCommercePaginatedType
from app.services.big_commerce_service import BigCommerceService


class Query(ObjectType):
    get_big_commerce = Field(BigCommerceType, id=Int())
    get_all_big_commerce = Field(BigCommercePaginatedType, limit=Int(
        default_value=2), offset=Int(default_value=0))

    def resolve_get_big_commerce(self, info, id):
        return BigCommerceService.get_by_id(id)

    def resolve_get_all_big_commerce(self, info, limit, offset):
        return BigCommerceService.get_all(limit, offset)
