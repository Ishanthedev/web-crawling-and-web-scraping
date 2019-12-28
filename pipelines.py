# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#import sqlite3
import pymongo
class QuotetutorialPipeline(object):
    #mongo bd process
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['myquotes']
        self.collection = db['quotes_tb']
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item



    # Down from here I have SQLITE code
    # def __init__(self):
    #     self.create_connection()
    #     self.creat_table()
    # def create_connection(self):
    #     self.conn = sqlite3.connect("myquotes.db")
    #     self.curr = self.conn.cursor()
    # def creat_table(self):
    #     self.curr.execute("""DROP TABLE  IF EXISTS quotes_tb""")
    #     self.curr.execute("""create table quotes_tb(
    #                     title text,
    #                     author text,
    #                     tag text)""")
    #
    # def process_item(self, item, spider):
    #     self.store_db(item)
    #     print("pipeline :" + item['title'][0])
    #     return item
    # def store_db(self,item):
    #     self.curr.execute("""insert into quotes_tb values(?,?,?) """,(
    #         item['title'][0],
    #         item['author'][0],
    #         item['tag'][0]
    #     ))
    #     self.conn.commit()
