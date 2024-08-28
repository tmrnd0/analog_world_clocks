#2024 ixkakaw. This is a analog world clock script that works by timezones.

import tkinter as tk
import time
import math
from datetime import datetime
from pytz import timezone
import sys
from tkinter import *

W = 146 		# oval position makes outline of oval to dissapear. Adjusted by subtracting one unit from W and H
H = 146 		# height and width of each clock oval.
CH = 150 		# height and width of each clock oval.
CW = 150
PX = 7			# x padding of each canvas.
PY = 7

color = "#212121"														#background color	

root = tk.Tk() 															#initiates main window
root.title("Analog World Clocks")												#window title
root.config(bg = color)													#window color

canvas_belize = Canvas(root, width=CW, height=CH, bg=color, 			#creates single canvas for each clock to be used for the_clock function. bd=0, highlightthickness=0 disables canvas border.
relief='flat', bd=0, highlightthickness=0)
canvas_saopaulo = Canvas(root, width=CW, height=CH, bg=color, 
relief='flat', bd=0, highlightthickness=0)
canvas_casablanca = Canvas(root, width=CW, height=CH, bg=color, 
relief='flat', bd=0, highlightthickness=0)
canvas_calcutta = Canvas(root, width=CW, height=CH, bg=color, 
relief='flat', bd=0, highlightthickness=0)
canvas_kamchatka = Canvas(root, width=CW, height=CH, bg=color, 
relief='flat', bd=0, highlightthickness=0)

def the_clock(region, city, canvas, C):

    canvas.grid(row = 0, column = C, padx = PX, pady = PY)				#constructs the grid so that clocks are aligned in single row
    
    canvas.delete("all")												#deletes the animation of arrows with each iteration	
    
    datetime.now(timezone(region)).time()								#obtains the time according to region
    
    x = datetime.now(timezone(region)).hour
    y = datetime.now(timezone(region)).minute
    z = datetime.now(timezone(region)).second

    hour = x %12
    minute = y
    second = z

    canvas.create_oval(2, 2, H, W, outline="#0D7377",	
    width=0.5, fill = '#323232')										#draws cirle enclosing clock

    canvas.create_text(CH/2, CW/2, text=str(city), 
    fill= "#14FFEC", font=("Helvetica 13 bold"))						#prints text of city inside each clock	
    
    for i in range(12):													#draws the numbers
        angle = i * math.pi/6 - math.pi/2
        x = (W)/2 + 0.80 * (W)/2 * math.cos(angle)
        y = (H)/2 + 0.80 * (H)/2 * math.sin(angle)
        if i == 0:
            canvas.create_text(x, y, text=str(i+12), fill = "#FBFF64", font=("helvetica", 9))
        else:
            canvas.create_text(x, y, text=str(i), fill="#FBFF64", font=("helvetica", 9))

    hour_angle = (hour + minute/60) * math.pi/6 - math.pi/2				#draws hours' hand
    hour_x = W/2 + 0.5 * W/2 * math.cos(hour_angle)
    hour_y = H/2 + 0.5 * H/2 * math.sin(hour_angle)
    canvas.create_line(W/2, H/2, hour_x, hour_y, fill="#FF0032", width=4)

    minute_angle = (minute + second/60) * math.pi/30 - math.pi/2		#draws minutes' hand
    minute_x = W/2 + 0.7 * W/2 * math.cos(minute_angle)
    minute_y = H/2 + 0.7 * H/2 * math.sin(minute_angle)
    canvas.create_line(W/2, H/2, minute_x, minute_y, fill="#FF0032", width=2)

    second_angle = second * math.pi/30 - math.pi/2						#draws seconds' hand
    second_x = W/2 + 0.6 * W/2 * math.cos(second_angle)
    second_y = H/2 + 0.6 * W/2 * math.sin(second_angle)
    canvas.create_line(W/2, H/2, second_x, second_y, fill="#FF0032", width=1)
    
    canvas.after(1000, the_clock, region, city, canvas, C)

the_clock('America/Belize', 'Belize', canvas_belize, 0)					#calls the function the_clock for each region
the_clock('America/Sao_Paulo', 'Sao Paulo',  canvas_saopaulo, 1)
the_clock('Africa/Casablanca', 'Casablanca',  canvas_casablanca, 2)
the_clock('Asia/Calcutta', 'Calcutta', canvas_calcutta, 3)
the_clock('Asia/Kamchatka', 'Kamchatka', canvas_kamchatka, 4)


root.mainloop()															# runs the main loop 

#colors and regions can be changed accordingly. For more regions check: https://mljar.com/blog/list-pytz-timezones/ or the README file.

