# Movie Management System

## Table of Contents
- [Summary](#summary)
- [Important Files and Specification](#important-files-and-specification)
- [Installation](#installation)
- [Video Demo](#video-demonstration)

## Summary
A video game rental management system, developed in Python using Matplotlib for visualisations on Jupyter Notebook. The system enables a store manager to manage video game rentals based on customer subscriptions. The manager can also check the availability of video games, rent them out to customersd and a maintain a database of all video games in the inventory.


## Important Files and Specification
1. Game_Info.txt, Rental.txt -> Stores data for video game details and rental history of video games, respectively
2. gameSearch.py -> Python module containing functions allowing the manager to input search terms and strings and return the output
3. gameReturn.py -> Python module containing functions that promt the store manager for the ID of the game(s) they wish to return and collect feedback if they want
4. InventoryPruning.py -> Python module containing functions used to identify games for potential removal based on rental frequency for example. Offers visualisations.
5. database.py -> contains common functions used by all modules
6. menu.ipynb -> GUI menu program that provides the required menu options to the store manager. The GUI was required to only use one window.
7. subscriptionManager.pyc, feedbackManager.pyc -> provided modules to manage customer subscriptions and collect feedback, respectively


## Installation
Ensure that you have Java installed on your local computer. You check by running the following command in Terminal: ```java -version```

To install and run this Python project, follow the instructions below:
1. **Clone this repository or download the ZIP file**:
   ```bash
   git clone https://github.com/Jeev28/Movie-Management-System.git
   
2. **Set up a virtual environment (optional)**:
   It is not required, but set a virtual environment to provide isolation from any current    Python projects you have locally.
   ```bash
   python3 -m venv env
   source env/bin/activate  # On macOS/Linux
   env\Scripts\activate     # On Windows
  
3. **Install Dependencies**:
   Execute: ``` pip install jupyter matplotlib ipywidgets ```

4. **Open in Jupyter Notebook**:
   Execute: ``` jupyter notebook ```
   Navigate to the directory where you cloned this and open the ```.ipynb``` file

## Video Demonstration
COMING SOON...
