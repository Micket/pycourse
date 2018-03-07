## Stop watch

In this assignment you will create a class `StopWatch` that models a simple stopwatch with "start", "stop" and "reset" buttons.

The following methods should be implemented:

* A constructor that can accept an arbitrary starting time (in seconds), e.g. `StopWatch(5)` should create a stop watch
  that is initially set to 5 second.
* `start()` - Starts the watch. If the watch is already started, should raise a `StopWatchException` (create it yourself) with an
              informative error message.
* `stop()` - Stops the watch. If the watch is already stopped, should raise a `StopWatchException` with an informative error message.
* `reset()` - Resets the watch, i.e. sets the current elapsed time to 0 seconds and stops it.
* `get_time()` - Returns the current elapsed time, i.e. what is currently on the display of the stop watch (in seconds).

Methods should be overloaded so that the following functionality is available:

* Comparison between two watches using `<` and `==` based on the elapsed time.
* Pretty prining of watches in the format `{a}H:{b}m:{c}s:{d}` where `{a}` is the number of hours, `{b}` is
the number of minutes, `{c}` is the number of seconds and `{d}` is the number of hundreds of seconds. For example:
`print(StopWatch(12313.327)` should print `3H:25m:13s:33` (note that `a, b, c, d` are all integers).

**Hints**:
 * Use `time.time()` to get the number of seconds elapsed since the epoch (1 January 1970).
 * Use `time.sleep(t)`, to sleep (do nothing) for `t` seconds when testing your code.

You should not use any other functions found in the `time`, `datetime` or `calendar`
modules other than the ones listed in the hints above.

### Example

Belows is some code you can use to test your code. The expected result from running this code is shown after the test code block.

#### Test code

```python
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
```

#### Expected results

```
Creating watch at 5.22 seconds
0H:0m:5s:21
Starting watch and waiting 1 second
0H:0m:6s:22
Waiting one more second
0H:0m:7s:22
Stopping and waiting 1 second, watch is the same
0H:0m:7s:22
Starting watch again and waiting 1 second
0H:0m:8s:22
Resetting watch
0H:0m:0s:0
Starting and waiting 1 second
0H:0m:1s:0

Pretty print a watch:
3H:25m:13s:33

equals and <:
True
True

StopWatchException: cannot stop a stop watch already stopped

StopWatchException: cannot start a stop watch already running
```