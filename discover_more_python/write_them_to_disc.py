import requests

headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 89a061b4ed9ecbfd9801450418d3af551b06c4ae'
}  
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
r = requests.get(url, headers=headers)
target = open ("/tmp/33.txt", 'w')
target.write(r.content)
target.close()
print "The file was saved!"
