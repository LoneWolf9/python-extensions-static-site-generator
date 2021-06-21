import time

from ssg import hooks

start_time = None
total_written = 0


@hook.event("start_build")
def start_build():
    global start_time
    start_time.gmtime()
