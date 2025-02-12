# app/schemas/big_commerce_schema.py
from graphene import Schema
from .types import BigCommerceType, BigCommercePaginatedType
from ..queries.big_commerce_queries import Query
from ..mutations.big_commerce_mutations import Mutation

schema = Schema(query=Query, mutation=Mutation)
