import steps
import subprocess
import re

def report_load():
  pattern = re.compile(r"\d+\.\d+") # find the first occurence of a number of the form '3.76'
  # the output of 'uptime' typically looks like this:
  # '15:07  up 8 days,  3:16, 13 users, load averages: 0.43 0.52 0.49'
  # and we take the first number of the described format
  load_value = pattern.search(subprocess.check_output("uptime")).group()
  # TODO: hard coded graphite id ahead
  return "servers.dummy.cpu_load {}".format(load_value)
steps.define_step("Dummy CPU Load", report_load)

def report_swap_used():
  # This is really just a dummy...
  return "servers.dummy.swap_used 344"
steps.define_step("another step", report_swap_used)
