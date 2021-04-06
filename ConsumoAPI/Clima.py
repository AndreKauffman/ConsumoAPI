import requests
request = requests.get(
    f'http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=7d1c54f2a2bd5451fe8203f05c9c7c54')
print(request.json())
