from flask import Flask, render_template, request, redirect
from file_proc import pievienot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/kontakti')
def kontakti():
    return render_template('kontakti.html')

@app.route('/par_mani')
def par_mani():
    return render_template('par_mani.html')

@app.route('/jaunumi')
def jaunumi():
    return render_template('jaunumi.html')

@app.route('/postdata', methods = ['POST', 'GET'])
def postdata():
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        #print(request.form)
        vards = request.form.get('vards')
        pievienot(vards)
        return redirect('/kontakti')
    else:
        return "Nevajag Tev"

if __name__ == '__main__':
    app.run(port=80, debug=True)

