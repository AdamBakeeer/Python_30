from flask import Flask, render_template, session


app = Flask(__name__, template_folder='templates')
app.secret_key = 'SOME KEY'

@app.route('/')
def index3():
    return render_template('index3.html', message='Index')

@app.route('/set_data')
def set_data():
    session['name'] = 'mike'
    session['other'] = 'hello world'
    return render_template('index.html', message='session data set')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)