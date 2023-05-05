import requests
import json
from app import config
from app.services.repository_to_check import repository_to_check
def get_org_repos():
    url = 'https://api.github.com/orgs/<owner/repos?type=all'
    params = {'per_page': 100, 'page': 1}

    repo_names = []

    while True:
        response = requests.get(url, headers=config.HEADER, params=params)

        response.raise_for_status()
        response_json = json.loads(response.text)

        # Salir del bucle si no hay más resultados
        if not response_json:
            break

        # Obtener nombres de repositorios y agregarlos a la lista
        for repo in response_json:
            if repository_to_check(repo['name']):
                repo_names.append(repo['name'])

        params['page'] += 1
        print('-')

    if repo_names:
        return repo_names
    else:
        raise ValueError('fallo')
