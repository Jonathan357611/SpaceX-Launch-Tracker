# Importing all Libraries I used for this Project:
from PIL import Image, ImageDraw, ImageFont
import os
import scrape_api as api  # Importing our file "scrape_api.py" as "api"
from datetime import datetime
import calendar
import ast
import time
import epd2in13b_v3 as epd2in13b_v3
from epd2in13b_v3 import *
import re
from datetime import timedelta


MINUTES = 15  # Define The amount of time to wait in the loop


display = epd2in13b_v3.EPD()  # Defining "display"

display.init()  # Initializing and Clearing the display [epd2in13b_v3.EPD()]
display.Clear()

def calculate_percentage(start, current, end, image_x=50):    # This is a function which will calcute how many Pixels of the X need to be red
    x = (current - start) / (end - start)
    return int(round(image_x/100*x*100))

while True:
    api.load_site() # This will load all 3 API endpoints

    ### GETTING DATA ###
    mission_name = api.next_launch("name")    # This Gets the name of the Next mission
    launch_time = api.next_launch("date_unix")   # And this will scrape the time of the launch in Unix Time
    unix_time_last_launch = api.latest_launch("date_unix")   # Gives the Unix Time of the last launch
    flight_number = api.next_launch("flight_number")   # The number of the launch
    next_launch = api.get_more_launches("name", 1)  # will return The launch after the next launch
    ###             ###

    current_date = datetime.utcnow()
    unixtime = calendar.timegm(current_date.utctimetuple())  # Saving the current Unix Time

    UNIX_START = unix_time_last_launch
    UNIX_NOW = unixtime                         # Defining the 3 important Unix-Timestamps (last flight, current time, next flight)
    UNIX_STOP = launch_time


    font_9 = ImageFont.truetype(os.path.join("font.ttf"), size=9)   # Creating multiple font-sizes using the Pillow (PIL) module
    font_8 = ImageFont.truetype(os.path.join("font.ttf"), size=8)
    font_7 = ImageFont.truetype(os.path.join("font.ttf"), size=7)
    font_10 = ImageFont.truetype(os.path.join("font.ttf"), size=10)
    font = ImageFont.truetype(os.path.join("font.ttf"), size=15)


    try:                                                    # Converting Unix Time in a readable format
        time_left = int(launch_time) - int(unixtime)
        if time_left > 86400:
            time_text = f"{round(time_left / 86400)} Days"
        elif time_left > 3600:
            time_text = f"{round(time_left / 3600)} Hours"
        elif time_left > 60:
            time_text = f"{round(time_left / 60)} Minutes"
        else:
            time_text = f"{time_left} Seconds! "
    except:
        time_text = "error"


    white_spaces = " " * (10 - len(time_text))     # Adding whitespaces in front of the Text so that the text is on the left side
    time_text = f"{white_spaces}{time_text}"


    w = display.height  # Receiving Display High/Width
    h = display.width

    red_image = Image.new(mode="1", size=(212, 104), color=255)  # Creating two images
    red_draw = ImageDraw.Draw(red_image)
    image = Image.new(mode="1", size=(212, 104), color=255)
    draw = ImageDraw.Draw(image)

    ### THIS PART IS OPTIONAL ###
    next_mission_name = re.sub("\([^>]+\)", "", mission_name)      # I had a problem Displaying "(" and ")" on the display, so I will filter them out using some basic RegEX
    if next_mission_name[-1] == " ":                                    # You can delete this part if you want!
        next_mission_name = next_mission_name[:-1]

    _2_launch = re.sub("\([^>]+\)", "", next_launch)
    if _2_launch[-1] == " ":
        _2_launch = _2_launch[:-1]
    ###                      ###


    core = api.next_launch("cores")  # Parsing a Dictionary with important data from the SpaceX api
    core = str(core[-1:])      # Removing a '"' from the beginning and end of the String
    core = str(core[1:][:-1])
    core_dict = ast.literal_eval(core)  # Converting the Parsed string to Python Dictionary (Not the most Pythonic way!)

    t = time.localtime()                              # Receiving the time in the Hour:Minute:Second Format
    current_time = time.strftime("%H:%M:%S", t)

    draw.text((167, 0), f"N. {flight_number}", 0, font_10)    # Drawing the flight number on the Black Image
    red_draw.text((209 - len(next_mission_name) * 5, 30), next_mission_name, 0, font, align="left", anchor="md") # Drawing Mission-name on Red image
    draw.text((172, 45), f"{time_text}", 0, font_10, anchor="md")   # Drawing the time on the black Image
    draw.text((0, 0), str(current_time), 0, font_10)  # Drawing the current time in the upper right corner so we can see if the display updated.

    if core_dict["landing_attempt"] == True:
        draw.text((5, 62), f"Landing: Yes", 0, font_9)  # If the Rocket attemts to land
    else:
        red_draw.text((5, 62), f"Landing: No", 0, font_9) # If the Rocket won't land, the Text will get displayed in red!

    if core_dict["reused"] == True:
        draw.text((5, 72), f"Reused: Yes", 0, font_9)  # If the Booster is reused
    else:
        red_draw.text((5, 72), f"Reused: No", 0, font_9)

    draw.text((5, 82), f"Next: {_2_launch}", 0, font_9)  # And this will draw the next launch on the Image


    full_spacex_x = Image.open("spacex.png")  # Here we open/load the SpaceX logo (You can Download this Image in my GitHub Repo.)
    full_spacex_x_redpart = full_spacex_x.crop((0, 0, calculate_percentage(UNIX_START, UNIX_NOW, UNIX_STOP), 24))   # Crops the SpaceX logo using the "calculate_percentage" function

    image.paste(full_spacex_x, (156, 69))
    red_image.paste(full_spacex_x_redpart, (156, 69))  # This fills the cropped part with red

    display.Clear() # Clearing the display

    display.display_black(display.getbuffer(image=image))  # Finaly draws the Black image on the E-Paper display
    display.display_red(display.getbuffer(image=red_image)) # And the same with the red image!
    display.sleep()  # Putting the display in sleep mode to reduce the power!
    time.sleep(MINUTES * 60) # Waits n Minutes