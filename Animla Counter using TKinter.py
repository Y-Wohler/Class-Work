from tkinter import *

cat = 0
dog = 0
animal = 0
animalz = ""
myList = ""
otherAnimal = input("If you have animals other than dog and cat please type 'y', if not type 'n'")

window = Tk()
window.title("Animal Counter")

topframe = Frame(window)
topframe.pack()

bottomframe = Frame(window)
bottomframe.pack(side = BOTTOM)

welcome = Label(topframe, fg="red", font=("Helvetica", 16), text = "Welcome to the pet Selector")
welcome.pack()

if otherAnimal == "y":
    animalz = input("Enter the animal type")
    animal = 0

def name(updateDisplay):
    global outputStr


def addcat(event):
    global cat
    cat = cat + 1
    updateDisplay()

def addanimal(event):
    global animal
    animal = animal + 1
    updateDisplay()

def adddog(event):
    global dog
    dog = dog + 1
    updateDisplay()

def reset(event):
    global cat, dog, animal
    dog = 0
    cat = 0
    animal = 0
    updateDisplay()

def updateDisplay():
    global catTxt, dogTxt, newTxt, outputStr
    name(updateDisplay)
    catTxt = str(cat)
    dogTxt = str(dog)
    newTxt = str(animal)
    outputStr = "There are " + catTxt + " cats," + dogTxt + " dogs"
    if otherAnimal == "y":
        catTxt = str(cat)
        dogTxt = str(dog)
        newTxt = str(animal)
        outputStr = "There are " + catTxt + " cats and " + dogTxt + " dogs"
        outputStr = outputStr + " and " + newTxt + " " + animalz
    outputb1.configure(text = outputStr)

b1 = Button(bottomframe, text = "dog")
b1.bind("<1>", adddog)
b1.pack()
#dog Button

b1 = Button(bottomframe, text = "cat")
b1.bind("<1>", addcat)
b1.pack()
#Cat Button

if otherAnimal == "y":
    b1 = Button(bottomframe, text = animalz)
    b1.bind("<1>", addanimal)
    b1.pack()
#Adding new animal

b1 = Button(bottomframe, text = "Reset")
b1.bind("<1>", reset)
b1.pack()
#Reset Button

outputb1 = Label(bottomframe, text = "")
outputb1.pack()

window.mainloop()