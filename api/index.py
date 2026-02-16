from flask import Flask, render_template
from flask_cors import CORS

from aiAgent import input_req
from until.response import response

app = Flask(__name__)
CORS(app)


@app.route("/api/invest/<target>")
def mikir(target):
    try:
        agent = input_req(target)

        return response(200, agent, "success")

    except Exception as e:
        return response(500, str(e), "error")


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/")
def health():
    return {"status": "ok"}
