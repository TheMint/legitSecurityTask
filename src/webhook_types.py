"""
Add relevant fields from GitHub's webhook schema here.
"""

from typing import Literal

from pydantic import BaseModel


class GithubWebhook(BaseModel):
    event_type: Literal["repository", "push", "team"]
    action: Literal[
        "created",
        "deleted",
        "edited",
        "added_to_repository",
        "removed_from_repository",
    ] = None

    organization: dict
    sender: dict
    repository: dict = []
    team: dict = []
