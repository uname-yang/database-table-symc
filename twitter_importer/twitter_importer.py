#!/usr/bin/env python
from __future__ import absolute_import, print_function
import os
import pymysql.cursors
from time import sleep
import json

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# List of the interested topics
KEYWORDS_LIST = []
KEYWORDS_LIST += filter(
    bool, os.environ.get('KEYWORDS_LIST', '').split(','))

#Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')

# Kafka Configurations
MYSQL_HOST_NAME = os.environ.get('MYSQL_HOST_NAME')
MYSQL_ROOT_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD')

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, tweets):
        data=json.loads(tweets)

        # Connect to the database
        connection = pymysql.connect(host=MYSQL_HOST_NAME,
                             user='root',
                             password=MYSQL_ROOT_PASSWORD,
                             db='twee',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = """INSERT INTO `twwees`
                (`twee_id`, `id_str`, `text`, `source`, `user`, `retweet_count`, `favorite_count`, `lang`)
                VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"""
                cursor.execute(sql, (data['id'],data['id_str'],data['text'],data['source'],data['user'],data['retweet_count'],data['favorite_count'],data['lang']))

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
        finally:
            connection.close()
        return True

    def on_error(self,status):
        print(status)

def main():
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)
    stream.filter(track=KEYWORDS_LIST)


if __name__ == "__main__":
    main()
