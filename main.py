from PIL import Image, ImageDraw, ImageFont
import os
import SpaceP
from datetime import datetime
import calendar
from google_trans_new import google_translator
import ast
import time
import epd2in13b_v3 as epd2in13b_v3
from epd2in13b_v3 import *
import re

# display = epd2in13b_v3.EPD()
print(1)
display = epd2in13b_v3.EPD()
print(1)
display.init()
print(1)
translator = google_translator()
print(1)
display.Clear()

def calculate_percentage(start, current, end, image_x=50):
    x = (current - start) / (end - start); return int(round(image_x/100*x*100))

while True:
    SpaceP.load_site()

    next_mission_name = SpaceP.next_launch("name")
    launch_time = SpaceP.next_launch("date_unix")
    flight_number = SpaceP.next_launch("flight_number")
    mission_desc_english = SpaceP.next_launch("details")
    _2_launch = SpaceP.get_more_next("name", 1)
    unix_time_last_launch = SpaceP.latest_launch("date_unix")

    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    #unixtime = 1619582000

    UNIX_START = unix_time_last_launch
    UNIX_NOW = unixtime
    UNIX_STOP = launch_time

    core = SpaceP.next_launch("cores")
    core = str(core[-1:])
    core = core[1:][:-1]
    core_dict = ast.literal_eval(core)
    print(core_dict["flight"])

    print(mission_desc_english)

    mission_desc_german = translator.translate(mission_desc_english, lang_src="en", lang_tgt="de")

    mission_desc_german = mission_desc_german.replace("Charat", "Charge")

    print(mission_desc_german)

    print(next_mission_name)
    print(type(launch_time))
    print(flight_number)

    font_9 = ImageFont.truetype(os.path.join("font.ttf"), size=9)
    font_8 = ImageFont.truetype(os.path.join("font.ttf"), size=8)
    font_7 = ImageFont.truetype(os.path.join("font.ttf"), size=7)
    font_10 = ImageFont.truetype(os.path.join("font.ttf"), size=10)
    font = ImageFont.truetype(os.path.join("font.ttf"), size=15)



    print(int(launch_time) - unixtime)

    time_left = int(launch_time) - unixtime


    if time_left > 86400 * 10:           # Please do not post my code on r/badcode :( But I would love some tips how to clean this weird code!
        time_text = "    10 Days"
    elif time_left > 86400 * 9:
        time_text = "     9 Days"
    elif time_left > 86400 * 8:
        time_text = "     8 Days"
    elif time_left > 86400 * 7:
        time_text = "     7 Days"
    elif time_left > 86400 * 6:
        time_text = "     6 Days"
    elif time_left > 86400 * 5:
        time_text = "     5 Days"
    elif time_left > 86400 * 4:
        time_text = "     4 Days"
    elif time_left > 86400 * 3:
        time_text = "     3 Days"
    elif time_left > 86400 * 2:
        time_text = "     2 Days"
    elif time_left > 86400:
        time_text = "      1 Day"
    elif time_left > 3600 * 23:
        time_text = "   23 Hours"
    elif time_left > 3600 * 22:
        time_text = "   22 Hours"
    elif time_left > 3600 * 21:
        time_text = "   21 Hours"
    elif time_left > 3600 * 20:
        time_text = "   20 Hours"
    elif time_left > 3600 * 19:
        time_text = "   19 Hours"
    elif time_left > 3600 * 18:
        time_text = "   18 Hours"
    elif time_left > 3600 * 17:
        time_text = "   17 Hours"
    elif time_left > 3600 * 16:
        time_text = "   16 Hours"
    elif time_left > 3600 * 15:
        time_text = "   15 Hours"
    elif time_left > 3600 * 14:
        time_text = "   14 Hours"
    elif time_left > 3600 * 13:
        time_text = "   13 Hours"
    elif time_left > 3600 * 12:
        time_text = "   12 Hours"
    elif time_left > 3600 * 11:
        time_text = "   11 Hours"
    elif time_left > 3600 * 10:
        time_text = "   10 Hours"
    elif time_left > 3600 * 9:
        time_text = "    9 Hours"
    elif time_left > 3600 * 8:
        time_text = "    8 Hours"
    elif time_left > 3600 * 7:
        time_text = "    7 Hours"
    elif time_left > 3600 * 6:
        time_text = "    6 Hours"
    elif time_left > 3600 * 5:
        time_text = "    5 Hours"
    elif time_left > 3600 * 4:
        time_text = "    4 Hours"
    elif time_left > 3600 * 3:
        time_text = "    3 Hours"
    elif time_left > 3600 * 2:
        time_text = "    2 Hours"
    elif time_left > 3600:
        time_text = "    1 Hour"
    elif time_left > 3600 / 2:
        time_text = "30 Minutes"
    elif time_left > 3600 / 4:
        time_text = "15 Minutes"
    elif time_left > 0:
        time_text = "     Soon!"
    else:
        time_text = "error"
    print(time_text)
    # time_text = "1,5 Stunden"
    w = display.height
    h = display.width
    print(w)
    print(h)



    red_image = Image.new(mode="1", size=(212, 104), color=255)

    image = Image.new(mode="1", size=(212, 104), color=255)
    draw = ImageDraw.Draw(image)
    red_draw = ImageDraw.Draw(red_image)

    next_mission_name = re.sub("\([^>]+\)", "", next_mission_name)
    if next_mission_name[-1] == " ":
        next_mission_name = next_mission_name[:-1]

    _2_launch = re.sub("\([^>]+\)", "", _2_launch)
    if _2_launch[-1] == " ":
        _2_launch = _2_launch[:-1]

    draw.text((167, 0), f"N. {flight_number}", 0, font_10)
    red_draw.text((209 - len(next_mission_name) * 5, 30), next_mission_name, 0, font, align="left", anchor="md")

    draw.text((172, 45), f"{time_text}", 0, font_10, anchor="md")

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)



    draw.text((0, 0), str(current_time), 0, font_10)

    if core_dict["landing_attempt"] == True:
        draw.text((5, 52), f"Landing: Yes", 0, font_9)
    else:
        red_draw.text((5, 52), f"Landen: Nein", 0, font_9)

    if core_dict["reused"] == True:
        draw.text((5, 62), f"Reused: Yes", 0, font_9)
    else:
        red_draw.text((5, 62), f"Reused: No", 0, font_9)

    if type(core_dict["flight"]) == int:
        flight = core_dict["flight"]
        draw.text((5, 72), f"{flight}x Reused", 0, font_9)
    else:
        draw.text((5, 72), f"New Rocket", 0, font_9)
    draw.text((5, 83), f"Soon: {_2_launch}", 0, font_9)

    # draw.text((0, 0), f"{mission_desc_german}", 0, font_10, anchor="ma")

    full_spacex_x = Image.open("spacex.png")

    full_spacex_x_part1 = full_spacex_x.crop((0, 0, calculate_percentage(UNIX_START, UNIX_NOW, UNIX_STOP), 24))
    print(calculate_percentage(UNIX_START, UNIX_NOW, UNIX_STOP))
    with open("start_percent.log", "a") as f:
        f.write("\n" + str(calculate_percentage(UNIX_START, UNIX_NOW, UNIX_STOP)))

    image.paste(full_spacex_x, (156, 69))
    red_image.paste(full_spacex_x_part1, (156, 69))



    image = image.rotate(angle=180)
    red_image = red_image.rotate(angle=180)

    display.Clear()

    display.display_black(display.getbuffer(image=image))
    display.display_red(display.getbuffer(image=red_image))

    time.sleep(900)
# draw.text()