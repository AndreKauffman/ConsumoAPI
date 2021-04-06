import requests

receber_cep = input('Digite seu CEP: ')

if len(receber_cep) != 8:
    print(f"O CEP: {receber_cep} é invalido...")
    exit()

request = requests.get(f'https://viacep.com.br/ws/{receber_cep}/json/')
pegar_chaves_json = request.json()

if pegar_chaves_json['complemento'] == '':
    pegar_chaves_json['complemento'] = 'casa 1'

if 'erro' not in pegar_chaves_json:
    for c in pegar_chaves_json:
        print(f'{c} : {pegar_chaves_json[c]}')
else:
    print('o cep é invalido!!!')

