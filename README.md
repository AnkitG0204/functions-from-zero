# functions-from-zero
live training

[![Python application test with Github Actions](https://github.com/AnkitG0204/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/AnkitG0204/functions-from-zero/actions/workflows/main.yml)

### To Call Microservices
something like this
```bash
curl -X 'POST' \
  'https://crispy-waffle-qpqx95w4x94f955v-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

### Build container

`docker build .`
`docker image ls`

### Run container
`docker run -p 127.0.0.1:8080:8080 IMAGE_ID`

### Invoke POST request
bash `invoke.sh`