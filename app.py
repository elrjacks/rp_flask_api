# app.py
# gets a basic web server up and running and makes it
# respond with a home.html template

import connexion
# access to flask functionality
from flask import render_template


# flask application instance called app
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)