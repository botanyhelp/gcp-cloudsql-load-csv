import json
import datetime
path = "click-analytics_20240910_tenDays_5000recs.txt"
#path = "click-analytics_20240910_tenDays_5000recs_5000lines_listBracketsRemoved.txt"
#path = "click-analytics_20240910_tenDays_5000recs_5000lines_listBracketsAndEndingCommasRemoved.txt"

def check_nested_key(d, key):
    if d:
        if key in d:
            return True
        for value in d.values():
            if isinstance(value, dict):
                if check_nested_key(value, key):
                    return True
    return False

with open(path, mode='r') as f:
    data = json.load(f)
dayCountsDict = {
        "0":0,
        "1":0,
        "2":0,
        "3":0,
        "4":0,
        "5":0,
        "6":0,
        "7":0,
        "8":0,
        "9":0,
        "10":0,
        }
osList = []
componentList = []
pageList = []
browserList = []
usernameList = []
for item in data:
    #if item["insertId"] == 'l9e30czt7nnjv43y':
    jsonPayload = item.get("jsonPayload")
    if jsonPayload is not None:
        timestamp = jsonPayload.get("timestamp")
        if timestamp is not None:
            dt = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
            dayCountsDict[str(dt.day)] += 1
            #print(f"{dt.day}")
    if(check_nested_key(jsonPayload, "os")):
        #print(f'{item["jsonPayload"]["message"]["metaData"]["os"]}')
        osList.append(item["jsonPayload"]["message"]["metaData"]["os"])
    if(check_nested_key(jsonPayload, "component")):
        componentList.append(item["jsonPayload"]["message"]["payload"]["component"])
    if(check_nested_key(jsonPayload, "page")):
        pageList.append(item["jsonPayload"]["message"]["metaData"]["page"])
    if(check_nested_key(jsonPayload, "browserName")):
        browserList.append(item["jsonPayload"]["message"]["metaData"]["browser"]["browserName"])
    if(check_nested_key(jsonPayload, "username")):
        usernameList.append(item["jsonPayload"]["username"])

for day in dayCountsDict.keys():
    print(f"September {day} had {dayCountsDict[day]} hits")

osSet = set(osList)
print(f"\nThe operating system visits included: {osSet}\n")
for os in osSet:
    print(f"{os} total count: {osList.count(os)}")

componentSet = set(componentList)
print(f"\nThe component visits included: {componentSet}\n")
for component in componentSet:
    print(f"{component} total count: {componentList.count(component)}")

pageSet = set(pageList)
print(f"\nThe page visits included: {pageSet}\n")
for page in pageSet:
    print(f"{page} total count: {pageList.count(page)}")

browserSet = set(browserList)
print(f"\nThe browser visits included: {browserSet}\n")
for browser in browserSet:
    print(f"{browser} total count: {browserList.count(browser)}")

usernameSet = set(usernameList)
print(f"\nThe username visits included: {usernameSet}\n")
for username in usernameSet:
    print(f"{username} total count: {usernameList.count(username)}")

