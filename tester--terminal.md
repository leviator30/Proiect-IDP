curl http://localhost:3000/blueprints


curl -X POST http://localhost:3000/blueprints -H "Content-Type: application/json" -d '{  "title": "Linux Test Chest",  "author": "Edis",  "blueprintString": "0eNqV0t2KwjAQBeB3mesoa02szauISH8GGWinJRlFKXl3p1bYi2WlvZxwzjeBZISqveEQiAX8CA3GOtAg1DP4aZLPtKmwFTBAdc8R/GmESFcu26nEZYeallByHPogczZpmBt8gN+lswFkISGcu+/heeFbV2HQgPnHMDD0kebbjKDU3m2dgSf4TZ5vna5oKGA9B2wyf+RsuXxYJ++Xy/k62S6Xi3WyWy4fv8n6nCTYqfP7eQy0pVp6Nq24fNg7hvguuUNW2KJwx+zHWbtL6QUcq9Bz"}'

-----
dupa kong



// register

curl -X POST http://localhost:8000/auth/register \
-H "Content-Type: application/json" \
-d '{
  "username": "Test1",
  "password": "Test1"
}'

//login

curl -X POST http://localhost:8000/auth/login \
-H "Content-Type: application/json" \
-d '{"username": "Test1", "password": "Test1"}'

// add blueprint

curl -X POST http://localhost:8000/api/blueprints/share \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJUZXN0MSIsImV4cCI6MTc3NTQyNDcxOSwiaXNzIjoiVGVzdDEifQ.DBQzts4sqhKLSjvmJsp6g60fcQPrZO0pGlkG4V8W02w" \
-H "X-User-Name: Test1" \
-H "Content-Type: application/json" \
-d '{
  "title": "Belt Balancer 4x4",
  "blueprintString": "0eNqV0t2KwjAQBeB3mesoa02szauISH8GGWinJRlFKXl3p1bYi2WlvZxwzjeBZISqveEQiAX8CA3GOtAg1DP4aZLPtKmwFTBAdc8R/GmESFcu26nEZYeallByHPogczZpmBt8gN+lswFkISGcu+/heeFbV2HQgPnHMDD0kebbjKDU3m2dgSf4TZ5vna5oKGA9B2wyf+RsuXxYJ++Xy/k62S6Xi3WyWy4fv8n6nCTYqfP7eQy0pVp6Nq24fNg7hvguuUNW2KJwx+zHWbtL6QUcq9Bz",
  "author": "Test1"
}'

// get

curl -X GET http://localhost:8000/api/blueprints \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJUZXN0MSIsImV4cCI6MTc3NTQyNDcxOSwiaXNzIjoiVGVzdDEifQ.DBQzts4sqhKLSjvmJsp6g60fcQPrZO0pGlkG4V8W02w"