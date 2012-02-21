#!/usr/bin/env python
import time
import thread
from steps import steps

# TODO: idea is to load multiple files here (e.g. all in a configured dir)
X = __import__( "FirstMetrics" )

class timed:
  def __init__(self):
    thread.start_new(self.do_something, tuple())
    while True:
      time.sleep(1)

  def do_something(self):
    while True:
      # TODO: push metrics to graphite here...
      for name, function in steps.iteritems():
        print "now should push metric: {}".format(name)
      print "metrics pushed to graphite, #steps is {}".format(len(steps))
      time.sleep(1)

if __name__ == "__main__":
  print "starting thread"
  timed()

