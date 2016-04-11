Exports Issues from a specified repository to a CSV file
Uses basic authentication (Github username + password) to retrieve Issues
from a repository that username has access to.
INSTUCTIONS to get the list of bugs title and number:
1. pip install requests
2. replace GITHUB_USER with your username
3. replace GITHUB_PASSWORD with your auth token (settings -> personal access tokens)
4. run as "python export_issues.py"
5. type --help for information about the parameters


INSTUCTIONS to get the bug stats:
1. pip install requests
2. replace GITHUB_USER with your username
3. replace GITHUB_PASSWORD with your auth token (settings -> personal access tokens)
4. run as "python bugstats.py"