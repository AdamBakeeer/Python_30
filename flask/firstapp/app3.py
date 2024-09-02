from flask import Flask, request, make_response, render_template


app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index2():
    if request.method == 'GET':
        return render_template('index2.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'adam' and password == 'password':
            return 'success'
        else:
            return 'failure'
        
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    

    




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)