import datetime
import flask

from time import sleep

from microservice import (microservice, initialise_interface, terminate_interface, create_deployment,
                          destroy_deployment, configure_logging)


app = flask.Flask(__name__)


@microservice
def hints(host, port):
    return """
    Try navigating to the following links:
    http://{host}:{port}/
    http://{host}:{port}/hello
    http://{host}:{port}/hello/World
    http://{host}:{port}/time
    http://{host}:{port}/bottles/99
    http://{host}:{port}/ticktock/99
    """.format(host=host, port=port)


@microservice
def green_bottles(song, num_bottles):
    if num_bottles > 0:
        song += "{} bottles of beer on the wall.<br/>".format(num_bottles)
        return green_bottles(song, decrementer(num_bottles))
    return song


@microservice
def decrementer(number):
    return number - 1


@microservice
def tick(text, counter):
    if counter > 0:
        text += "tick: {}<br/>".format(counter)
        return tock(text, decrementer(counter))
    return text


@microservice
def tock(text, counter):
    if counter > 0:
        text += "tock: {}<br/>".format(counter)
        return tick(text, decrementer(counter))
    return text


@microservice
def hello_world_service():
    return "Hello, world!"


@microservice
def hello_name_service(name):
    return "Greetings, {}! Have an awesome day!".format(name)


@microservice
def time_of_day_service():
    return datetime.datetime.now()


@app.route('/')
def homepage():
    return "Welcome to the microservice example project!"


@app.route('/hello')
def hello():
    return hello_world_service()


@app.route('/hello/<string:name>/')
def hello_name(name):
    return hello_name_service(name)


@app.route('/time')
def time():
    return str(time_of_day_service())


@app.route('/bottles/<int:num_bottles>/')
def bottles(num_bottles):
    return green_bottles("", num_bottles)


@app.route('/ticktock/<int:counter>/')
def ticktock(counter):
    return tick("", counter)


def main():
    configure_logging(__name__)
    initialise_interface(__name__)

    # Must have imported all modules that contain microservices before this point for auto-detection to work.
    create_deployment()

    sleep(1)  # Wait for the services to initialise
    print(hints('127.0.0.1', 4000))

    app.run(threaded=True, port=4000)
    terminate_interface()
    destroy_deployment()


if __name__ == "__main__":
    main()
