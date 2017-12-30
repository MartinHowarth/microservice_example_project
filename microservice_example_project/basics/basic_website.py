import datetime
import flask

from microservice import microservice, initialise_interface


app = flask.Flask(__name__)


@microservice
def hello_world():
    return "Hello, world!"


@microservice
def hello_name(name):
    return "Greetings, {}! Have an awesome day!".format(name)


@microservice
def time_of_day():
    return datetime.datetime.now()


@app.route('/')
def homepage():
    return "Welcome to the microservice example project!"


@app.route('/hello')
def hello():
    return hello_world()


@app.route('/hello/<string:name>/')
def hello_name(name):
    return hello_name(name)


@app.route('/time')
def time():
    return time_of_day()


if __name__ == "__main__":
    app.run(threaded=True)
    initialise_interface(__name__)
