#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re
import datetime
import sqlite3
import time
import smtplib
from email.message import EmailMessage

SENDER_ADDRESS = "benji.xiao@gmail.com"
SENDER_PASSWORD = "oEp-pQD-X1K-mhl"
RECEIVER_ADDRESS = "ben.xiao@me.com"

DATE_PATTERN = re.compile(".*/(\d{4})/(\d{2})/(\d{2}).*")
TITLE_PATTERN = re.compile(".*/([^/]+).html")
HOME = "https://www.nytimes.com"

# TABLE_CREATION = '''create table stories (
#       title text,
#       url text unique,
#       content text
# )
# '''


class Story:
    def __init__(self):
        self.title = None
        self.url = None
        self.content = None

    def set_content(self):
        def _inline_callback(soup):
            content_html = soup.find_all("p", attrs={"class": "story-content"})
            content = []
            for c in content_html:
                try:
                    content.append(c.text)
                except:
                    pass
            return "".join(content)

        self.content = fetch_soup(self.url, _inline_callback)


def top_stories_callback(soup):
    top_stories_section = soup.find("section", attrs={"class": "top-news"})
    return top_stories_section.find_all("h2", attrs={"class": ["story-heading", "story-sub-heading"]})

def notification_send(subject, text):
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = subject
    msg['From'] = SENDER_ADDRESS
    msg['To'] = RECEIVER_ADDRESS
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(SENDER_ADDRESS, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
    except:
        pass

def get_today_string():
    today = datetime.datetime.today()
    day_string = str(today.day)
    if today.day < 10:
        day_string = f"0{day_string}"
    month_string = str(today.month)
    if today.month < 10:
        month_string = f"0{month_string}"
    today_string = f"/{today.year}/{month_string}/{day_string}/"
    return today_string


def get_stories():
    stories = []
    top_stories = fetch_soup(HOME, top_stories_callback)
    if top_stories:
        for story in top_stories:
            try:
                url = story.a.get("href")
            except:
                continue
            found_title = re.search(TITLE_PATTERN, url)
            found_date = re.search(DATE_PATTERN, url)
            if found_date and found_title:  # and today_string in url:
                title = found_title.group(1)
                s = Story()
                s.title = title
                s.url = url
                stories.append(s)
    return stories


def fetch_soup(url, callback):
    num = 5
    while 1:
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                break
            else:
                continue
        except Exception:
            if num > 0:
                time.sleep(1)
                num -= 1
                continue
            else:
                return None

    if resp.status_code == 200:
        content = resp.content
        soup = BeautifulSoup(content, features='html.parser')
        return callback(soup)
    return None


def report(new_titles):
    lines = []
    lines.append(str(datetime.datetime.now()))
    lines.extend(new_titles)
    notification_send("nytimes_cron", "\n".join(lines))


def main():
    stories = get_stories()
    for s in stories:
        print(s.url)
    print("num:", len(stories))
    for s in stories:
        s.set_content()

    stories = [s for s in stories if s.content]

    with sqlite3.connect("/home/ranxiao/PycharmProjects/untitled/nytimes.db") as conn:
        cursor = conn.cursor()
        story_tuples = [(s.title, s.url, s.content) for s in stories]
        new_titles = []
        for row in story_tuples:
            try:
                cursor.execute('INSERT INTO stories VALUES (?,?,?)', row)
                new_titles.append(row[0])
            except sqlite3.IntegrityError:
                pass
        report(new_titles)

main()
