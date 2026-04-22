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

curl -X POST http://localhost:8000/auth/login -H "Content-Type: application/json" -d '{"username": "Test1", "password": "Test1"}'

// add blueprint

curl -X POST http://localhost:8000/api/blueprints/share \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJUZXN0MSIsImV4cCI6MTc3NTQyNDcxOSwiaXNzIjoiVGVzdDEifQ.DBQzts4sqhKLSjvmJsp6g60fcQPrZO0pGlkG4V8W02w" \
-H "X-User-Name: Test1" \
-H "Content-Type: application/json" \
-d '{
  "title": "Belt Balancer 4x4,test1",
  "blueprintString": "0eNqV0t2KwjAQBeB3mesoa02szauISH8GGWinJRlFKXl3p1bYi2WlvZxwzjeBZISqveEQiAX8CA3GOtAg1DP4aZLPtKmwFTBAdc8R/GmESFcu26nEZYeallByHPogczZpmBt8gN+lswFkISGcu+/heeFbV2HQgPnHMDD0kebbjKDU3m2dgSf4TZ5vna5oKGA9B2wyf+RsuXxYJ++Xy/k62S6Xi3WyWy4fv8n6nCTYqfP7eQy0pVp6Nq24fNg7hvguuUNW2KJwx+zHWbtL6QUcq9Bz",
  "author": "Test1"
}'
// get

curl -X GET http://localhost:8000/api/blueprints \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJUZXN0MSIsImV4cCI6MTc3NTQzMTM1MywiaXNzIjoiVGVzdDEifQ.kUTwafNNZ0XrFfw16csUlPmYALb2e7HTC8_i84rgBJI"


curl -X GET http://localhost:8000/api/my-blueprints \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJUZXN0MSIsImV4cCI6MTc3NTQzMTM1MywiaXNzIjoiVGVzdDEifQ.kUTwafNNZ0XrFfw16csUlPmYALb2e7HTC8_i84rgBJI"


//delete 
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJUZXN0MSIsImV4cCI6MTc3NTQzMTM1MywiaXNzIjoiVGVzdDEifQ.kUTwafNNZ0XrFfw16csUlPmYALb2e7HTC8_i84rgBJI"


curl -X DELETE http://localhost:8000/api/blueprints/69d2d1d0fd795608d069555d \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJUZXN0MSIsImV4cCI6MTc3NTQyNjExMiwiaXNzIjoiVGVzdDEifQ.SnLmbhAebUm-lr-1BCc5Tl3nZWl1MYiBkCvawVnaLXI" \
-H "X-User-Name: Test1"




-- teste 22.05. merg toate

curl -X POST http://localhost:5000/api/blueprints/share \
-H "Content-Type: application/json" \
-H "x-user-name: Test1" \
-d '{
  "title": "Nuclear Power Setup",
  "blueprintString": "0eNqV0t2KwjAQBeB3mesoa02szauISH8GGWinJRlFKXl3p1bYi2WlvZxwzjeBZISqveEQiAX8CA3GOtAg1DP4aZLPtKmwFTBAdc8R/GmESFcu26nEZYeallByHPogczZpmBt8gN+lswFkISGcu+/heeFbV2HQgPnHMDD0kebbjKDU3m2dgSf4TZ5vna5oKGA9B2wyf+RsuXxYJ++Xy/k62S6Xi3WyWy4fv8n6nCTYqfP7eQy0pVp6Nq24fNg7hvguuUNW2KJwx+zHWbtL6QUcq9Bz" 
}'

curl http://localhost:5000/api/blueprints


curl -H "x-user-name: Test1" http://localhost:5000/api/my-blueprints


curl -X DELETE http://localhost:5000/api/blueprints/69d2d1d0fd795608d069555d \
-H "x-user-name: Test1"