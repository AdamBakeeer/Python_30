from flask import Flask, request, make_response


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
         return 'You made a GET request'
    elif request.method == 'POST':
         return 'yOU MADE A post REQUEST'
    
@app.route('/hellor')
def hrllor():
     return 'hellow world\n', 

@app.route('/greet/<name>')
def greet(name):
      return f"hellow {name}"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
      return f"{number1} + {number2} = {number1 + number2}"

@app.route('/handle_url')
def handle_params():
      if 'greeting' in request.args.keys() and 'name' in request.args.keys():
            greeting = request.args.get('greeting')
            name = request.args.get('name')
            return f"{greeting}, {name}"
      else:
            return " Some parameters are missing"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)