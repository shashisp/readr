# Readr

Read Hackernews articles in your dashboard

## Features

- Store reading logs.
- Mark as read to archive
- Delete unwanted articles

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install requirements (`$ pip install -r requirements.txt`)
3. `python manage.py migrate`
4. `python manage.py runserver`


## Populate Top news articles from hackernews

    $ python manage.py populate_news
    
    using HackerNews API for populating https://github.com/HackerNews/API


#ToDo
- Add proper validation for registration form.
- Add sidebar filters, to filter based on article status

<img src="rss.png">
