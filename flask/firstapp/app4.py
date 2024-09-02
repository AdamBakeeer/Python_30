from flask import Flask, render_template


app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/')
def image():
    return render_template('image.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)