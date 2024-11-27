import logging
from typing import Callable

from eventHandlers.push_event_handler import scan_push_event
from eventHandlers.repository_event_handler import scan_repository_event
from eventHandlers.team_event_handler import scan_team_event
from models import GithubEvent, PushEvent, RepositoryEvent, TeamEvent

EVENT_SCANNER_MAP: dict[GithubEvent, Callable[[GithubEvent], str | None]] = {
    PushEvent: scan_push_event,
    RepositoryEvent: scan_repository_event,
    TeamEvent: scan_team_event,
}


def handle_github_webhook(event: GithubEvent) -> None:
    """
    Calls relevant scanner based on GithubWebhook's event_type
    Prints warning messages if needed
    """
    event_detected_msg = EVENT_SCANNER_MAP[type(event)](event)

    if event_detected_msg:
        logging.warning(f"Security alert! {event_detected_msg}")
