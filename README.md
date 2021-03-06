# SeeBus
SeeBus is a web application for viewing real time information about the Texas State Shuttle buses.


## Using SeeBus
*This tutorial is for a linux environment and assumes you already have Python 3, pip and (if you wish) a means of creating virtual environments installed on your machine. If you do not, [this tutorial](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) can help*


### Our Website
To see our website, navigate to [seebus.net](https://seebus.net) and accept any warnings about site security (our site is safe, but the HTTPS certificate is not recognized because we did not pay for it).

To see information about us, click the [about](https://seebus.net/about.html) button on the sidebar.

To see the live list of buses, click the [data](https://data.seebus.net) button on the sidebar. We did not have time for formatting or cleaning of the table. All of the information we have calculated on the buses is displayed.


### Frontend Code
To see the live list of buses locally, run
```bash
python frontend/see_bus.py
```
And navigate to [localhost:5000](localhost:5000) in your browser.
*Note: the links on the sidebar of the locally hosted website will take you to our remotely hosted website, not to locally hosted versions of the files.*


### Backend Code
Clone the repository to your machine and navigate to the root directory of our project.
```bash
git clone https://github.com/CS3398-Luna-Sea/SeeBus && cd SeeBus
```

Install all the necessary python packages (it is recommended that you do so in a virtual environment).
```bash
pip install -r requirements.txt
```

To poll the DoubleMap API for bus ETAs (not yet implemented in our website), run
```bash
python backend/poll_api.py
```

To see raw information from the DoubleMap API of currently active buses in the command line, run
```bash
python backend/bus_tracker.py
```

## Final Retrospective
### Features / Accomplishments by Team Member
* Zach
    * Wrote classes:
        * [`Bus`](backend/bus.py) - manages information about a single bus (id, location, heading, speed, etc)
        * [`BusTracker`](backend/bus_tracker.py) - periodically polls the DoubleMap API to maintain a list of `Bus` objects as well as calculate their speeds and other valuable information.
        * [`DisplayCommandLine`](backend/monitor_cl.py) - uses a `BusTracker` object to display information about the buses in the command line in real time.
        * [`Saver`](backend/saver.py) - constantly runs in the background on our server and collects arrival and departure times in JSON format when each bus makes a stop.
        * [`TestBus`](test/test_bus.py) - contains unit tests for the [`Bus`](backend/bus.py) class.
        * [`TestPollAPI`](test/test_poll_api.py) - contains unit tests for functions I wrote in [`poll_api.py`](backend/poll_api.py).
    * Wrote files:
        * [`translate.py`](backend/translate.py) - translates stop and route IDs from the DoubleMap API into useful information such as route/stop name, route type, and route number.
        * [`see_bus.py`](frontend/see_bus.py) - a Flask app that serves a dynamic webpage containing a table of information about currently active buses in real time.
        * [`buses.html`](frontend/templates/buses.html) - the template for table of buses used by the Flask app.
        * [`index.html`](frontend/templates/index.html) - the template used for the main page of the Flask app when it runs locally.
    * Wrote functions:
        * [`poll_api.get_buses()`](backend/poll_api.py) - polls the DoubleMap API for currently active buses.
        * [`poll_api.get_buses_on_route()`](backend/poll_api.py) - polls the DoubleMap API for currently active buses and returns those on a specified route.
* Chris
    * Set up server infrastructure and access
        * Set up Ubuntu AWS server that runs 24/7 hosting our website.
        * Set up server to handle incoming web requests.
        * Configured [`nginx`](misc/niginx.conf) to serve static and dynamic webpages over HTTP and HTTPS.
        * Routed our domain name [seebus.net](https://seebus.net) to our server IP [54.146.186.245](https://54.146.186.245/).
    * Coordinated frontend development.
        * Created [`landing page`](index.html) page with a dynamic GoogleMap, the main page of our website.
        * Created [`about page`](frontend/about.html) with information about us, the developers.
        * Integrated output from [`see_bus.py`](frontend/see_bus.py) to [`data page`](index.html).
* Miguel
    * Wrote code in [`Saver`](backend/saver.py) to allow for saving bus data in a database.
    * Added functions in [`poll_api.py`](backend/poll_api.py):
        * [`get_stops()`](backend/poll_api.py) - polls the DoubleMap API for a list of stops currently serviced by Texas State.
        * [`get_routes()`](backend/poll_api.py) - polls the DoubleMap API for a list of routes currently ran by Texas State.
        * [`eta()`](backend/poll_api.py) - polls the DoubleMap API for an estimated time of arrival for a given stop on a given route.
        * [`select_location()`](backend/poll_api.py) - prompts the user to choose a stop when [`poll_api.py`](backend/poll_api.py) is used in the command line.
        * [`find_route()`](backend/poll_api.py) - finds the route with a corresponding begin and finish stop entered by the user.
    * Wrote [`routeCalculator.py`](backend/routeCalculator.py) class.


### Measurable Improvements from Sprint 2
* *Chris: I need to get better with github commands. I was pushing directly to the master branch at a few points, instead of checking out and pushing to the dev branch.*
    * Since last sprint, I have been much more disciplined with working in the `dev` branch instead of committing straight to master. I have also worked on tasks that others are dependent on first, in order to minimize their hold ups. 
* *Miguel: Set aside more time to work on the assignment. Communicate more effectively what I don't know and do know. In addition we could use our bi-weekly meetings to do a code review to display progress and provide feedback to team members.*
    * I focused more on getting a viable feature out during the sprint even if it didn't work 100 percent correctly.
    * I spoke more often with Chris and Zach about issues I had during my sprint
    * I met with Zach additional times to see about how to improve my code.
* *Zach: Update my teammates with my progress so they know ahead of time how their code will be interfacing with mine.*
    * Since my work in sprint 3 was mostly focused documenting/refactoring code and assisting my teammates in finishing their features, I did not have much to inform them about. However, we did communicate better as a team.


### Next Steps
* Zach
    * Fix bugs in [`Saver`](backend/saver.py) that cause it to unexpectedly crash. Should be able to constantly run in the background with no issues.
    * Explore DoubleMap API further to see what other features are possible.
    * Clean up bus table and only show relevant information.
* Chris
    * Display bus locations as pins on the GoogleMap
    * Make bus pins move in real time.
* Miguel
    * Fix query bug in [`routeCalculator.py`](backend/routeCalculator.py) that returns more buses than specified.
    * Fix exception errors that occur when using [`poll_api.eta()`](backend/poll_api.py) function with stop combinations that do not exist.
    * Display ETAs on the website.


### Retrospective Notes
What went well for the team?
* We have all learned a lot throughout the project and were good at solving problems as they came up.
* We created a minimal viable product that is semi-useful in real life situations.
* Getting a strong backend setup to poll the API and perform calculations.
* Had regular meetings throughout the semester to coordinate project tasks and prepare for the next sprint.
* Followed through on time commitments made.

What might be impeding us from performing better?
* Not knowing the number of sprints in the semester from the beginning.
* Having other homework for this class and others while working on the project.
* Change in group size. After sprint 1, we had to adjust product scope, vision, and member roles that each person would take on.

What can we do to improve?
* Communicate our progress better.
* Stay on top of our work.
* Do more research about the best way to set up a static/dynamic website that interacts with a backend and database.
Better preparing for challenges, and being more conservative in estimating task complexity.
