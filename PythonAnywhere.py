import requests
username = 'ericlima'
token = '53f7414cc6ab72233e95055841ebaab359f61375'

response = requests.get(
  'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
      username=username
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('CPU quota info:')
  print(response.content)
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))