# Project discontinued due to unavailable API!

Sadly, the r/SpaceX-API is no longer active, so this project does not work,
But thankfully [@rizzl3r](https://github.com/rizzl3r) ( Thank you :D ) continued development of this project
and is now using a different+better API and fixed some other stuff.

[His new repo](https://github.com/rizzl3r/SpaceX-Launch-Tracker)

---

# SpaceX-Launch-Tracker

## Install

Install PIL library:
```bash
python3 -m pip install Pillow
```
Also, you need to enable SPI in your raspi-config:
```bash
sudo raspi-config
```
Go to "Interface Options" and enable SPI.

Thats it! Now you can run the program:
```bash
python3 main.py
```

## Note:
This Program was designed for the Waveshare 2.13 Inch E-Paper Display (Red/Black/White)!
You can buy it
[here](https://www.waveshare.com/2.13inch-e-paper-hat-b.htm).

You can find a tutorial [here](https://www.electromaker.io/project/view/jonathan357611spacex-launch-tracker)

## Description
This code uses the Pillow library to create the image which will be shown on the display.

The Display show all important informations about the next launch like these:

- Name of the next rocket (and the rocket after that)
- If it lands
- If it was reused
- how often it was reused
- when the rocket will launch
- The time the display refreshed itself
- The SpaceX logo works as a "Progress Bar" (Left side of X=Last launch, Right side= next launch, edge between red/black = current time) 

## Image

![Image](https://preview.redd.it/52g9xqpay7371.jpg?width=960&crop=smart&auto=webp&s=07689cdbafba99e23649e644a1e26e3f6d572140)



I am still learning, if you see any errors or have a way to code it better, please contact me! :)
