{getAllBigCommerce(limit:2,offset:0){
  total
  items{
    storeId
  }
  
}}

{
  getBigCommerce(id:1){
    storeId,
    id
  }
}

mutation {
  createBigCommerce(token: "my_test_token", storeId: "12345") {
    bigCommerce {
      id
      token
      storeId
      createdAt
      updatedAt
    }
  }
}


mutation {
  updateBigCommerce(id: 1, token: "test12345", storeId: "67890") {
    bigCommerce {
      id
      token
      storeId
      createdAt
    }
  }
}


curl -X POST http://127.0.0.1:5000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "{ getBigCommerce(id: 1) { id, storeId, token, createdAt, updatedAt } }"}'


curl -X POST http://127.0.0.1:5000/graphql \
  -H "Content-Type: application/json" \
  -d '
    {"query":"{getAllBigCommerce(limit:2,offset:0){\n  total\n  items{\n    storeId\n  }\n  \n}}\n\n# {\n#   getBigCommerce(id:1){\n#     storeId,\n#     id\n#   }\n# }\n\n# mutation {\n#   createBigCommerce(token: \"my_test_token\", storeId: \"12345\") {\n#     bigCommerce {\n#       id\n#       token\n#       storeId\n#       createdAt\n#       updatedAt\n#     }\n#   }\n# }\n\n\n# mutation {\n#   updateBigCommerce(id: 1, token: \"test12345\", storeId: \"67890\") {\n#     bigCommerce {\n#       id\n#       token\n#       storeId\n#       createdAt\n#     }\n#   }\n# }\n","variables":null,"operationName":null}'