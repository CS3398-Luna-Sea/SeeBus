# SeeBus

## Steps to Run
All of the backend python code can be downloaded and ran (with the appropriate modules installed).

You can go to our website by visiting the IP directly [`http://35.168.221.32`](http://35.168.221.32).

## Current Status
Currently, 2 classes, [`Bus.py`](Bus.py) and [`BusTracker.py`](BusTracker.py) successfully poll the API and show information.

`Bus` objects hold information about buses, and `BusTracker` has a list of buses, polls the API to update it, and
displays the information every 3 seconds.

All code can be downloaded and ran to show the output described above. In the future, this output will be manipulated
and formatted to display all desired information in a nice presentable manner.

[`poll_api.py`](poll_api.py) contains functions to request various inforamtion from the DoubleMap API. These functions
are used by `BusTracker`.

[`infrastructure_notes.txt`](infrastructure_notes.txt) contains the IP of our remote server.

## Next Steps
* Zach
  * Implement speed calculation
  * Make bus info display in nice format in command line
* Chris
  * Get example webpage up and running with domain name
  * Figure out infrastructure (Gradle, TravisCI)
  * Experiment with map APIs
* Miguel
  * Get example database up and running
  * Begin saving bus data into database for use in statistics calculations later
