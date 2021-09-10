from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Sveiks, jaukais pitons!"


@app.route('/kontakti')
def kontakti():
    return "<html><h1>Kontakti</h1><p>Jānis  Graudiņš</p></html>"

if __name__ == '__main__':
    app.run(port=80, debug=True)

