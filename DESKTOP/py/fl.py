from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(user):
        if user.is_logged_in:
            return function()
        else:
            return '<h1>You are not logged in!</h1>'
    return wrapper
@app.route('/user/<name>/profile')
def create_blog_post(name):
    return '<h1>Hello, %s!</h1>' % name
is_authenticated_decorator(create_blog_post)

new_user = User('Lucas')
new_user.is_logged_in = True
create_blog_post(new_user)

if __name__ == '__main__':
    app.run(debug=True)




# make a function to get the sum of a list
def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum 