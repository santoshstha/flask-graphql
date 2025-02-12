API Documentation Queries

    Get All BigCommerce Entries

Endpoint: getAllBigCommerce(limit: Int, offset: Int) Description: Fetches a list of BigCommerce entries with pagination. Arguments:

limit (Optional): The number of items to fetch. Default: 10.
offset (Optional): The starting point for fetching items. Default: 0.

Response:

{ "total": Int, "items": [ { "storeId": String } ] }

Example Request:

query { getAllBigCommerce(limit: 2, offset: 0) { total items { storeId } } }

Curl Example:

curl -X POST http://127.0.0.1:5000/graphql
-H "Content-Type: application/json"
-d '{"query": "{ getAllBigCommerce(limit: 2, offset: 0) { total items { storeId } } }"}'

    Get Single BigCommerce Entry by ID

Endpoint: getBigCommerce(id: Int) Description: Fetches a single BigCommerce entry by its ID. Arguments:

id (Required): The unique ID of the BigCommerce entry.

Response:

{ "storeId": String, "id": Int }

Example Request:

query { getBigCommerce(id: 1) { storeId id } }

Curl Example:

curl -X POST http://127.0.0.1:5000/graphql
-H "Content-Type: application/json"
-d '{"query": "{ getBigCommerce(id: 1) { storeId, id } }"}'

Mutations

    Create BigCommerce Entry

Endpoint: createBigCommerce(token: String, storeId: String) Description: Creates a new BigCommerce entry. Arguments:

token (Required): A unique token for the BigCommerce entry.
storeId (Required): The unique store ID.

Response:

{ "bigCommerce": { "id": Int, "token": String, "storeId": String, "createdAt": String, "updatedAt": String } }

Example Request:

mutation { createBigCommerce(token: "my_test_token", storeId: "12345") { bigCommerce { id token storeId createdAt updatedAt } } }

Curl Example:

curl -X POST http://127.0.0.1:5000/graphql
-H "Content-Type: application/json"
-d '{"query": "mutation { createBigCommerce(token: "my_test_token", storeId: "12345") { bigCommerce { id token storeId createdAt updatedAt } } }"}'

    Update BigCommerce Entry

Endpoint: updateBigCommerce(id: Int, token: String, storeId: String) Description: Updates an existing BigCommerce entry. Arguments:

id (Required): The ID of the BigCommerce entry to be updated.
token (Required): The new token value.
storeId (Required): The new store ID.

Response:

{ "bigCommerce": { "id": Int, "token": String, "storeId": String, "createdAt": String } }

Example Request:

mutation { updateBigCommerce(id: 1, token: "test12345", storeId: "67890") { bigCommerce { id token storeId createdAt } } }

Curl Example:

curl -X POST http://127.0.0.1:5000/graphql
-H "Content-Type: application/json"
-d '{"query": "mutation { updateBigCommerce(id: 1, token: "test12345", storeId: "67890") { bigCommerce { id token storeId createdAt } } }"}'

GraphQL Endpoint

URL: http://127.0.0.1:5000/graphql
Method: POST
Headers:
Content-Type: application/json
Body: JSON formatted GraphQL query or mutation as shown in the examples above.
