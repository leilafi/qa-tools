"""
Exports Issues count from a specified repository
Uses basic authentication (Github username + password) to retrieve Issues
from a repository that username has access to.
INSTUCTIONS:
1. pip install requests
2. replace GITHUB_USER with your username
3. replace GITHUB_PASSWORD with your auth token (settings -> personal access tokens)
4. run as "python bugstats.py"
"""

import csv
import requests

since = '2016-01-01'
bugState = 'open'


def main(label):
    count = 0
    GITHUB_USER = 'leila.firouz@red-badger.com'
    GITHUB_PASSWORD = '2af029a70f0b6ed9d3e52ceea6eb98b5512d39b5'
    REPO = 'redbadger/ct-cms'  # format is username/repo
    ISSUES_FOR_REPO_URL = 'https://api.github.com/repos/%s/issues?state=%s&since=%s&labels=%s' % (REPO,bugState,since,label)
    AUTH = (GITHUB_USER, GITHUB_PASSWORD)
    r = requests.get(ISSUES_FOR_REPO_URL, auth=AUTH)

    csvfile = '%s-issues-%s-%s.csv' % ((REPO.replace('/', '-')), label, bugState)
    csvout = csv.writer(open(csvfile, 'wb'))
    csvout.writerow(('id', 'title', 'state'))
    count = len(r.json())
    write_issues(r, csvout)

    # more pages? examine the 'link' header returned
    if 'link' in r.headers:
        pages = dict(
            [(rel[6:-1], url[url.index('<')+1:-1]) for url, rel in
                [link.split(';') for link in
                    r.headers['link'].split(',')]])
        while 'last' in pages and 'next' in pages:
            r = requests.get(pages['next'], auth=AUTH)
            count = count+len(r.json())
            write_issues(r, csvout)
            if pages['next'] == pages['last']:
                break

    print 'number of %s :%d' %(label, count)


def write_issues(response, csvout):
    "output a list of issues to csv"
    if not response.status_code == 200:
        raise Exception(response.status_code)
    for issue in response.json():

        csvout.writerow([issue['number'], issue['title'], issue['state']])

main('bug')
main('to fix')
main('pending story')
main('enhancement')