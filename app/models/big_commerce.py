from orator import DatabaseManager, Model
# from ..config import db_config

# db = DatabaseManager(db_config)

# # Connect the database instance to the model
# Model.set_connection_resolver(db)


class BigCommerce(Model):
    __table__ = 'bigcommerce_clients'
    __primary_key__ = 'id'
    __timestamps__ = False
    __fillable__ = ['token', 'store_id', 'created_at', 'updated_at']
