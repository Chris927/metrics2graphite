#!/usr/bin/env python
import time
import thread

class timed:
  def __init__(self):
    thread.start_new(self.do_something, tuple())
    while True:
      time.sleep(1)
    
  def do_something(self):
    while True:
      # TODO: push metrics to graphite here...
      print "metrics pushed to graphite"
      time.sleep(1)

if __name__ == "__main__":
  print "starting thread"
  timed()

