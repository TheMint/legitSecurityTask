# How to run smee.io for webhook deliveries from GitHub
Execute the following command -
`
smee -u https://smee.io/230RT53tGQjBAI4F --target http://127.0.0.1:3000/github-event
`

## Docs of relevant events
* Push - https://docs.github.com/en/webhooks/webhook-events-and-payloads#push
* Repository - https://docs.github.com/en/webhooks/webhook-events-and-payloads?actionType=created#repository
* Team - https://docs.github.com/en/webhooks/webhook-events-and-payloads#team


