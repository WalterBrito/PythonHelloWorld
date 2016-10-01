# -*- coding: utf-8 -*-

import os
from flask import Flask

app = Flask(_name_)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
