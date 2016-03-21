require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 89a061b4ed9ecbfd9801450418d3af551b06c4ae'
}

filename = '/tmp/33'
uri = "https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc"
target = open(filename,'w')
target.truncate(0)
clin = HTTPClient.new

res = clnt.get_content uri, extheaders
target.write(res)
puts "The file was saved!"
target.close
