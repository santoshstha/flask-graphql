# Flask GraphQL(Basic CRUD )

A brief description of what this project does and who it's for

System Documentation

1. Overview

The system is a GraphQL API built using Flask, Orator (ORM), and MySQL. It allows CRUD operations on a bigcommerce_clients table, with features like pagination, filtering, and error handling.

2. System Architecture

The system follows a modular architecture with the following components:

    Flask: The web framework used to handle HTTP requests and responses.

    GraphQL: The query language for the API, enabling flexible data retrieval.

    Orator: The ORM used to interact with the MySQL database.

    MySQL: The relational database for storing data.

    Docker: Used to containerize the application and database for easy deployment.

3.  Directory Structure
    flask_graphql_app/
    │
    ├── app/
    │ ├── **init**.py # Flask app initialization
    │ ├── models/ # Database models
    │ │ └── big_commerce.py # BigCommerce model
    │ ├── schemas/ # GraphQL schemas and types
    │ │ ├── big_commerce_schema.py # GraphQL schema
    │ │ └── types.py # GraphQL types
    │ ├── mutations/ # GraphQL mutations
    │ │ └── big_commerce_mutations.py
    │ ├── queries/ # GraphQL queries
    │ │ └── big_commerce_queries.py
    │ ├── services/ # Business logic layer
    │ │ └── big_commerce_service.py
    │ ├── utils/ # Utility functions
    │ │ └── error_handlers.py # Error handling utilities
    │ └── config.py # Configuration settings
    │
    ├── requirements.txt # Python dependencies
    ├── Dockerfile # Docker configuration for the Flask app
    ├── docker-compose.yml # Docker Compose configuration
    └── run.py # Entry point for the application

4.  Key Components
    4.1. Models

        Location: app/models/big_commerce.py

        Description: Defines the BigCommerce model using Orator for interacting with the bigcommerce_clients table.

        Fields:

            id: Primary key.

            token: Token for BigCommerce authentication.

            store_id: Store identifier.

            created_at: Timestamp for record creation.

            updated_at: Timestamp for record update.

4.2. GraphQL Types

    Location: app/schemas/types.py

    Description: Defines GraphQL types for the BigCommerce model.

    Types:

        BigCommerceType: Represents a single BigCommerce record.

        BigCommercePaginatedType: Represents a paginated list of BigCommerce records.

4.3. Queries

    Location: app/queries/big_commerce_queries.py

    Description: Defines GraphQL queries for fetching data.

    Queries:

        get_big_commerce: Fetches a single record by ID.

        get_all_big_commerce: Fetches a paginated list of records.

4.4. Mutations

    Location: app/mutations/big_commerce_mutations.py

    Description: Defines GraphQL mutations for creating, updating, and deleting records.

    Mutations:

        create_big_commerce: Creates a new record.

        update_big_commerce: Updates an existing record.

        delete_big_commerce: Deletes a record.

4.5. Services

    Location: app/services/big_commerce_service.py

    Description: Contains business logic for interacting with the database.

    Methods:

        get_by_id: Fetches a record by ID.

        get_all: Fetches a paginated list of records.

        create: Creates a new record.

        update: Updates an existing record.

        delete: Deletes a record.

4.6. Configuration

    Location: app/config.py

    Description: Contains database configuration settings loaded from environment variables.

4.7. Error Handling

    Location: app/utils/error_handlers.py

    Description: Centralized error handling for GraphQL mutations and queries.
