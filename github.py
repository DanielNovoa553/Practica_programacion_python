import requests

def get_repositories(username, token):
    url = f'https://api.github.com/users/{username}/repos'
    headers = {
        'Authorization': f'token {token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repositories = response.json()
        for repo in repositories:
            print(repo['name'])
    else:
        print(f'Error: {response.status_code}')

# Reemplaza 'TU_NOMBRE_DE_USUARIO' y 'TU_TOKEN' con tus credenciales de GitHub
get_repositories('DanielNovoa553', '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')
