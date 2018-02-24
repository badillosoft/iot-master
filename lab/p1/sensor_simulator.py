from threading import Thread
import random
import time

humidity = 0
temperature = 0
valid = False

humidity_buff = []
temperature_buff = []

running = False

def task():
    global humidity, temperature, valid

    while running:
        valid = random.random() < 0.9

        if valid:
            humidity = random.uniform(0, 100)
            temperature = random.uniform(0, 100)

        humidity_buff.append(humidity)
        temperature_buff.append(temperature)

        if len(humidity_buff) > 100:
            humidity_buff.pop(0)

        if len(temperature_buff) > 100:
            temperature_buff.pop(0)

        print("DTH11/SIM: H={:.2f} T={:.2f} V={}".format(humidity, temperature, valid))

        time.sleep(1)

def stop():
    global running
    running = False

def start():
    global running

    if running:
        print("DTH11/SIM is running")
        return

    running = True
    thread = Thread(target=task)
    thread.start()

if __name__ == "__main__":
    start()