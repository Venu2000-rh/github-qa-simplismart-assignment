import requests


def test_fetch_existing_repo():
    username = "venugopal-2000"
    token = "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"
    repo = f"flexiple-simplismart-api-qa-assignment"

    url = f"https://api.github.com/repos/{username}/{repo}"
    response = requests.get(url, auth=(username, token))

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == repo
    assert data["owner"]["login"] == username


def test_fetch_nonexistent_repo():
    username = "venugopal.fitbiz@gmaicom"
    token = "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"
    fake_repo = "this-repo-does-not-exist-xyz"

    url = f"https://api.github.com/repos/{username}/{fake_repo}"
    response = requests.get(url, auth=(username, token))

    assert response.status_code == 404
