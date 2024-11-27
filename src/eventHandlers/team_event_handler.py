from webhook_types import GithubWebhook

ILLEGAL_PREFIXES = tuple("hacker")


def scan_team_event(event: GithubWebhook) -> str | None:
    team_name = event.team["name"]
    user = event.sender["login"]
    if team_name.lower().startswith(ILLEGAL_PREFIXES):
        return f"User '{user}' just created the illegally named team '{team_name}'"
