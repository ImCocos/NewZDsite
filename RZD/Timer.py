from threading import Thread
import time
from turtle import update

class Timer:
    def __init__(self):
        self.time = int(time.time())
    

    def update(self):
        self.time += 1
        time.sleep(1)
    

    def run(self):
        def runner():
            while True:
                self.update()
        self.t = Thread(target=runner)
    
    def stop(self):
        self.t._stop()
    
    def skip(self, s=None, m=None, h=None):
        if s is not None:
            self.time += s
        if m is not None:
            self.time += m * 60
        if h is not None:
            self.time += h * 3600
    
    def back(self, s=None, m=None, h=None):
        if s is not None:
            self.time -= s
        if m is not None:
            self.time -= m * 60
        if h is not None:
            self.time -= h * 3600


timer = Timer()
timer.run()
print('Start')

for i in range(0, 1000):
    print(timer.time)

timer.back(s=20)
print(timer.time)
timer.stop()

