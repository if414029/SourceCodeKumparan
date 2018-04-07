# SourceCodeKumparan
REST API using Flask and SQLite
# Simple News Management Documentation

## Description
Simple News Management is a web application to manage news. The web application is built in form of REST API using flask framework (a python microframework). It consists many functions, there are:

1. Write/create an news and topic
2. Show list of news, including functionality to search by the status and topic
3. Edit/update an news and topic

## Endpoint List News

| Method | Action                     | Example                                                       |
| ------ | -------------------------- | ------------------------------------------------------------- |
| GET    | Get all news           | http://127.0.0.1:8080/newsList                                    |
| GET    | Search an news by status | http://127.0.0.1:8080/newsList/publish			      |
| GET    | Search an news by topic | http://127.0.0.1:8080/newsList/Olahraga                          |
| POST   | Write/create a new news | http://127.0.0.1:8080/news                                       |
| PUT    | Update an news          | http://0.0.0.0:8080/news-edit/1 (1 is id of the news)	      |
| DELETE | Delete an news          | http://0.0.0.0:8080/news-delete/1 (1 is id of the news)          |

## Endpoint List Topic

| Method | Action                     | Example                                                       |
| ------ | -------------------------- | ------------------------------------------------------------- |
| GET    | Get all topic           | http://127.0.0.1:8080/topics                                  |
| POST   | Write/create a new topic | http://127.0.0.1:8080/topic                                   |
| PUT    | Update an topic          | http://0.0.0.0:8080/topic-edit/1 (1 is id of the topic)   |
| DELETE | Delete an topic          | http://0.0.0.0:8080/topic-delete/1 (1 is id of the topic) |

## Tools Required
1. Python3
2. Sqlite3
3. Flask

Install the tools required first to operate the web application. To install sqlite3 run the following commands:
```
$ sudo apt-get update

$ sudo apt-get install sqlite3 libsqlite3-dev
```

## Install Guide
**Clone the repo**

Go to computer's shell and type the following command:
```
$ git clone https://github.com/if414029/SourceCodeKumparan.git

$ cd kumparan/kumparan-api
```

To operate the web application there are two dependencies required:
1. Flask
2. Flask-RESTful


Two dependencies above can install in root environment or in a virtual environment. Install dependencies in virtual environment used to separate all of the flask framework dependencies from base python dependencies (in root environment). To install virtual environment run the following commands:

**Install virtual environment dependency**
```
$ pip install virtualenv
```
**Back to home directory (in ubuntu)**
```
$ cd ~
```
**Make new directory for virtual environment**
```
$ mkdir venvs

$ python3 -m venv venvs/flaskproject
```
**Activate virtual environment**
```
$ source ~/venvs/flaskproject/bin/activate
```
**Deactivate virtual environment**
```
$ deactivate
```
If we want to install dependencies please activate the virtual environment first and then run the following commands:
```
$ pip install Flask

$ pip install Flask-RESTful

```

Before run the project, open shell in project directory (on kumparan/kumparan-api), activate the virtual environment, and then run the project. Activate virtual environment make the project can use the dependencies required. On the other hand, we can just run the three commands above if we don't want to install the dependencies in a separate virtual environment (writer use this way), so we don't need to activate any virtual environment.

**Note:**

The application is built and run in ubuntu 16.04 operating system.

## Run The Web Application
To run the web application we must create the database first and then run the app. Open shell in project directory (in kumparan/kumparan-api directory) and run the following commands:
```
$ sqlite3 kumparan.db < dbSchema.sql

$ python run_app.py
```
If the database have been installed, just run the second command.

## Test The API
If you want to test all method uncommend and commend this code one by one and run again
```
$ python run_app.py

```
	from api._01_get_topic import app
	# from api._02_post_topic import app
	# from api._03_put_topic import app
	# from api._04_delete_topic import app
	# from api._01_get_news import app
	# from api._02_post_news import app	
	# from api._03_put_news import app	
	# from api._04_delete_news import app
