# Full path and name to your csv file
csv_filepathname="/Users/alexander/Documents/Atom/CINS465-Alex-Cooksey/Tippingplate/plate/Fixture.csv"
# Full path to your django project directory
your_djangoproject_home="/Users/alexander/Documents/Atom/CINS465-Alex-Cooksey/Tippingplate/"

import sys,os
from django.shortcuts import render, HttpResponse
from django.utils.html import escape

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from plate.models import Fixture


import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'GAME': # Ignore the header row, import everything else
        fixture = Fixture()
        fixture.game_no = row[0]
        fixture.round_no = row[1]
        fixture.game_code = row[2]
        fixture.game_day = row[3]
        fixture.game_date = row[4]
        fixture.hmaw_status = row[5]
        fixture.home_team = row[6]
        fixture.ht_code = row[7]
        fixture.away_team = row[8]
        fixture.at_code = row[9]
        fixture.ground_name = row[10]
        fixture.game_time = row[11]
        fixture.time_slot = row[12]
        fixture.game_state = row[13]
        fixture.save()
