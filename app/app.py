import main as m
from tinydb import TinyDB, where

# m.race('Winter One','13:15:00')
# m.race.tbl.purge()
# m.result.tbl.purge()

# m.result('Helter Skelter', 'Winter One', '14:02:32')
# m.result('Wedgetail', 'Winter One', '14:14:05')
# m.result('Airship', 'Winter One', '14:57:2')


race = 'Winter One'

json = m.result.getRaceResults(race)
start = m.race.getStartTime(race)
fmt = '%H:%M:%S'
for i in range(0,len(json)):
    boattime = json[i]['time']
    boatname = json[i]['boat']
    correction = m.handicap.getCorrection(boatname, 'club')
