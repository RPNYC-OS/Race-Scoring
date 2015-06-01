from tinydb import TinyDB, where

db = TinyDB('app/db/data.json')

class division(object):

    tbl = db.table('division')

    def __init__(self,name,boatlist):
        self.name = name
        self.boatlist = boatlist
        division.tbl.insert({
            'name': self.name,
            'boatlist': self.boatlist
        })

    def getDivisionBoats(name):
        div = division.tbl.get(where('name')== name)
        return div['boatlist']

class series(object):

    tbl = db.table('series')

    def __init__(self,name,racelist):
        self.name = name
        self.racelist = racelist
        series.tbl.insert({
            'name': self.name,
            'racelist': self.racelist
        })

    def getSeriesRaces(name):
        races = series.tbl.get(where('name')== name)
        return races['racelist']
