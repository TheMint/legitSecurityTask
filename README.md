# Legit Security / GitHub Webhook Scanner

FastAPI server that detects suspicious activity in GitHub Organizations.
Setup your Github Organization's webhooks to pipe via smee.io into this tool.

## Docker usage

Run / test -

```
Run - docker run -e SMEE_LINK={LINK} themint/legit-security-task
Test - docker run -e MODE=test themint/legit-security-task
```

If you want to rebuild the image, use -

```
docker build -t legit-security-task .
```

## Local usage

Install dependencies -

```
poetry install && npm install
```

Execute -

```
./run.sh
```

Test -

```
./test.sh
```

## Docs of currently supported GitHub Webhooks

- Push - https://docs.github.com/en/webhooks/webhook-events-and-payloads#push
- Repository - https://docs.github.com/en/webhooks/webhook-events-and-payloads?actionType=created#repository
- Team - https://docs.github.com/en/webhooks/webhook-events-and-payloads#team

## Authors

- Yotam Ran
