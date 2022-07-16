import threading
import time
import queue
from random import randrange

##### SIMPLE THREADING ####
# this function will be running in a separate thread
def thread_function(name):
    for i in range(10):
        time.sleep(1)
        print(name)

# set daemon = True if you want the threadded code to be completely independent from the main code (i.e. it can run after the main code terminates)
x = threading.Thread(target = thread_function, args = ("steve", ), daemon = False)

x.start()
print("outside the other thread!")
x.join()
print("the other thread is done")


#### DEALING WITH MUTEXES ######
class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock() #this is your mutex

    # mutex-protected update
    def locked_update(self, name):
        with self._lock:
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

##### THIS IS A CONVENIENT THREADPOOL ######
class Worker(threading.Thread):
    """Thread executing tasks from a given tasks queue"""
    def __init__(self, tasks):
        threading.Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception:
                print("whoops!")
            finally:
                self.tasks.task_done()


class ThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads):
        self.tasks = queue.Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()


# toy example for the threadpool 
delays = [randrange(1, 10) for i in range(100)]
def wait_delay(d):
    print(f"sleeping! {d}")
    time.sleep(d)

pool = ThreadPool(20) #number of workers

for i, d in enumerate(delays):
    pool.add_task(wait_delay, d)

pool.wait_completion()
