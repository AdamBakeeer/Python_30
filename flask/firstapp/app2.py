from flask import Flask, request, make_response, render_template


app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = 'hoo hoo'
    myresult = 10 + 20
    return render_template('index.html', myvalue=myvalue, myresult=myresult)


@app.route('/other')
def other():
    some_text = 'Hello world'
    return render_template('other.html', some_text=some_text)

@app.template_filter('reverse_string')
def reverse_string(s):
    return s [::-1]

@app.template_filter('repeat')
def repeat(s, time=2):
    return s * time

@app.template_filter('alt')
def alt(s):
    return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)