>> grep pid by filename
    ps aux | grep python.py

>> to find the PID directly:
    pgrep -f watch.py


>> pgrep -f watchdog.py
# Assume it returns 12345
>> kill -9 12345


# Or, in one line using pgrep
kill -9 $(pgrep -f watchdog.py)

