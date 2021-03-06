import requests
import time
def load_site():
    global site_latest, site_next, site_upcoming

    site_latest = None
    site_next = None
    site_upcoming = None

    try:
        site_latest = requests.get("https://api.spacexdata.com/v4/launches/latest")
        site_next = requests.get("https://api.spacexdata.com/v4/launches/next")
        site_upcoming = requests.get("https://api.spacexdata.com/v4/launches/upcoming")
        did_work = True
    except Exception as e:
        print(e)
        did_work = False
    while did_work == False:
        try:
            while site_latest == "None" or site_latest == None or site_next == "None" or site_next == None or site_upcoming == "None" or site_upcoming == None:
                site_latest = requests.get("https://api.spacexdata.com/v4/launches/latest")
                site_next = requests.get("https://api.spacexdata.com/v4/launches/next")
                site_upcoming = requests.get("https://api.spacexdata.com/v4/launches/upcoming")
                print("ERROR OCCURED")
            did_work = True
        except:
            print("ERROR OCCURED")
            time.sleep(60)
            did_work = False
    site_latest = site_latest.json()
    site_next = site_next.json()
    site_upcoming = site_upcoming.json()

def latest_launch(info_to_get="name"):
    global site_latest, site_next, site_upcoming
    return site_latest[info_to_get]
def next_launch(info_to_get="details"):
    global site_latest, site_next, site_upcoming
    return site_next[info_to_get]
def next_launch_core(info_to_get="gridfins"):
    global site_latest, site_next, site_upcoming
    return site_next["cores"][info_to_get]
def get_more_launches(info_to_get="name", number=1):
    global site_latest, site_next, site_upcoming
    return site_upcoming[number][info_to_get]