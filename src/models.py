"""
Add relevant fields from GitHub's webhook schema here.
"""

from typing import Literal

from pydantic import BaseModel


class Team(BaseModel):
    name: str
    id: int
    node_id: str
    slug: str
    descriptions: str
    privacy: str
    notification_setting: str
    url: str
    html_url: str
    members_url: str
    repositories_url: str
    permission: str
    parent: str = None


class Pusher(BaseModel):
    name: str
    email: str


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
    team: dict = {}


class PushEvent(GithubWebhookBase):
    pusher: Pusher


class RepositoryEvent(GithubWebhookBase):
    repository: dict = {}


GithubEvent = RepositoryEvent | PushEvent | TeamEvent

EVENT_MODEL_MAP: dict[str, GithubEvent] = {
    "repository": RepositoryEvent,
    "push": PushEvent,
    "team": TeamEvent,
}
