import asyncio

from app.services.get_org_repos import get_org_repos
from app.services.get_repo_issues import get_repo_issues
from app.services.close_issue import probot

print("STARTING")
repositories = []
repositories = get_org_repos()
total_issues = 0
if repositories:
    print(f"Se encontraron {len(repositories)} repositorios:")
    for repo in repositories:
        print(repo)
        issues_array = []
        issues_array = asyncio.run(get_repo_issues(repo))
        total_issues += len(issues_array)
        if len(issues_array) > 0:
            for issue in issues_array:
                asyncio.run(probot.close_issue(repo, str(issue)))

print("Finalizado con exito")
print("Total de issues limpiados: ", total_issues)





