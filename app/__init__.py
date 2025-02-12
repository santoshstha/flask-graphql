from flask import Flask
from flask_graphql import GraphQLView
from orator import DatabaseManager, Model
from .config import db_config
from .schemas.big_commerce_schema import schema


def create_app():
    app = Flask(__name__)

    # Database configuration
    db = DatabaseManager(db_config)
    app.db = db

    Model.set_connection_resolver(db)

    # Register GraphQL endpoint
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
    )

    return app
