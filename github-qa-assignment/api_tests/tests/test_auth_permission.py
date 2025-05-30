import requests

def test_valid_token_access_public_repo():
    username = "venugopal-2000"
    token = "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"
    repo = "flexiple-simplismart-api-qa-assignment"

    res = requests.get(f"https://api.github.com/repos/{username}/{repo}", auth=(username, token))
    assert res.status_code == 200, f"Expected 200 OK, got {res.status_code}: {res.text}"


def test_invalid_token_access():
    username = "venugopal-2000"
    invalid_token = "ghp_FAKE12345invalid"

    res = requests.get(f"https://api.github.com/user", auth=(username, invalid_token))
    assert res.status_code == 401, f"Expected 401 Unauthorized, got {res.status_code}: {res.text}"



def test_no_token_access_to_private_repo():
    username = "venugopal-2000"
    repo = "private_repo_name"

    res = requests.get(f"https://api.github.com/repos/{username}/{repo}")
    assert res.status_code == 404 or res.status_code == 403, f"Expected 404 or 403 for unauthenticated private repo access, got {res.status_code}"


def test_expired_token_access():
    username = "venugopal-2000"
    expired_token = "ghp_FAKEexpired123"

    res = requests.get(f"https://api.github.com/user", auth=(username, expired_token))
    assert res.status_code == 401, f"Expected 401 Unauthorized for expired token, got {res.status_code}"

