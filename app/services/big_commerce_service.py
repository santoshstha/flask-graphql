# app/services/big_commerce_service.py
from datetime import datetime
from app.models.big_commerce import BigCommerce


class BigCommerceService:
    @staticmethod
    def get_by_id(id):
        return BigCommerce.find(id)

    @staticmethod
    def get_all(limit, offset):
        total_records = BigCommerce.count()
        query = BigCommerce.order_by('id').offset(offset).limit(limit)
        paginated_items = query.get()
        return {"total": total_records, "items": paginated_items}

    @staticmethod
    def create(token, store_id):
        return BigCommerce.create(
            token=token,
            store_id=store_id,
            updated_at=datetime.now(),
            created_at=datetime.now()
        )
