# app.py
# gets a basic web server up and running and makes it
# respond with a home.html template

# access to flask functionality
from flask import render_template

import config
from models import Person
# flask application instance called app
app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)