import steps

print "in first metrics..."
def report_load():
  return "servers.localhost.cpu_load 0.34"
steps.define_step("My First Step", report_load)

def report_swap_used():
  return "servers.localhost.swap_used 344"
steps.define_step("another step", report_swap_used)
