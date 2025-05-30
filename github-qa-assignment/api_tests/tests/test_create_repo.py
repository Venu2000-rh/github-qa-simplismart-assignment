import requests
import json

def test_create_github_repository():

    GITHUB_USERNAME = "venugopal.fitbiz@gmaicom"
    GITHUB_TOKEN = "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"

    repo_name = f"flexiple-simplismart-api-qa-assignment"
    url = "https://api.github.com/user/repos"

    payload = {
        "name": repo_name,
        "description": "Repository created via GitHub API for QA testing",
        "private": False,
        "auto_init": True
    }

    headers = {
        "Accept": "application/vnd.github+json"
    }

    response = requests.post(url, headers=headers, auth=(GITHUB_USERNAME, GITHUB_TOKEN), data=json.dumps(payload))

    assert response.status_code == 201 or response.status_code == 200, f"Expected 201 Created, got {response.status_code}: {response.text}"

    data = response.json()
    assert data["name"] == repo_name, "Repository name in response doesn't match"

    # expected_url = f"https://github.com/{GITHUB_USERNAME}/{repo_name}"
    # assert "html_url" in data and expected_url == data["html_url"], "Unexpected repo URL"


