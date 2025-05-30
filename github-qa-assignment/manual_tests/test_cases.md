# Manual Test Cases as follows

## 1. Sign Up and Login

**Test Case 1**: Sign Up with Valid Data
**Steps as follows**

1. Go to https://github.com.
2. Enter a valid username, email, and password.
3. Click submit.

**Expected Result**: Account should be created and verification email sent.

**Test Case 2**: Login with valid credentials
 **Steps as follows**:
 1. Go to https://github.com/login
 2. Enter valid username and password
 3. Click 'Sign In'
 **Expected Result**: User is redirected to the dashboard
 
 **Test Case 3**: Login with invalid credentials
 **Steps as follows**:
 1. Go to https://github.com/login
 2. Enter invalid username and password
 3. Click 'Sign In'
 **Expected Result**: Error should be thrown like "Incorrect username or password"
 
 Note: There are still a few combinations of test cases like trying to sign up and login with empty fields etc, I have just included the high-priority test cases.

---------------------------------------------------------------------------------------------

## 2. Creating Repository
 **Test Case 1**: Create a new public repo with unique name
 **Steps as follows**:
  1) Go to the '+' icon and click 'New repository'
  2) Enter a unique name
  3) Set to Public and click 'Create repository'
 **Expected Result**: Repository will be created and listed in user's account
 
 **Test Case 2**: Create a new public repo with an existing repo name
 **Steps as follows**:
  1) Go to the '+' icon and click 'New repository'
  2) Enter an existing name
  3) Set to Public and click 'Create repository'
 **Expected Result**: The repository <repo-name> already exists on this account

----------------------------------------------------------------------------------------------

## 3. Issue Tracking
 **Test Case 1**: Create a new issue
 **Steps as follows**:
  1. Navigate to Issues tab in a repo
  2. Click 'New Issue' and fill details
  3. Submit the issue
 **Expected Result**: Issue appears in the issue list
 
 **Test Case 2**: Add Labels and Assignees
 **Steps as follows**:
  1. After issue creation, assign labels and users
 **Expected Result**: Labels and assignees should be saved and shown on the issue card
 
 **Test Case 3**: Check Notification System
 **Steps as follows**:
  1. Watch the repository.
  2. Create or comment on an issue.
 **Expected Result**: Email or in-app notification is sent to watchers or assignees
 
 --------------------------------------------------------------------------------------------
 
 ## 4. Pull Request Workflow
 
 **Test Case 1**: Create a Pull Request
 **Steps as follows**:
  1. Navigate to the repository
  2. Create a new branch and commit a change.
  3. Click on "Pull Requests" → "New Pull Request".
  4. Select the base and compare branches.
  5. Enter title and description, and create PR.
 **Expected Result**: Issue appears in the issue list
 
 **Test Case 2**: A pull request already exists
 **Steps as follows**:
  1. Open the PR
  2. View the "Files changed" tab.
  3. Add comments and submit a review (approve, comment, or request changes).
 **Expected Result**: Review is submitted and visible in the PR timeline.
 
 **Test Case 3**: Merge a Pull Request
 **Steps as follows**:
  1. Open the PR
  2. Click “Merge pull request”.
  3. Confirm merge.
 **Expected Result**: PR is merged and marked as "Merged".
 
 **Test Case 4**: Branch Comparison and Conflict Handling
 **Steps as follows**:
  1. Try to create a PR from a branch with conflicting changes.
  2. Check if GitHub highlights the conflict.
  3. Attempt to resolve the conflict via the UI.
 **Expected Result**: GitHub shows merge conflicts and blocks direct merge until resolved.
 
 ---------------------------------------------------------------------------------------------------
 
 ## 5. Navigation Between Repository Features
 
 **Test Case 1**: Navigate Between Tabs (Code, Issues, PRs, Actions)
 **Steps as follows**:
  1. Open a repository.
  2. Click on each of the top tabs: "Code", "Issues", "Pull Requests", and "Actions".
 **Expected Result**: Each tab loads the correct content without delay or any UI breakage.
 
 **Test Case 2**: Check Pagination in Issues or PRs
 **Steps as follows**:
  1. Navigate to "Issues" or "Pull Requests".
  2. Scroll to bottom and click “Next” or page numbers.
 **Expected Result**: Pagination works correctly, and content changes per page.
 
 **Test Case 3**: UI Consistency Check
 **Steps as follows**:
  1. Visit each tab.
  2. Check header, sidebar, icons, fonts, colors, and button placements.
 **Expected Result**: UI elements should be consistent across all tabs.
 
 **Test Case 4**: Page Load Performance
 **Steps as follows**:
  1. Measure time taken for each tab to load after clicking.
  2. Identify any lag, blank content, or spinner not disappearing.
 **Expected Result**: UI elements should be consistent across all tabs.
 
 
 
 
 
 
