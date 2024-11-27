from models import RepositoryEvent
from datetime import datetime, timedelta

# Map of recently created repositories and their creation time
repos_creation_time: dict[str, datetime] = {}


def scan_repository_event(event: RepositoryEvent) -> str | None:
    repo_name = event.repository["full_name"]  # "organization/repo"
    user = event.sender["login"]

    if event.action == "created":
        repos_creation_time[repo_name] = datetime.now()

    elif event.action == "deleted":
        if (
            repo_name in repos_creation_time.keys()
            and datetime.now() - repos_creation_time[repo_name] < timedelta(minutes=10)
        ):
            return f"User '{user}' created and deleted repository '{repo_name}' within 10 minutes"
        repos_creation_time.pop(repo_name)
