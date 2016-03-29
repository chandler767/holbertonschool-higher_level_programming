import requests

headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 89a061b4ed9ecbfd9801450418d3af551b06c4ae'
}  
for item in requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers=headers).json()['items']:
	print item['full_name']
