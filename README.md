Exports Issues from a specified repository to a CSV file.
</p>
Prints out the bug stats for: number of bugs, number of to fix, number of pending story, number of enhancement :5
</p>
Uses basic authentication (Github username + password) to retrieve Issues
from a repository that username has access to.
</p>
**INSTUCTIONS to get the list of bugs title and number:**
</p>
1.pip install requests
</p>
2.replace GITHUB_USER with your username
</p>
3.replace GITHUB_PASSWORD with your auth token (settings -> personal access tokens)
</p>
4.run as "python export_issues.py"
</p>
5.type --help for information about the parameters


**INSTUCTIONS to get the bug stats:**
</p>
1.pip install requests
</p>
2.replace GITHUB_USER with your username
</p>
3.replace GITHUB_PASSWORD with your auth token (settings -> personal access tokens)
</p>
4.run as "python bugstats.py"