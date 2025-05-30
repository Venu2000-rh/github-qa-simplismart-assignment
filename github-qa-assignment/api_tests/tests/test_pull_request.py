import requests
import time

def test_pull_request_with_metadata():
    username = "venugopal-2000"
    token = "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"
    repo = "flexiple-simplismart-api-qa-assignment"
    base_branch = "main"
    feature_branch = f"feature-pr"
    file_name = f"pull-request-file.txt"
    file_content = "This file was created via GitHub API to test pull request creation."

    headers = {
        "Accept": "application/vnd.github+json"
    }

    ref_url = f"https://api.github.com/repos/{username}/{repo}/git/ref/heads/{base_branch}"
    ref_res = requests.get(ref_url, auth=(username, token))
    assert ref_res.status_code == 200, f"Failed to get base ref: {ref_res.text}"
    base_sha = ref_res.json()["object"]["sha"]

    create_branch_url = f"https://api.github.com/repos/{username}/{repo}/git/refs"
    create_branch_payload = {
        "ref": f"refs/heads/{feature_branch}",
        "sha": base_sha
    }
    branch_res = requests.post(create_branch_url, headers=headers, auth=(username, token), json=create_branch_payload)
    assert branch_res.status_code == 201, f"Branch creation failed: {branch_res.text}"

    blob_url = f"https://api.github.com/repos/{username}/{repo}/git/blobs"
    blob_payload = {
        "content": file_content,
        "encoding": "utf-8"
    }
    blob_res = requests.post(blob_url, headers=headers, auth=(username, token), json=blob_payload)
    assert blob_res.status_code == 201, f"Blob creation failed: {blob_res.text}"
    blob_sha = blob_res.json()["sha"]

    commit_url = f"https://api.github.com/repos/{username}/{repo}/git/commits/{base_sha}"
    commit_res = requests.get(commit_url, headers=headers, auth=(username, token))
    assert commit_res.status_code == 200, f"Commit lookup failed: {commit_res.text}"
    tree_sha = commit_res.json()["tree"]["sha"]

    # Step 5: Create new tree with our file
    tree_url = f"https://api.github.com/repos/{username}/{repo}/git/trees"
    tree_payload = {
        "base_tree": tree_sha,
        "tree": [
            {
                "path": file_name,
                "mode": "100644",
                "type": "blob",
                "sha": blob_sha
            }
        ]
    }
    tree_res = requests.post(tree_url, headers=headers, auth=(username, token), json=tree_payload)
    assert tree_res.status_code == 201, f"Tree creation failed: {tree_res.text}"
    new_tree_sha = tree_res.json()["sha"]


    commit_payload = {
        "message": f"Add {file_name} for PR test",
        "tree": new_tree_sha,
        "parents": [base_sha]
    }
    new_commit_url = f"https://api.github.com/repos/{username}/{repo}/git/commits"
    new_commit_res = requests.post(new_commit_url, headers=headers, auth=(username, token), json=commit_payload)
    assert new_commit_res.status_code == 201, f"Commit creation failed: {new_commit_res.text}"
    new_commit_sha = new_commit_res.json()["sha"]


    update_ref_url = f"https://api.github.com/repos/{username}/{repo}/git/refs/heads/{feature_branch}"
    update_payload = {
        "sha": new_commit_sha,
        "force": True
    }
    update_res = requests.patch(update_ref_url, headers=headers, auth=(username, token), json=update_payload)
    assert update_res.status_code == 200, f"Failed to update ref: {update_res.text}"


    pr_url = f"https://api.github.com/repos/{username}/{repo}/pulls"
    pr_payload = {
        "title": f"Add {file_name} via API",
        "head": feature_branch,
        "base": base_branch,
        "body": f"This pull request was created automatically from the branch `{feature_branch}`."
    }
    pr_res = requests.post(pr_url, headers=headers, auth=(username, token), json=pr_payload)
    assert pr_res.status_code == 201, f"PR creation failed: {pr_res.text}"

    pr_data = pr_res.json()
    assert pr_data["state"] == "open"
    assert pr_data["head"]["ref"] == feature_branch
    assert pr_data["base"]["ref"] == base_branch
    assert pr_data["title"] == f"Add {file_name} via API"

    print(f"\n✅ Pull Request created: {pr_data['html_url']}")
