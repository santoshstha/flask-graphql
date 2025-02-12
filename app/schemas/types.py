# app/schemas/types.py
from graphene import ObjectType, String, Int, List


class BigCommerceType(ObjectType):
    id = Int()
    token = String()
    store_id = String()
    updated_at = String()
    created_at = String()


class BigCommercePaginatedType(ObjectType):
    total = Int()
    items = List(BigCommerceType)
