"""
This example shows off farming out expensive requests to the microservice backend.

The example is as follows:
Every 0.1 seconds: Start a thread to calculate the sum of 10,000,000 random ints between 0 and 100.
"""
import flask
import random
import threading
import time

from microservice import microservice, initialise_interface


app = flask.Flask(__name__)


@microservice
def expensive_calculation():
    total = 0
    for i in range(10000000):
        total += random.randint(0, 100)
    return total


@app.route('/')
def homepage():
    thrds = []
    results = []
    for i in range(1000):
        thrd = threading.Thread(target=expensive_calculation)
        thrd.start()
        thrds.append(thrd)
        time.sleep(0.1)

    for thrd in thrds:
        thrd.join()

    return results


if __name__ == "__main__":
    app.run(threaded=True)
    initialise_interface(__name__)
