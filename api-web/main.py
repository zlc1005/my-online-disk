from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def index():
    return 'sorry, can\'t open this page'
@app.route('/api/<name>/<iswin>/<li>/<ctime>')
def api(name, iswin, li, ctime):
    # try:
    with open('/l/12/lucasz228sd45/data.json',mode='r') as f:
        de=str(f.read())
        data=json.loads(de)
        # return data
    data.append({'name':name, 'iswin':iswin, 'li':li, 'ctime':ctime})
    with open('/l/12/lucasz228sd45/data.json',mode='w') as f:
        dd=json.dumps(data)
        f.write(dd)
    # except:
        # return f'api errror'
    # else:
        # return 'api white json success'
    return f'api success\n{dd}'

@app.route('/del/<name>')
def del_api(name):
    try:
        with open('C:\\Users\\29242\\OneDrive\\桌面\\JSONRW\\data.json',mode='r') as f:
            de=str(f.read())
            data=json.loads(de)
            # return data
        for i in data:
            if i['name']==name:
                data.remove(i)
        with open('C:\\Users\\29242\\OneDrive\\桌面\\JSONRW\\data.json',mode='w') as f:
            dd=json.dumps(data)
            f.write(dd)
    except:
        return f'del api errror'
    else:
        return f'del api success\n{dd}'


if __name__ == '__main__':
    app.run()# debug=True)