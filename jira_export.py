import os
import time
import requests
import csv

# ##############################################################################

jirasearch = ('http://rl-jira.poloralphlauren.com:8080/rest/api/2/search?')

jira_epic_payload = {'jql': 'filter=14110', 'expand': 'all,versionedRepresentations', 'maxResults': '5000',
                     'startAt': '0'}

jira_issue_payload = {'jql': 'filter=14108', 'expand': 'all,versionedRepresentations', 'maxResults': '5000',
                      'startAt': '0'}

# Used to capture Epic information
epicOutput = []
epicHeader = [
    'Epic Key',
    'Epic Aggregate Time Estimate',
    'Epic Aggregate Time Original Estimate',
    'Epic Aggregate Time Spent',
    'Epic Assignee Name',
    'Epic Assignee Email',
    'Epic Assignee Display Name',
    'Epic Created Date',
    'Epic Creator Name',
    'Epic Creator Email',
    'Epic Creator Display Name',
    'Epic Description',
    'Epic Due Date',
    'Epic Environment',
    'Epic Fix Versions',
    'Epic Issue Type',
    'Epic Labels',
    'Epic Priority',
    'Epic Priority Icon',
    'Epic Progress',
    'Epic Progress Total',
    'Epic Project',
    'Epic Reporter Name',
    'Epic Reporter Email',
    'Epic Reporter Display Name',
    'Epic Resolution',
    'Epic Resolution Date',
    'Epic Status',
    'Epic Status Icon',
    'Epic Summary',
    'Epic Time Estimate',
    'Epic Time Original Estimate',
    'Epic Time Spent',
    'Epic Updated',
    'Epic Link',
    'Epic Flagged',
    'Epic Theme',
    'Epic Story Points',
    'Epic Business Value',
    'Epic Release Version History',
    'Epic Geographic Region',
    'Epic Units',
    'Epic Percent Done',
    'Epic Due Time',
    'Epic Requested By',
    'Epic Start Date',
    'Epic Business Summary',
    'Epic CR#',
    'Epic Approved Date',
    'Epic CAR#',
    'Epic Funding Required',
    'Epic ServiceNow Incident#',
    'Epic Rank',
    'Epic Team', ]
epicOutputFilename = ('Epic_Output.csv')
# Used to capture issue information
issueOutput = []
issueHeader = [
    'Issue Key',
    'Issue Aggregate Time Estimate',
    'Issue Aggregate Time Original Estimate',
    'Issue Aggregate Time Spent',
    'Issue Assignee Name',
    'Issue Assignee Email',
    'Issue Assignee Display Name',
    'Issue Created Date',
    'Issue Creator Name',
    'Issue Creator Email',
    'Issue Creator Display Name',
    'Issue Description',
    'Issue Due Date',
    'Issue Environment',
    'Issue Fix Versions',
    'Issue Issue Type',
    'Issue Labels',
    'Issue Priority',
    'Issue Priority Icon',
    'Issue Progress',
    'Issue Progress Total',
    'Issue Project',
    'Issue Reporter Name',
    'Issue Reporter Email',
    'Issue Reporter Display Name',
    'Issue Resolution',
    'Issue Resolution Date',
    'Issue Status',
    'Issue Status Icon',
    'Issue Summary',
    'Issue Time Estimate',
    'Issue Time Original Estimate',
    'Issue Time Spent',
    'Issue Updated',
    'Issue Link',
    'Issue Flagged',
    'Issue Theme',
    'Issue Release Version History',
    'Issue Geographic Region',
    'Issue Units',
    'Issue Percent Done',
    'Issue Due Time',
    'Issue Requested By',
    'Issue Start Date',
    'Issue Business Summary',
    'Issue CR#',
    'Issue Approved Date',
    'Issue CAR#',
    'Issue ServiceNow Incident#',
    'Issue Rank',
    'Issue Team', ]
issueOutputFilename = ('Issue_Output.csv')

# Current date time
currDate = time.strftime("%Y_%m_%d_%H%M%S")

# ###############################################################################

def main():

    # Get Epics
    rjira_search = requests.get(jirasearch, params=jira_epic_payload)

    if rjira_search.status_code == requests.codes.ok:
        jira_results = jira_search(rjira_search)

        json_epic(jira_results)

    # Get Issues
    rjira_search = requests.get(jirasearch, params=jira_issue_payload)

    if rjira_search.status_code == requests.codes.ok:
        jira_results = jira_search(rjira_search)

        json_issue(jira_results)

    return


# ##############################################################################

def request_info(request):
    print('Url:', request.url)
    print('Encoding:', request.encoding)
    print('Headers:', request.headers)
    print('Cookies:', request.cookies)
    print('JSON:', request.json())

    return


# ##############################################################################

def jira_search(search_results):

    jira_search_json = search_results.json()

    print('jira_epic_json type = ', type(jira_search_json))
    print('jira_epic_json keys = ', jira_search_json.keys())
    print('jira_epic_json startAt = ', jira_search_json['startAt'])
    print('jira_epic_json maxResults = ', jira_search_json['maxResults'])
    print('jira_epic_json total = ', jira_search_json['total'])

    print('###########################')

    # Create jira_issues object
    jira_issues = jira_search_json['issues']  # Returns List Object
    print('jira_issues type = ', type(jira_issues))

    print('jira_issues len = ', (len(jira_issues)))
    print('###########################')

    return jira_issues


def json_epic(request):
    for item in request:

        itemList = []
        itemList.append(item['key'])
        itemList.append((item['versionedRepresentations']['aggregatetimeestimate']['1']))
        itemList.append((item['versionedRepresentations']['aggregatetimeoriginalestimate']['1']))
        itemList.append((item['versionedRepresentations']['aggregatetimespent']['1']))

        if item['versionedRepresentations']['assignee']['1']:
            itemList.append((item['versionedRepresentations']['assignee']['1']['name']))
            itemList.append((item['versionedRepresentations']['assignee']['1']['emailAddress']))
            # itemList.append((item['versionedRepresentations']['assignee']['1']['key']))
            itemList.append((item['versionedRepresentations']['assignee']['1']['displayName']))
        else:
            itemList.append(None)
            itemList.append(None)
            # itemList.append(None)
            itemList.append(None)

        # itemList.append((item['versionedRepresentations']['components']['1']))
        itemList.append((item['versionedRepresentations']['created']['1']))
        itemList.append((item['versionedRepresentations']['creator']['1']['name']))
        itemList.append((item['versionedRepresentations']['creator']['1']['emailAddress']))
        # itemList.append((item['versionedRepresentations']['creator']['1']['key']))
        itemList.append((item['versionedRepresentations']['creator']['1']['displayName']))
        itemList.append((item['versionedRepresentations']['description']['1']))
        itemList.append((item['versionedRepresentations']['duedate']['1']))
        itemList.append((item['versionedRepresentations']['environment']['1']))

        if item['versionedRepresentations']['fixVersions']['1']:
            itemList.append((item['versionedRepresentations']['fixVersions']['1'][0]['name']))
        else:
            itemList.append('None')

        # itemList.append((item['versionedRepresentations']['issuelinks']['1']))
        itemList.append((item['versionedRepresentations']['issuetype']['1']['name']))
        itemList.append((item['versionedRepresentations']['labels']['1']))
        itemList.append((item['versionedRepresentations']['priority']['1']['name']))
        # itemList.append((item['versionedRepresentations']['priority']['1']['iconUrl']))

        priorityIcon = '<img src="{}" alt="{}">'.format(item['versionedRepresentations']['priority']['1']['iconUrl'],
                                                        item['versionedRepresentations']['priority']['1']['name'])
        itemList.append(priorityIcon)

        itemList.append((item['versionedRepresentations']['progress']['1']['progress']))
        itemList.append((item['versionedRepresentations']['progress']['1']['total']))
        itemList.append((item['versionedRepresentations']['project']['1']['name']))
        itemList.append((item['versionedRepresentations']['reporter']['1']['name']))
        itemList.append((item['versionedRepresentations']['reporter']['1']['emailAddress']))
        # itemList.append((item['versionedRepresentations']['reporter']['1']['key']))
        itemList.append((item['versionedRepresentations']['reporter']['1']['displayName']))
        itemList.append((item['versionedRepresentations']['resolution']['1']))
        itemList.append((item['versionedRepresentations']['resolutiondate']['1']))
        itemList.append((item['versionedRepresentations']['status']['1']['name']))
        # itemList.append((item['versionedRepresentations']['status']['1']['iconUrl']))

        statusIcon = '<img src="{}" alt="{}">'.format(item['versionedRepresentations']['status']['1']['iconUrl'],
                                                      item['versionedRepresentations']['status']['1']['name'])
        itemList.append(statusIcon)

        # itemList.append((item['versionedRepresentations']['subtasks']['1']))
        itemList.append((item['versionedRepresentations']['summary']['1']))
        itemList.append((item['versionedRepresentations']['timeestimate']['1']))
        itemList.append((item['versionedRepresentations']['timeoriginalestimate']['1']))
        itemList.append((item['versionedRepresentations']['timespent']['1']))
        itemList.append((item['versionedRepresentations']['updated']['1']))
        # itemList.append((item['versionedRepresentations']['versions']['1']))

        
        # if item['versionedRepresentations']['customfield_10000']['2']: # Sprint
        # itemList.append((item['versionedRepresentations']['customfield_10000']['2']))
        # itemList.append((item['versionedRepresentations']['customfield_10000']['2'][0]['name']))
        # itemList.append((item['versionedRepresentations']['customfield_10000']['2'][1]['name']))
        itemList.append((item['versionedRepresentations']['customfield_10001']['1']))  # Epic Link
        # itemList.append((item['versionedRepresentations']['customfield_10002']['1'])) #

        # itemList.append((item['versionedRepresentations']['customfield_10003']['1']))  # Epic Status

        itemList.append((item['versionedRepresentations']['customfield_10006']['1']))  # Flagged
        itemList.append((item['versionedRepresentations']['customfield_10007']['1']))  # Epic/Theme
        itemList.append((item['versionedRepresentations']['customfield_10008']['1']))  # Story Points
        itemList.append((item['versionedRepresentations']['customfield_10009']['1']))  # Business Value
        itemList.append((item['versionedRepresentations']['customfield_10100']['1']))  # Release version History

        # itemList.append((item['versionedRepresentations']['customfield_10400']['1'])) # issueFunction
        if item['versionedRepresentations']['customfield_10401']['1']:  # Geographic Region
            itemList.append((item['versionedRepresentations']['customfield_10401']['1'][0]['value']))
        else:
            itemList.append('None')

        itemList.append((item['versionedRepresentations']['customfield_10403']['1']))  # Units
        itemList.append((item['versionedRepresentations']['customfield_10404']['1']))  # PercentDone
        itemList.append((item['versionedRepresentations']['customfield_10405']['1']))  # DueTime
        itemList.append((item['versionedRepresentations']['customfield_10500']['1']))  # Requested by

        itemList.append((item['versionedRepresentations']['customfield_10600']['1']))  # Start Date
        itemList.append((item['versionedRepresentations']['customfield_10700']['1']))  # Business Summary
        itemList.append((item['versionedRepresentations']['customfield_11000']['1']))  # CR#
        itemList.append((item['versionedRepresentations']['customfield_11100']['1']))  # Approved Date
        itemList.append((item['versionedRepresentations']['customfield_11101']['1']))  # CAR#
        itemList.append((item['versionedRepresentations']['customfield_11102']['1']['value']))  # Funding Required
        itemList.append((item['versionedRepresentations']['customfield_11103']['1']))  # ServiceNow Incident#
        itemList.append((item['versionedRepresentations']['customfield_11400']['1']))  # Rank
        # itemList.append((item['versionedRepresentations']['customfield_11500']['1'])) # MSTR_SEARCH_GUID
        # itemList.append((item['versionedRepresentations']['customfield_11800']['1'])) # MSTR_PROJECT
        itemList.append((item['versionedRepresentations']['customfield_12400']['1']))  # Team
        # itemList.append((item['versionedRepresentations']['customfield_12401']['1'])) # Parent Link

        epicOutput.append(itemList)

        # print(itemList)

    csv_output(epicOutput, epicHeader, epicOutputFilename)
    # jira_issues_versioned2 = jira_epic_json['issues']['versionedRepresentations']
    # jira_issues_versioned = jira_issues['versionedRepresentations']


    # print('Total:', jira_epic_json['total'])
    # print('Issues:', jira_epic_json['issues'])

    # pprint(epicOutput)
    # print(tabulate(epicOutput))

    return


def json_issue(request):
    for item in request:

        itemList = []
        itemList.append(item['key'])
        # itemList.append(item['versionedRepresentations']['aggregateprogress']['1'])

        # itemList.append((item['versionedRepresentations']['aggregateprogress']['1']))

        itemList.append((item['versionedRepresentations']['aggregatetimeestimate']['1']))
        itemList.append((item['versionedRepresentations']['aggregatetimeoriginalestimate']['1']))
        itemList.append((item['versionedRepresentations']['aggregatetimespent']['1']))

        if item['versionedRepresentations']['assignee']['1']:
            itemList.append((item['versionedRepresentations']['assignee']['1']['name']))
            itemList.append((item['versionedRepresentations']['assignee']['1']['emailAddress']))
            # itemList.append((item['versionedRepresentations']['assignee']['1']['key']))
            itemList.append((item['versionedRepresentations']['assignee']['1']['displayName']))
        else:
            itemList.append(None)
            itemList.append(None)
            # itemList.append(None)
            itemList.append(None)

        # itemList.append((item['versionedRepresentations']['components']['1']))
        itemList.append((item['versionedRepresentations']['created']['1']))
        itemList.append((item['versionedRepresentations']['creator']['1']['name']))
        itemList.append((item['versionedRepresentations']['creator']['1']['emailAddress']))
        # itemList.append((item['versionedRepresentations']['creator']['1']['key']))
        itemList.append((item['versionedRepresentations']['creator']['1']['displayName']))
        itemList.append((item['versionedRepresentations']['description']['1']))
        itemList.append((item['versionedRepresentations']['duedate']['1']))
        itemList.append((item['versionedRepresentations']['environment']['1']))

        if item['versionedRepresentations']['fixVersions']['1']:
            itemList.append((item['versionedRepresentations']['fixVersions']['1'][0]['name']))
        else:
            itemList.append('None')

        # itemList.append((item['versionedRepresentations']['issuelinks']['1']))

        itemList.append((item['versionedRepresentations']['issuetype']['1']['name']))
        itemList.append((item['versionedRepresentations']['labels']['1']))
        itemList.append((item['versionedRepresentations']['priority']['1']['name']))

        # itemList.append((item['versionedRepresentations']['priority']['1']['iconUrl']))

        priorityIcon = '<img src="{}" alt="{}">'.format(item['versionedRepresentations']['priority']['1']['iconUrl'],
                                                        item['versionedRepresentations']['priority']['1']['name'])
        itemList.append(priorityIcon)

        itemList.append((item['versionedRepresentations']['progress']['1']['progress']))
        itemList.append((item['versionedRepresentations']['progress']['1']['total']))

        itemList.append((item['versionedRepresentations']['project']['1']['name']))
        itemList.append((item['versionedRepresentations']['reporter']['1']['name']))
        itemList.append((item['versionedRepresentations']['reporter']['1']['emailAddress']))
        # itemList.append((item['versionedRepresentations']['reporter']['1']['key']))
        itemList.append((item['versionedRepresentations']['reporter']['1']['displayName']))
        itemList.append((item['versionedRepresentations']['resolution']['1']))
        itemList.append((item['versionedRepresentations']['resolutiondate']['1']))
        itemList.append((item['versionedRepresentations']['status']['1']['name']))

        # itemList.append((item['versionedRepresentations']['status']['1']['iconUrl']))
        statusIcon = '<img src="{}" alt="{}">'.format(item['versionedRepresentations']['status']['1']['iconUrl'],
                                                      item['versionedRepresentations']['status']['1']['name'])
        itemList.append(statusIcon)

        # itemList.append((item['versionedRepresentations']['subtasks']['1']))
        itemList.append((item['versionedRepresentations']['summary']['1']))
        itemList.append((item['versionedRepresentations']['timeestimate']['1']))
        itemList.append((item['versionedRepresentations']['timeoriginalestimate']['1']))
        itemList.append((item['versionedRepresentations']['timespent']['1']))
        itemList.append((item['versionedRepresentations']['updated']['1']))
        # itemList.append((item['versionedRepresentations']['versions']['1']))

        # Iterate through all Epics
        # if item['versionedRepresentations']['customfield_10000']['2']: # Sprint
        # itemList.append((item['versionedRepresentations']['customfield_10000']['2']))
        # itemList.append((item['versionedRepresentations']['customfield_10000']['2'][0]['name']))
        # itemList.append((item['versionedRepresentations']['customfield_10000']['2'][1]['name']))
        itemList.append((item['versionedRepresentations']['customfield_10001']['1']))  # Epic Link
        # itemList.append((item['versionedRepresentations']['customfield_10002']['1'])) #

        # itemList.append((item['versionedRepresentations']['customfield_10003']['1']))  # Epic Status

        itemList.append((item['versionedRepresentations']['customfield_10006']['1']))  # Flagged
        itemList.append((item['versionedRepresentations']['customfield_10007']['1']))  # Epic/Theme
        # itemList.append((item['versionedRepresentations']['customfield_10008']['1'])) # Story Points
        # itemList.append((item['versionedRepresentations']['customfield_10009']['1'])) # Business Value
        itemList.append((item['versionedRepresentations']['customfield_10100']['1']))  # Release version History

        # itemList.append((item['versionedRepresentations']['customfield_10400']['1'])) # issueFunction
        if item['versionedRepresentations']['customfield_10401']['1']:  # Geographic Region
            itemList.append((item['versionedRepresentations']['customfield_10401']['1'][0]['value']))
        else:
            itemList.append('None')

        itemList.append((item['versionedRepresentations']['customfield_10403']['1']))  # Units
        itemList.append((item['versionedRepresentations']['customfield_10404']['1']))  # PercentDone
        itemList.append((item['versionedRepresentations']['customfield_10405']['1']))  # DueTime
        itemList.append((item['versionedRepresentations']['customfield_10500']['1']))  # Requested by

        itemList.append((item['versionedRepresentations']['customfield_10600']['1']))  # Start Date
        itemList.append((item['versionedRepresentations']['customfield_10700']['1']))  # Business Summary
        itemList.append((item['versionedRepresentations']['customfield_11000']['1']))  # CR#
        itemList.append((item['versionedRepresentations']['customfield_11100']['1']))  # Approved Date
        itemList.append((item['versionedRepresentations']['customfield_11101']['1']))  # CAR#
        # itemList.append((item['versionedRepresentations']['customfield_11102']['1']['value'])) # Funding Required
        itemList.append((item['versionedRepresentations']['customfield_11103']['1']))  # ServiceNow Incident#
        itemList.append((item['versionedRepresentations']['customfield_11400']['1']))  # Rank
        # itemList.append((item['versionedRepresentations']['customfield_11500']['1'])) # MSTR_SEARCH_GUID
        # itemList.append((item['versionedRepresentations']['customfield_11800']['1'])) # MSTR_PROJECT
        itemList.append((item['versionedRepresentations']['customfield_12400']['1']))  # Team
        # itemList.append((item['versionedRepresentations']['customfield_12401']['1'])) # Parent Link

        issueOutput.append(itemList)

        # print(itemList)

    csv_output(issueOutput, issueHeader, issueOutputFilename)
    # jira_issues_versioned2 = jira_epic_json['issues']['versionedRepresentations']
    # jira_issues_versioned = jira_issues['versionedRepresentations']


    # print('Total:', jira_epic_json['total'])
    # print('Issues:', jira_epic_json['issues'])

    # pprint(epicOutput)
    # print(tabulate(epicOutput))

    return


def csv_output(jiraList, header, filename):
    # Check if existing csv file already exists
    if os.path.isfile(filename):
        # print("file exists")
        # fh = open(filename, "a")
        # writer = csv.writer(fh, delimiter=',')
        os.remove(filename)

    # mstrList = mstrHeader
    # print(mstrList)
    fh = open(filename, "w")
    writer = csv.writer(fh, delimiter=',')
    writer.writerow(header)

    writer.writerows(jiraList)

    fh.close()


# ##############################################################################


if __name__ == "__main__":
    main()
