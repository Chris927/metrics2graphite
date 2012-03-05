
# mapping names to blocks/closures: each block is expected to
# return a string consisting of a graphite identifier followed by its current value
# after importing this, the define_step() method is used to add a new name/block mapping
# TODO: why is it called 'steps', exactly?
steps = {}

def define_step(name, block):
  steps[name] = block
  print "defining step with name: {}, total # of steps is {}".format(name, len(steps))

