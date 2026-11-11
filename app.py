import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    student = os.environ.get("Чиженко Д.О. / ЗКІ-23 ")
    return f"Hello World!: {student}"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)