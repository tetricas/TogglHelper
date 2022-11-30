from jira.jira_sender import JiraSender
from jira import jira_rest
from utils import outside_task


def get_jira_tasks(start_date):
    tasks = list(query_jira_tasks(start_date))
    tasks.sort(key=lambda el: el.start_at, reverse=True)
    return tasks


def query_jira_tasks(start_date):
    jql = f'worklogDate>={start_date} AND worklogAuthor=currentUser()'
    issues_url = jira_rest.host + jira_rest.search_route + jql
    jira = JiraSender()

    for issue in jira.get_request(issues_url)['issues']:
        issue_id = issue['id']
        key = issue['key']
        summary = issue['fields']['summary']
        name = f'[{key}] {summary}'

        worklogs_url = jira_rest.host + jira_rest.issues_route + issue_id + jira_rest.worklog_route
        for worklog in jira.get_request(worklogs_url)['worklogs']:
            try:
                content = worklog['comment']['content'][0]['content']
                if content[0]['type'] == 'listItem':
                    text = str()
                    for element in content:
                        text += element['content'][0]['content'][0]['text'] + ' and '
                    text = text[:-5]
                else:
                    text = content[0]['text']
            except KeyError as err:
                text = "done"
            created = worklog['started']
            time_spent = worklog['timeSpentSeconds'] / 3600

            yield outside_task.OutsideTask(f'{name}: {text}', created, time_spent)
