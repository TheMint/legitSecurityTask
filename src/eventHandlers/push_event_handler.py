from webhook_types import GithubWebhook
from datetime import datetime, time


def scan_push_event(event: GithubWebhook) -> str | None:
    curr_time = datetime.now().time()
    if curr_time >= time(14, 0) and curr_time <= time(16, 0):
        return f"User '{event.sender['login']}' pushed code between 14:00 and 16:00!"
