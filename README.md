# SeeBus

## Steps to Run Backend Code
*This tutorial assumes you already have pip and (if you wish) a means of creating virtual environments installed on your machine. If you do not, this tutorial can help*

Clone the repository to your machine and navigate to the root directory of our project.
```bash
git clone https://github.com/CS3398-Luna-Sea/SeeBus && cd SeeBus
```

Install all the necessary python packages (it is recommended that you do so in a virtual environment).
```bash
pip install -r requirements.txt
```

To see a table of all the currently active buses shown in the command line, run the BusTracker class.
```bash
python backend/monitor_cl.py
```

To see a simple locally hosted web page of all the currently active buses, run the Flask application.
```bash
python frontend/see_bus.py
```
Then navigate to [`localhost:5000`](localhost:5000).

## Steps to see frontend
Navigate to [`54.146.186.245`](http://54.146.186.245).
Soon, our domain name SeeBus.net will be connected to the IP.


## Next Steps
* Zach
    * Research how to integrate the Flask app with our server.
    * Assist Chris and Miguel in tying together all the individual pieces of our project.
    * Review all code and put refactor and document it.
* Chris
    * Get Domain Name connected to server.
    * Integrate SeeBus live data stream into Frontend
    * Show live bus locations on Google Map
* Miguel
  * Get example database up and running
  * Begin saving bus data into database for use in statistics calculations later
