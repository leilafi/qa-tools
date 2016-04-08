"""
Exports Issues from a specified repository to a CSV file
Uses basic authentication (Github username + password) to retrieve Issues
from a repository that username has access to.
INSTUCTIONS:
1. pip install requests
2. replace GITHUB_USER with your username
3. replace GITHUB_PASSWORD with your auth token (settings -> personal access tokens)
4. run as "python export_issues.py"
5. type --help for information about the parameters
"""
import csv
import requests
from optparse import OptionParser
import json

parser = OptionParser()
args = parser.add_option("-s", "--state", dest="state", default="open", help="For know issues, leave it blank."
                                                                             "For fixed issues type closed")
args = parser.add_option("-d", "--since", dest="since", default="2016-01-01",
                         help="For known issues, leave it blank. "
                              "For fixed issues enter a date in YYYY-MM-DD format.")
args = parser.add_option("-l", "--label", dest="label", default="bug")
#args = parser.add_option("-r", "--report", dest="report", default="notreport", help="Generates a report of bug stats." )
(options, args) = parser.parse_args()
bugState = options.state
since = options.since
label = options.label
#report = options.report

count = 0
GITHUB_USER = 'leila.firouz@red-badger.com'
GITHUB_PASSWORD = '2af029a70f0b6ed9d3e52ceea6eb98b5512d39b5'
REPO = 'redbadger/ct-cms'  # format is username/repo
ISSUES_FOR_REPO_URL = 'https://api.github.com/repos/%s/issues?state=%s&since=%s&labels=%s' % (REPO,bugState,since,label)

AUTH = (GITHUB_USER, GITHUB_PASSWORD)


def write_issues(response):
    "output a list of issues to csv"
    if not response.status_code == 200:
        raise Exception(response.status_code)
    for issue in response.json():

        csvout.writerow([issue['number'], issue['title'], issue['state']])

r = requests.get(ISSUES_FOR_REPO_URL, auth=AUTH)

csvfile = '%s-issues-%s-%s.csv' % ((REPO.replace('/', '-')), label, bugState)
csvout = csv.writer(open(csvfile, 'wb'))
csvout.writerow(('id', 'title', 'state'))
count = len(r.json())
write_issues(r)

# more pages? examine the 'link' header returned
if 'link' in r.headers:
    pages = dict(
        [(rel[6:-1], url[url.index('<')+1:-1]) for url, rel in
            [link.split(';') for link in
                r.headers['link'].split(',')]])
    while 'last' in pages and 'next' in pages:
        r = requests.get(pages['next'], auth=AUTH)
        count = count+len(r.json())
        write_issues(r)
        if pages['next'] == pages['last']:
            break

print 'number of %s issues %s :%d' %(bugState, label, count)