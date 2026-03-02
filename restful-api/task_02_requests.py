#!/usr/bin/python3
"""
This module fetches post data from an external API and either prints
the post titles or saves selected data into a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from an online API and prints their titles along with
    the HTTP status code.
    """
    try:
        r = requests.get('https://jsonplaceholder.typicode.com/posts')
        print(f"Status Code: {r.status_code}")
        r_json = r.json()
        for post in r_json:
            print(post["title"])
    except Exception:
        print("Error")


def fetch_and_save_posts():
    """
    Fetches posts from an online API and saves their id, title, and body
    into a CSV file.
    """
    try:
        r = requests.get('https://jsonplaceholder.typicode.com/posts')
        r_json = r.json()
        with open("posts.csv", "w") as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for post in r_json:
                writer.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
    except Exception:
        print("Error")
