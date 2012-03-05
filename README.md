# metrics2graphite

Small script / service in Python to enable reading
metrics from an application (using Coda Hale's metrics principles)
and writing the results to a graphite server.

Important: If the source of the metrics is a JVM, this approach is *unnecessary*, as Coda Hale's metrics
library has built-in support to push to a Graphite server, see http://metrics.codahale.com/manual/graphite/.
Unfortunately, I haven't found anything similar when the metrics source is a .NET or Ruby process.

Also important: These script are not finished! Please check the various TODOs.

## Little Overview

* metrics2graphite.py
  * contains the thread that would run forever and report every metric ("step") registered every minute.
* steps.py
  * mini-DSL to register a "step". Python scripts that implement reading metrics from the process would
  import this and register one or more "steps".
* FirstMetrics.py
  * This is an example on how metrics would be implemented. See the TODOs in there and in metrics2graphite.py
  how this should *actually* be implemented... or any better ideas?
