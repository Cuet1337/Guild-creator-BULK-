import requests

token = 'NzQ2NTkwNDg2MTQzMzAzNzIw.X0Cipw.2NnHhKm1otYrzmi9hUVnIbgS2TM'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
  }
request = requests.Session()
guild = {
    'channels': None, # Default channels
    'icon': None, # Guild logo/icon
    'name': "cuet1337", # Guild name 
    'region': "europe" #Region
}
for r in range(50):
    requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
print('Done.')
while True:
  input()
