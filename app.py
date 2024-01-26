from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "M.Birza Putra Nasution, 2119121710, Teknik Informatika"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
