# Legit Security / GitHub Webhook Scanner
FastAPI server that detects suspicious activity in GitHub Organizations.

## Docker usage
Run / test -
```
docker run -e MODE=(test/run) themint/legit-security-task
```

If you want to rebuild the image, use - 
```
docker build -t legit-security-task .
```


Alternatively, run locally - 

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




## Docs of currently supported GitHub Webhooks
* Push - https://docs.github.com/en/webhooks/webhook-events-and-payloads#push
* Repository - https://docs.github.com/en/webhooks/webhook-events-and-payloads?actionType=created#repository
* Team - https://docs.github.com/en/webhooks/webhook-events-and-payloads#team



## Authors

- Yotam Ran

