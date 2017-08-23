#!/usr/bin/env python
from __future__ import absolute_import, print_function
import os
import pymysql.cursors
from time import sleep
import json


def main():
    # Connect to the database
    connection = pymysql.connect(host='127.0.0.1',port=10001,
                     user='root',
                     password='passwd',
                     db='twee',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            # sql = """INSERT INTO `twwees`
            # (`twee_id`, `id_str`, `text`, `source`, `user`, `retweet_count`, `favorite_count`, `lang`)
            # VALUES (%d, %s, %s, %s, %s, %d, %d, %s)"""
            sql = """INSERT INTO twees
            (twee_id, id_str, text, source, user,lang)
            VALUES (1,'1','1','1','YI','en')"""
            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":
    main()
