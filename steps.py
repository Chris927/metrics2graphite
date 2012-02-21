
steps = {}

def define_step(name, block):
  steps[name] = block
  print "defining step with name: {}, total # of steps is {}".format(name, len(steps))

