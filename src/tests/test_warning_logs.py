import json
import logging
from http import HTTPStatus

from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_repo_log(caplog):
    logging.basicConfig(level=logging.INFO)

    with caplog.at_level(logging.WARNING):
        with open("./tests/utils/create_repo.json", "r") as file:
            create_repo = json.load(file)
            response = client.post(
                "/github-event",
                json=create_repo,
                headers={"x-github-event": "repository"},
            )
            assert response.status_code == HTTPStatus.OK

        with open("./tests/utils/delete_repo.json", "r") as file:
            delete_repo = json.load(file)
            response = client.post(
                "/github-event",
                json=delete_repo,
                headers={"x-github-event": "repository"},
            )
            assert response.status_code == HTTPStatus.OK

    assert (
        "Security alert! User 'TheMint' created and deleted repository 'MintTestOrg/awefaw' within 10 minutes"
        in caplog.text
    )


def test_repo_log(caplog):
    logging.basicConfig(level=logging.INFO)

    with caplog.at_level(logging.WARNING):
        with open("./tests/utils/create_team.json", "r") as file:
            create_repo = json.load(file)
            response = client.post(
                "/github-event",
                json=create_repo,
                headers={"x-github-event": "team"},
            )
            assert response.status_code == HTTPStatus.OK

    assert (
        "Security alert! User 'TheMint' just created the illegally named team 'HackerMentha'"
        in caplog.text
    )
