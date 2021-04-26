import requests
def load_site():
    global site_latest, site_next, site_upcoming
    site_latest = requests.get("https://api.spacexdata.com/v4/launches/latest").json()
    site_next = requests.get("https://api.spacexdata.com/v4/launches/next").json()
    site_upcoming = requests.get("https://api.spacexdata.com/v4/launches/upcoming").json()

def latest_launch(info_to_get="name"):
    global site_latest, site_next, site_upcoming
    return site_latest[info_to_get]
    #return requests.get("https://api.spacexdata.com/v4/launches/latest").json()[info_to_get]
def next_launch(info_to_get="details"):
    global site_latest, site_next, site_upcoming
    return site_next[info_to_get]
    #return requests.get("https://api.spacexdata.com/v4/launches/next").json()[info_to_get]
def next_launch_core(info_to_get="gridfins"):
    global site_latest, site_next, site_upcoming
    return site_next["cores"][info_to_get]
    #return requests.get("https://api.spacexdata.com/v4/launches/next").json()["cores"]
def get_more_next(info_to_get="name", number=1):
    global site_latest, site_next, site_upcoming
    return site_upcoming[number][info_to_get]
    #space = requests.get("https://api.spacexdata.com/v4/launches/upcoming").json()
    #return space[number][info_to_get]