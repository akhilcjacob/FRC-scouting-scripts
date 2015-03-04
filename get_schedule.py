import json
import urllib2
import sys
from pprint import pprint

event = raw_input('Enter the event: ').lower() #normally will be nyro
year = raw_input('Enter the year: ')
url = "http://www.thebluealliance.com/api/v2/event/" + year+"%s/matches" % (event)

req = urllib2.Request(url, headers={"X-TBA-App-Id": "frc2791:scoutingSystem:v01"}) # b/c the API requires some stoopid HTTP headers

jsonData = json.loads(urllib2.urlopen(req).read())

def compMatches(a, b):
    if a["match_number"] == b["match_number"]:
        return 0
    else:
        return 1 if a["match_number"] > b["match_number"] else -1

matches = sorted([{"match_number":match["match_number"], "alliances":match["alliances"]} for match in jsonData if match["comp_level"] == u"qm"], cmp=compMatches)

total=''
fileName=event+"-Schedule.txt"
fileOpen = open(fileName,"w")

for match in matches:
    total=total+str(match["match_number"])+","+str(match["alliances"]["blue"]["teams"][0][3:])+","+str(match["alliances"]["blue"]["teams"][1][3:])+","+ str(match["alliances"]["blue"]["teams"][2][3:])+","+str(match["alliances"]["red"]["teams"][0][3:]) +","+str(match["alliances"]["red"]["teams"][1][3:])+","+str( match["alliances"]["red"]["teams"][2][3:])+"\n"

print total
fileOpen.write(str(total))
fileOpen.close()
