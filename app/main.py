# Title: Race Score Module
# Author: Campbell Fleury
# Date: 2015-05-11

from tinydb import TinyDB, where
import csv

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

    def importBoat(self,file):
        'Performs a purge, then an import'
        boat.tbl.purge()
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                boat.tbl.insert({
                    'name': row['Boat'],
                    'sailno': row['SailNo']
                })

class handicap(object):

    tbl = db.table('handicap')

    def __init__(self,name,club,phrf,irc):
        self.name = name
        self.club = club
        self.phrf = phrf
        self.irc = irc
        handicap.tbl.insert({
            'name': self.name,
            'club': self.club,
            'phrf': self.phrf,
            'irc': self.irc
        })

    def importHandicaps(file):
        handicap.tbl.purge()
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                handicap.tbl.insert({
                    'name': row['Boat'],
                    'club': row['Club'],
                    'phrf': row['PHRF'],
                    'irc': row['IRC']
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

    def importRace(file):
        race.tbl.purge()
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                race.tbl.insert({
                    'name': row['Race'],
                    'start': row['StartTime'],
                })

class result(object):

    tbl = db.table('result')

    def __init__(self,boat,race,time):
        self.boat = boat
        self.race = race
        self.time = time
        result.tbl.insert({
            'boat': self.boat,
            'race': self.race,
            'time': self.time
        })

    def importResults(file):
        race.tbl.purge()
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                race.tbl.insert({
                    'boat': row['Boat'],
                    'race': row['Race'],
                    'time': row['Time'],
                })
