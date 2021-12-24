# GUPPy v0.1 - Game Uninstalling Program Python

import tkinter, time, threading, random, os
from tkinter import *
from tkinter import ttk, font
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image
from math import floor


### Prog

# Randomly selecting a game
# Read folder with icons named as their game and extract game name

flist = []
rootDir = './images'

for dirName, subdirList, fileList in os.walk(rootDir):
	for fname in fileList:
		if fname[-4:] == '.ico':
			flist.append(fname)

iconname = random.choice(flist)
game = iconname.strip('.ico')
print(len(game))
gpath = game

if len(game) > 13:
	game = game[:13]+'...'


### GUI

master = Tk()
master.title(f'{game} Uninstall')
master.geometry('600x450')
master.resizable(False, False)
master.configure(background='#ededed')

# setting default font
deffont = tkinter.font.nametofont('TkDefaultFont')
deffont.configure(family='Segoe UI',size=10)
master.option_add('*Font', deffont)

# Game Icon
gameimage = Image.open(f'{rootDir}/{iconname}')
gix, giy = gameimage.size # game image x and y

if gix > giy:
	aspect = gix/giy
	gameimage = gameimage.resize((200,floor(200*aspect)))
else:
	aspect = giy/gix
	gameimage = gameimage.resize((floor(80*aspect),80))


icon = ImageTk.PhotoImage(gameimage)
master.iconphoto(False, icon)





## Header

headerframe = Frame(master, background='#fff') # header frame
headerframe.grid(row=0,column=0,sticky='w')

canv1 = Canvas(headerframe, width=200, height=80, background='#000') # Game image canvas
canv1.grid(row=0,column=0)
canv1.create_image(100,40,anchor=CENTER,image=icon)


textframe = Frame(headerframe,width=500, height=80,background='#fff')
# textframe.columnconfigure(0, weight=1)
textframe.grid(row=0,column=1,ipady=18)


tv1 = StringVar(textframe) # uninstalling text variable
tv1var = 'Uninstall'
tv1.set(tv1var)

t1 = Label(textframe, textvariable=tv1, anchor='w', width=40, bg='#fff', fg='#000') # Uninstalling text
t1.config(font=('Segoe UI', 10, 'bold'))
t1.grid(row=0,column=0,sticky='w',padx=10)

tv2 = StringVar(textframe) # Game name text variable
tv2var = f'Remove {game} from your computer.'
tv2.set(tv2var) 

t2 = Label(textframe, textvariable=tv2, anchor='w', width=50, bg='#fff', fg='#000') # Uninstalling game text
t2.grid(row=1,column=0,sticky='w',padx=20)


## Body

# Top message box

tv3 = StringVar(master) # message box variable
tv3var = f'{game} will be uninstalled from the following folder. Click Uninstall to start the uninstallation.'
tv3.set(tv3var)

t3 = Label(master, textvariable=tv3, anchor=CENTER, bg='#ededed', fg='#000') # Uninstalling game text
t3.grid(row=1,column=0,pady=(20,0))


# Progress bar
progbarframe = Frame(master, height=50, width=700, bg='#ededed')
# progbarframe.grid(row=2, column=0, padx=25)

# s = ttk.Style()
# s.configure('Progressbar', background='#ededed')

def uninstall(): # https://pythonguides.com/python-tkinter-progress-bar/

	progbarframe.grid(row=2, column=0, padx=25)
	closebutton.grid(row=0,column=0) # shows close button
	closebutton.config(state='disabled')
	dirframe.grid_forget() # Hides directory frame
	uninbutton.grid_forget() # hides uninstall button

	# Set header messages
	tv1var = 'Uninstalling'
	tv1.set(tv1var)

	tv2var = f'Please wait while {game} is being uninstalled.'
	tv2.set(tv2var)	

	# Set message bar
	tv3var = ''
	tv3.set(tv3var)

	total = 0

	while total < 100:
		master.update_idletasks()
		step = random.randint(1,1) # Random amount for progress bar to increase
		progbar['value'] += step
		time.sleep(random.randint(0,10)/100) # random time between updates
		total += step

	# Set header messages
	tv1var = 'Uninstallation Complete'
	tv1.set(tv1var)

	tv2var = f'Uninstall was completed successfully.'
	tv2.set(tv2var)	

	# Set message bar
	t3.grid(row=1,column=0,padx=21,pady=(20,0),sticky='w')
	tv3var = 'Completed'
	tv3.set(tv3var)

	closebutton.config(state='normal')

progbar = Progressbar(progbarframe, orient=HORIZONTAL, length=550, mode='determinate')
progbar.grid(row=0,column=0)



# Directory

dirframe = Frame(master, background='#ededed')
dirframe.grid(row=3,column=0,sticky='w',padx=10,pady=20) # use grid_forget to hide these widgets on next stage

tv4 = StringVar(dirframe) # message box variable
tv4var = f'Uninstalling from:'
tv4.set(tv4var)

t4 = Label(dirframe, textvariable=tv4, anchor='w', bg='#ededed', fg='#000') # Uninstalling game text
t4.grid(row=0,column=0,padx=10)

tv5 = StringVar(dirframe) # message box variable
tv5var = f'C:/Program Files (x86)/{gpath}'
tv5.set(tv5var)

t5 = Label(dirframe, textvariable=tv5, anchor='w', width=60, bg='#ededed', fg='#000', borderwidth=1, relief='solid') # Uninstalling game text
t5.grid(row=0,column=1,ipadx=10)

# Line

master.rowconfigure(4,weight=1)

canv2 = Canvas(master,height=10,width=600,background='#ededed',highlightthickness=0) # canvas for separation line
canv2.create_line(25, 5, 575, 5, fill='#ababab')
canv2.grid(row=4,column=0,sticky='s')


# Uninstall button

# def on_enter(e):
#     buttonframe['background'] = '#0c92f7'
#     buttonframe['borderwidth'] = 2

# def on_leave(e):
#     buttonframe['background'] = '#000'
#     buttonframe['borderwidth'] = 1



buttonframe = Frame(master, background='#ededed',borderwidth=1)
buttonframe.grid(row=5,column=0,sticky='e',padx=20,pady=20) 

uninbutton = Button(buttonframe, text='Uninstall', command=lambda:threading.Thread(target=uninstall).start(), width=10, background='#ededed')
# uninbutton.bind("<Enter>", on_enter)
# uninbutton.bind("<Leave>", on_leave)
uninbutton.grid(row=0,column=0)


# Close button

closebutton = Button(buttonframe, text='Close', command=lambda:threading.Thread(target=quit()).start(), width=10, background='#ededed')
# closebutton.grid(row=0,column=0,padx=20,pady=20)







master.mainloop()