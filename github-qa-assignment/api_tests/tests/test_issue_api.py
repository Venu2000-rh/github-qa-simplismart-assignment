import requests
import time

def test_issue_api():
    username = "venugopal-2000"
    token = "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"
    repo = "flexiple-simplismart-api-qa-assignment"  # ✅ Your working repo
    issue_title = f"Issue Title {int(time.time())}"
    issue_body = "This issue was created via GitHub API for automation testing."

    # Step 1: Create Issue
    create_url = f"https://api.github.com/repos/{username}/{repo}/issues"
    payload = {
        "title": issue_title,
        "body": issue_body
    }

    create_res = requests.post(create_url, auth=(username, token), json=payload)
    assert create_res.status_code == 201, f"Issue creation failed: {create_res.text}"
    issue_number = create_res.json()["number"]

    # Step 2: Wait briefly (GitHub cache delay protection)
    time.sleep(2)

    # Step 3: List Issues and verify the one we created
    list_url = f"https://api.github.com/repos/{username}/{repo}/issues?state=all&per_page=100"
    list_res = requests.get(list_url, auth=(username, token))
    assert list_res.status_code == 200, f"Issue list fetch failed: {list_res.text}"

    issues = list_res.json()
    titles = [issue["title"] for issue in issues]

    # Debugging output (optional)
    print("Fetched Issues:", titles)

    assert issue_title in titles, f"Issue '{issue_title}' not found in issue list"
