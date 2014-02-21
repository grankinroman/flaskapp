import os
from flask import Flask, render_template, send_from_directory

#----------------------------------------
# initialization
#----------------------------------------
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)
app.config["SECRET_KEY"] = "2FsB\xda\x0frx18!rx17;a\xbd42A\xbbYx#h\x9e7\xf2"

#----------------------------------------
# database
#----------------------------------------

from mongoengine import connect
from flask.ext.mongoengine import MongoEngine

app.config["MONGODB_DB"] = "heroku_app22379827"
connect("heroku_app22379827", host='mongodb://heroku_app22379827:bservo27gf1agn0jn2p3cneuru@ds033629.mongolab.com:33629/heroku_app22379827')
db = MongoEngine(app)

#----------------------------------------
# controllers
#----------------------------------------
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')

#----------------------------------------
# launch
#----------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)