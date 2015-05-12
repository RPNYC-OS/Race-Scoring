# Title: Race Score Module
# Author: Campbell Fleury
# Date: 2015-05-11
from tinydb import TinyDB, where

db = TinyDB('app/db/data.json')

class boat(object):

    tbl = db.table('boat')

    def __init__(self,name,sailno):
        self.name = name
        self.sailno = sailno
        boat.tbl.insert({
            'name': self.name,
            'sailno': self.sailno
            })

class handicap(object):

    tbl = db.table('handicap')

    def __init__(self,name,type,value):
        self.name = name
        self.type = type
        self.value = value
        handicap.tbl.insert({
            'name': self.name,
            'type': self.type,
            'value': self.value
            })

class race(object):

    tbl = db.table('race')

    def __init__(self,name,start):
        self.name = name
        self.start = start
        race.tbl.insert({
            'name': self.name,
            'start': self.start
        })

class result(object):

    tbl = db.table('result')

    def __init__(self,name,time):
        self.name = name
        self.time = time
        result.tbl.insert({
            'name': self.name,
            'time': self.time
        })
