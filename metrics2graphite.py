#!/usr/bin/env python
import time
import thread
import subprocess
import socket
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
        id_and_value = function()
        msg = "{} {}".format(id_and_value, subprocess.check_output([ "date", r"+%s" ]))
        print "now should push metric: {}, msg={}".format(name, msg)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TODO: could have one socket open while sending all metrics?
        s.connect(('localhost', 10003))
        s.sendall(msg)
        s.close()
      time.sleep(10)

if __name__ == "__main__":
  print "starting thread"
  timed()

