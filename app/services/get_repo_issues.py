import requests
import json
import asyncio
from app import config
from app.services.issue_to_check import issue_to_check
async def get_repo_issues(repository: str):
    url = f'https://api.github.com/repos/<owner>/{repository}/issues'
    params = {'per_page': 100, 'page': 1}
    issues = []

    while True:
        await asyncio.sleep(1)
        response = requests.get(url, headers=config.HEADER, params=params)
        response.raise_for_status()
        response_json = json.loads(response.text)
        if not response_json:
            break

        for issue in response_json:
            
            if issue_to_check(issue['title']):
                issues.append(issue['number'])

        params['page'] += 1

    return issues