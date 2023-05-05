import requests
import socket
import asyncio
import json

from app import config

class probot: 

    async def close_issue(repository: str, issue_number: str):
        await asyncio.sleep(1)
        probot_url = ('<probot-end-point>' +
                        '/repos/<owner>/{repository}/issues/{issue_number}').format(repository=repository, issue_number= issue_number)
        data = {
            'state': 'closed'
        }
        probot_headers = probot.get_probot_headers()
        response = requests.patch(probot_url, headers=probot_headers, data=json.dumps(data))

        if response.status_code == 204 or response.status_code == 200:
            print(f'El issue {issue_number} del repositorio {repository} se cerro correctamente')
        else:
            # Imprimir un mensaje de error si la solicitud falló
            print(f'La solicitud de cierre del issue {issue_number} del repositorio {repository} fallo, con el código de estado {response.status_code}')

    @staticmethod
    def get_probot_headers():
        hostname = socket.gethostname()
        return {
            'X-Channel': 'Web',
            'X-IpAddr': socket.gethostbyname(hostname),
            'X-Name': 'Transversales',
            'Content-Type': 'application/json',
            'x-api-key': '<pobot-api-key>'
        }