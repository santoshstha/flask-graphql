# app/mutations/big_commerce_mutations.py
from graphene import Mutation, String, Field, ObjectType, Int
from app.schemas.types import BigCommerceType
from app.services.big_commerce_service import BigCommerceService
from datetime import datetime


class CreateBigCommerce(Mutation):
    class Arguments:
        token = String(required=True)
        store_id = String(required=True)

    big_commerce = Field(BigCommerceType)

    def mutate(self, info, token, store_id):
        return BigCommerceService.create(token, store_id)


class UpdateBigCommerce(Mutation):
    class Arguments:
        id = Int()
        token = String()
        store_id = String()

    big_commerce = Field(lambda: BigCommerceType)

    def mutate(self, info, id, token=None, store_id=None):
        big_commerce = BigCommerceService.find(id)
        if big_commerce:
            if token:
                big_commerce.token = token
            if store_id:
                big_commerce.store_id = store_id
            big_commerce.updated_at = datetime.now()
            big_commerce.save()
        return UpdateBigCommerce(big_commerce=big_commerce)


class DeleteBigCommerce(Mutation):
    class Arguments:
        id = Int()

    success = String()

    def mutate(self, info, id):
        big_commerce = BigCommerceService.find(id)
        if big_commerce:
            big_commerce.delete()
            return DeleteBigCommerce(success="Deleted Successfully")
        return DeleteBigCommerce(success="Not Found")


class Mutation(ObjectType):
    create_big_commerce = CreateBigCommerce.Field()
    update_big_commerce = UpdateBigCommerce.Field()
    delete_big_commerce = DeleteBigCommerce.Field()
