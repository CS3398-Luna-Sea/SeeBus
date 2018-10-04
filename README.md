# SeeBus

Currently, 2 classes, [`Bus.py`](Bus.py) and [`BusTracker.py`](BusTracker.py) successfully poll the API and show information.

`Bus` objects hold information about buses, and `BusTracker` has a list of buses, polls the API to update it, and
displays the information every 3 seconds.

All code can be downloaded and ran to show the output described above. In the future, this output will be manipulated
and formatted to display all desired information in a nice presentable manner.

[`poll_api.py`](poll_api.py) contains functions to request various inforamtion from the DoubleMap API. These functions
are used by `BusTracker`.

[`Infrastructure Notes`](infrastructure_notes.txt) contains the IP of our remote server.