from fastapi import Request

from webhook_types import GithubWebhook


async def parse_github_webhook_request(request: Request):
    data = {**(await request.json()), "event_type": request.headers["x-github-event"]}
    return GithubWebhook(**data)
