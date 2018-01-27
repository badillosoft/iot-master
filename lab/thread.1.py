import threading
import time

def task_1():
    for i in range(10):
        print("TASK 1 %d" % i)
        time.sleep(1)

def task_2():
    for i in range(5):
        print("TASK 2 %d" % i)
        time.sleep(2)

threading.Thread(target=task_1).start()
threading.Thread(target=task_2).start()

print("Tareas iniciadas...")

