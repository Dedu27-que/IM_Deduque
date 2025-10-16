from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/output', methods=['POST'])
def output():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    sex = request.form['sex']
    status = request.form['status']
    location = request.form['location']
    return render_template('output.html', firstname=firstname, lastname=lastname, sex=sex, status=status, location=location)

if __name__ == '__main__':
    app.run(debug=True)
