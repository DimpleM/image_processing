import threading
import time


class myThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()

    def run(self):
        i = 0
        print('Starting Thread {} '.format(self.name))
        while self.__running.isSet():
            self.__flag.wait()
            print("Thread {0} is running at {1}  ".format(self.name, i))
            time.sleep(5)
            i = i + 5

    def pause(self):
        print("Pausing thread {}".format(self.name))
        self.__flag.clear()

    def resume(self):
        print("Resuming thread {}".format(self.name))
        self.__flag.set()

    def stop(self):
        print("Stopping thread {}".format(self.name))
        self.__flag.set()
        self.__running.clear()

if __name__ == "__main__":
    t1 = myThread(1)
    t2 = myThread(2)
    t3 = myThread(3)
    t1.start()
    t3.start()
    time.sleep(20)
    t1.pause()
    t2.start()
    time.sleep(18)
    t3.stop()
    t1.resume()
    time.sleep(10)
    t1.stop()
    t2.stop()
    t3.stop()
