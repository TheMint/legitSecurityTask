from fastapi import Request

from models import EVENT_MODEL_MAP, GithubEvent


async def parse_github_webhook_request(request: Request) -> GithubEvent:
    dataJson = await request.json()
    return EVENT_MODEL_MAP[request.headers["x-github-event"]](**dataJson)
