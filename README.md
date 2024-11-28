# Legit Security / GitHub Webhook Scanner
FastAPI server that detects suspicious activity in GitHub Organizations.

## Installing dependencies
Execute - 
```
poetry install && npm install
```

## How to run
Execute -
```
./run.sh
```

## How to test
Execute -
```
./test.sh
```

## Docker usage
Build image locally - 
```
docker build -t legit-security-task .
```
Run / test -
```
docker run -e MODE=(test/run) legit-security-task
```


## Docs of currently supported GitHub Webhooks
* Push - https://docs.github.com/en/webhooks/webhook-events-and-payloads#push
* Repository - https://docs.github.com/en/webhooks/webhook-events-and-payloads?actionType=created#repository
* Team - https://docs.github.com/en/webhooks/webhook-events-and-payloads#team



## Authors

- Yotam Ran

