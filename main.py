from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/kontakti')
def kontakti():
    return "<html><h1>Kontakti</h1><p>Jānis  Graudiņš</p></html>"

if __name__ == '__main__':
    app.run(port=80, debug=True)

