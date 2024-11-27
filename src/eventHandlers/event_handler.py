import logging
from eventHandlers.push_event_handler import handle_push_event
from eventHandlers.repository_event_handler import handle_repository_event
from eventHandlers.team_event_handler import handle_team_event
from webhook_types import GithubWebhook

EVENT_HANDLER_MAPPING = {
    "push": handle_push_event,
    "repository": handle_repository_event,
    "team": handle_team_event,
}


def handle_github_webhook(event: GithubWebhook) -> None:
    """
    Calls relevant handler based on GithubWebhook's event_type
    Prints warning messages if needed
    """
    event_detected_msg = EVENT_HANDLER_MAPPING[event.event_type](event)

    if event_detected_msg:
        logging.warning(f"Security alert! {event_detected_msg}")
