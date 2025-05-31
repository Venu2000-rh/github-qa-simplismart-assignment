# github-qa-simplismart-assignment

This project contains automated test cases for GitHub using both API and UI testing. It covers repository creation, issue tracking, pull requests, authentication flows, and more.

## Prerequisites

- Python 3.9 or above
- Google Chrome (latest)
- ChromeDriver (matching your Chrome version)
- GitHub account with Personal Access Token (PAT)
- pip (Python package manager)

## Installation

1. Clone the repository:
   git clone https://github.com/<your-username>/github-qa-assignment.git
   cd github-qa-assignment

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate       (for Windows)
   source venv/bin/activate    (for macOS/Linux)

3. Install dependencies:
   pip install -r requirements.txt

4. Make sure ChromeDriver is in your PATH or placed in the project root.

## Running the Tests

To run all API tests:
   pytest api_tests/tests/ --html=reports/api_report.html

To run all UI tests:
   pytest ui_tests/tests/ --html=reports/ui_report.html

You can also run any individual test file using the same format.

## Viewing HTML Reports

After running tests, open the generated HTML files in the reports/ folder with any browser:
   reports/api_report.html
   reports/ui_report.html

## API Authentication Setup

1. Generate a GitHub Personal Access Token from https://github.com/settings/tokens.
2. Use the token inside your API test script headers like this:

   headers = {
       "Authorization": "Bearer <your_token>",
       "Accept": "application/vnd.github+json"
   }

## Folder Structure

github-qa-assignment/
├── api_tests/
│   └── tests/
│       └── test_*.py
├── ui_tests/
│   ├── conftest.py
│   └── tests/
│       └── test_*.py
├── reports/
│   └── api_report.html
│   └── ui_report.html
├── requirements.txt
└── README.md
