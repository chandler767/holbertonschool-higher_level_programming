var https = require('https');

var options = {
  hostname: 'api.github.com',
  path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
  headers: {
    'User-Agent': 'Holberton_School',
    'Authorization': 'token 93ec5a59a9aafb78d09ca58d42501d61a34cfc5a'
  }
}

var req = https.get(options, function(res) {
  const chunks = [];
  var jsonString = '';
  res.on('data', (chunk) => {
    chunks.push(chunk);
  });
  res.on('end', () => {
    jsonString = chunks.join('');
    console.log(typeof jsonString);
    console.log(jsonString);
  });
});