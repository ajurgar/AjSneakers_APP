# AjSneakers_APP

AJsneakers-Tracker

1. AJsneakers application allows the user to track their inventory and manufacturers. 
Includes functionality to view, edit, delete and add new products/manufacturers to the tracker. 

2. Tests results: ![](https://img.shields.io/badge/Ran%2012%20tests%20in%200.000s-12%20passed%2C%200%20failed-green)

3. The technologies used are Python, SQL, Flask, HTML and CSS.

Usage:

1) Create the database, run command:
createdb stock_manager 

2) Create the tables in the database, run command:
psql -d stock_manager -f db/stock_manager.sql

3) Pass the data from console, run command:
python3 console.py

4) Run Flask server, run command:
flask run

5) Check http port location on terminal:
* Running on http://127.0.0.1:4999 (Press CTRL+C to quit)

6) Visit http://localhost:4999/ on Chrome browser to run application.



Support:

For addtional support and queries contact --- ajsneakers@outlook.com

Roadmap:

- Add functionality to add more sizes for each pair. Show different selling prices and markups for them.
- Add shipping cost and net profit to the tracker.
- Add selling platform for additional information.


I would like to acknowledge Ally McGilloway, Ashley Healy, Ben Roberts, Juan Molero and Harpreet Dhanda for their support.

This project is an open source project which contributions are welcome.
