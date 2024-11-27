"""
Add relevant fields from GitHub's webhook schema here.
"""

from typing import Literal

from pydantic import BaseModel


class GithubWebhookBase(BaseModel):
    action: Literal[
        "created",
        "deleted",
        "edited",
        "added_to_repository",
        "removed_from_repository",
    ] = None

    organization: dict
    sender: dict


class TeamEvent(GithubWebhookBase):
    team: dict


class PushEvent(GithubWebhookBase):
    pusher: dict


class RepositoryEvent(GithubWebhookBase):
    repository: dict


GithubEvent = RepositoryEvent | PushEvent | TeamEvent

EVENT_MODEL_MAP: dict[str, GithubEvent] = {
    "repository": RepositoryEvent,
    "push": PushEvent,
    "team": TeamEvent,
}
