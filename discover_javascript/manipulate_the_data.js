var https = require('https');

var options = {
  hostname: 'api.github.com',
  path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
  headers: {
    'User-Agent': 'Holberton_School',
    'Authorization': 'token ' + process.env.TOKEN
  }
}

var req = https.get(options, function (res) {
    const chunks = [];
    var jsonString = '';
    res.on('data', (chunk) => {
        chunks.push(chunk);
    });
    res.on('end', () => {
        jsonString = chunks.join('');
        var jsonobject = JSON.parse(jsonString);
        var full_names = jsonobject.items.map(function(obj){
            return obj.full_name;
        });

        console.log(full_names.join('\n'));
    });
});

req.on('error', function (e) {
    console.error(e);
});