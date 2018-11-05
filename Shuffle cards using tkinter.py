from tkinter import *

import random

def drawCards():
	global lablelist,cards
	for card in cards:
		cardTxt = str(card[0])+" "+ str(card[1])
		if card[1] == "Hearts" or card[1] == "Diamonds":
			cardColor = "red"
		else:
			cardColor = "black"
		lablelist.append(Label(lblframe, fg=cardColor, font=("Helvetica", 10), text = cardTxt))

	for i in range(0,len(lablelist)):
		lablelist[i].grid(row=i, column = 0)


def shuffle(event):
	global cards, lablelist, i
	while counter < 2 * lists:
		x = cards.pop(i)
		cards.append(x)
	drawCards()

window = Tk()#create the window#
window.title("Mr Jacob")

cards = [[2, "Hearts"],
[3,"Hearts"],
[4,"Hearts"],
[5,"Hearts"],
[6,"Hearts"],
[3,"Clubs"],
[4,"Clubs"],
[5,"Clubs"],
[6,"Clubs"]]
##Setup frames##
counter = 0
lists = len(cards)
lablelist = 0
i = random.randint(0,lists-1)

topframe = Frame(window)
topframe.pack()
midframe = Frame(window)
midframe.pack()

lblframe = Frame(midframe)
lblframe.pack()

bottomframe = Frame(window)
bottomframe.pack(side = BOTTOM)
##setup label to display output in top frame##
welcome = Label(topframe, fg="red", font=("Helvetica", 16), text = "Shuffle the cards")
welcome.pack()

lablelist=[]
drawCards()

b1 = Button(bottomframe, text='shuffle')
b1.bind("<1>", shuffle)
b1.grid(row=0, column = 0)
window.mainloop()
