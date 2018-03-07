from time import time, sleep


class StopWatchException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class StopWatch:
    def __init__(self, initial_time=0.0):
        self.time_since_stop = initial_time
        self.start_time = 0
        self.stopped = True

    def start(self):
        if not self.stopped:
            raise(StopWatchException("cannot start a stop watch already running"))
        self.start_time = time()
        self.stopped = False

    def stop(self):
        if self.stopped:
            raise(StopWatchException("cannot stop a stop watch already stopped"))
        self.stopped = True
        self.time_since_stop += (time() - self.start_time)

    def reset(self):
        self.time_since_stop = 0
        self.stopped = True

    def get_time(self):
        if self.stopped:
            return self.time_since_stop
        else:
            return self.time_since_stop + (time() - self.start_time)

    def __lt__(self, other):
        return self.get_time() < other.get_time()

    def __eq__(self, other):
        return self.get_time() == other.get_time()

    def __str__(self):
        t = self.get_time()
        n_hours = int(t // 3600)
        t -= 3600 * n_hours
        n_min = int(t // 60)
        t -= 60 * n_min
        n_sec = int(t)
        t -= n_sec
        n_hundreds = round(t * 100)
        return "{}H:{}m:{}s:{}".format(str(n_hours), str(n_min), str(n_sec), str(n_hundreds))


print("Creating watch at 5.22 seconds")
watch = StopWatch(5.22)
print(watch)
print("Starting watch and waiting 1 second")
watch.start(); sleep(1); print(watch)
print("Waiting one more second")
sleep(1); print(watch)
print("Stopping and waiting 1 second, watch is the same")
watch.stop(); sleep(1); print(watch)
print("Starting watch again and waiting 1 second")
watch.start(); sleep(1); print(watch)
print("Resetting watch")
watch.reset(); print(watch)
print("Starting and waiting 1 second")
watch.start(); sleep(1); print(watch)
print("Pretty print a watch:", StopWatch(12313.327))
print("equals and <:")
print(StopWatch(5.22) == StopWatch(5.22))
print(StopWatch() < StopWatch(2.0))
print("Stopping a stopped watch raises an exception:")
StopWatch().stop()
print("Starting a started watch raises an exception:")
watch = StopWatch()
watch.start(); watch.start()
