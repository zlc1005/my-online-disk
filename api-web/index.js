const request = require("request")
const express = require("express")
const querystring = require('querystring');
var url = require('url');
const fs = require("fs")
const app=express() //makes computer a local server

app.listen(process.env.PORT || 3000, function(){
  console.log("Server is running on port 3000")
});

app.get("/xxx", function(req, res){ //first parameter is the path, / which means the current folder
  var url_parts = url.parse(req.url, true);
  query = url_parts.query;
  res.send("hello")  //__dirname is current directory (two _)
  var dataString=''
  console.log(query);
  const newPerson = query
  fs.readFile('./data.json','utf-8',function(err, jsonString){
    if (err){
      console.log(err);
    }else{
        var data = JSON.parse(jsonString);
        data.push(newPerson);
        dataString=JSON.stringify(data);
        //console.log(data)
        fs.writeFileSync("./data.json",dataString, function(err){
          if (err){
            console.log(err);
          }else{
            console.log("successed");
          }
        })
    }
  });

});
app.get('/check', function(req,res){
  datagui=''
  fs.readFile('./data.json','utf-8',function(err, jsonString){
    if (err){
      console.log(err);
    }else{
        var data = JSON.parse(jsonString);
        for (var i = 0; i < data.length; i++) {
          datagui+=('name:'+data[i]['name']+"\n")
          datagui+=('level:'+data[i]['level']+"\n")
          datagui+=('iswin:'+data[i]['win']+"\n")
          datagui+='<br>'
        }
        res.send(datagui)
        //console.log(data)
    }
  });
})
app.get('/json', function(req,res){
  fs.readFile('./data.json','utf-8',function(err, jsonString){
    if (err){
      console.log(err);
    }else{
        var data = JSON.parse(jsonString)
        res.send(data)
        //console.log(data)
    }
  });
})
app.get('/delall', function(req,res){
  fs.readFile('./toleo.json','utf-8',function(err, jsonString){
    if (err){
      console.log(err);
    }else{
        var data = JSON.parse(jsonString);
        res.send(data)
        //console.log(data)
    }
  });
})

app.get('/delallnow', function(req,res){
fs.writeFileSync("./data.json","[]", function(err){
  if (err){
    console.log(err);
  }else{
    console.log("successed");
    // res.send("successed")
  }
});
res.send('success');
})

app.get("/toleo", function(req, res){ //first parameter is the path, / which means the current folder
  var url_parts = url.parse(req.url, true);
  query = url_parts.query;
  res.send("hello")  //__dirname is current directory (two _)
  var dataString=''
  console.log(query);
  const newPerson = query
  jsonString='[]'
        var data = JSON.parse(jsonString);
        data.push(newPerson);
        dataString=JSON.stringify(data);
        //console.log(data)
        fs.writeFileSync("./toleo.json",dataString, function(err){
          if (err){
            console.log(err);
          }else{
            console.log("successed");
          }})
})