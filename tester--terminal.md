curl http://localhost:3000/blueprints


curl -X POST http://localhost:3000/blueprints -H "Content-Type: application/json" -d '{  "title": "Linux Test Chest",  "author": "Edis",  "blueprintString": "0eNqV0t2KwjAQBeB3mesoa02szauISH8GGWinJRlFKXl3p1bYi2WlvZxwzjeBZISqveEQiAX8CA3GOtAg1DP4aZLPtKmwFTBAdc8R/GmESFcu26nEZYeallByHPogczZpmBt8gN+lswFkISGcu+/heeFbV2HQgPnHMDD0kebbjKDU3m2dgSf4TZ5vna5oKGA9B2wyf+RsuXxYJ++Xy/k62S6Xi3WyWy4fv8n6nCTYqfP7eQy0pVp6Nq24fNg7hvguuUNW2KJwx+zHWbtL6QUcq9Bz"}'
git add -m "added persistence-brifge and validator" README.md docker-compose.yml my-db-folder/ persistence-bridge/ validator-service/ tester--terminal.md 