import json
import logging
from datetime import datetime
from http import HTTPStatus

import uvicorn
from fastapi import FastAPI, Request, Response
from pydantic import ValidationError

from eventHandlers.event_handler import handle_github_webhook
from webhookParser.webhook_parsers import parse_github_webhook_request

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)


@app.post("/github-event")
async def github_event(request: Request):
    try:
        event = await parse_github_webhook_request(request)
        handle_github_webhook(event)
        content = json.dumps({"message": f"{event.event_type} event received"})
        return Response(content=content, status_code=HTTPStatus.OK)

    except ValidationError as e:
        content = json.dumps(
            {"message": f"{datetime.now()} - Validation error! {str(e)}"}
        )
        logging.error(f"Validation error!\n\n{content}")
        return Response(content=content, status_code=HTTPStatus.BAD_REQUEST)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
