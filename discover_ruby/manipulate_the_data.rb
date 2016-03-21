require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 89a061b4ed9ecbfd9801450418d3af551b06c4ae'
}

uri = "https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc"

clnt = HTTPClient.new
json_string = clnt.get_content(uri, extheaders)
res = JSON.parse(json_string)['items']

names = res.map {|e| e["full_name"]}
puts names.join("\n")
