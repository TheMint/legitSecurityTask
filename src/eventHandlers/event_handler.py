import logging
from typing import Callable
from eventHandlers.push_event_handler import scan_push_event
from eventHandlers.repository_event_handler import scan_repository_event
from eventHandlers.team_event_handler import scan_team_event
from webhook_types import GithubWebhook

EVENT_SCANNER_MAPPING: dict[str, Callable[[GithubWebhook], str | None]] = {
    "push": scan_push_event,
    "repository": scan_repository_event,
    "team": scan_team_event,
}


def handle_github_webhook(event: GithubWebhook) -> None:
    """
    Calls relevant scanner based on GithubWebhook's event_type
    Prints warning messages if needed
    """
    event_detected_msg = EVENT_SCANNER_MAPPING[event.event_type](event)

    if event_detected_msg:
        logging.warning(f"Security alert! {event_detected_msg}")
