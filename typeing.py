# Importing modules...

from tkinter import *
import random
import time

# Tkinter window set up

root = Tk()
root.title('Typing test by Parth Parmar')
root.geometry('1350x650') # width x height
root.config(bg='#64d7fa')

# Global vars 
wrong = 0

def pause(): # left
    
    if pause:
        time.sleep(1000)


def self():
    
    root.option_add('*Label.Font','consolas 22')
    
    global title; title = Label(root,text='Typing Speed Test Software',fg='black',bg='#64d7fa')
    title.place(relx=0.5,rely=0.1,anchor=S)
    
    root.option_add('*Label.Font','consolas 16')
    
    global NAME ; NAME = Label(root,text='Enter your name',fg='black',bg='#64d7fa')
    NAME.place(relx=0.42,rely=0.19,anchor=S)
    
    global n 
    n = StringVar()
    
    global name; name = Entry(root.option_add('*Label.Font','consolas 16'),textvariable=n, bd =4)
    name.place(relx=0.57,rely=0.19,anchor=S,width=160)
    
    global strName ; 
    strName = n.get()
    
    global CUSTOM; CUSTOM = Label(root,text='Enter custom text',fg='black',bg='#64d7fa')
    CUSTOM.place(relx=0.42,rely=0.26,anchor=S)
    
    global custom; custom = Entry(root.option_add('*Label.Font','consolas 16'), bd =4)
    custom.place(relx=0.642,rely=0.40,anchor=S,width=360,height=120)
    
    global MAIL ; MAIL = Label(root,text='Enter your e-mail',fg='black',bg='#64d7fa')
    MAIL.place(relx=0.42,rely=0.48,anchor=S)
    
    global mail; mail = Entry(root.option_add('*Label.Font','consolas 16'), bd =4)
    mail.place(relx=0.57,rely=0.48,anchor=S,width=160)
    
    root.option_add('*Button.Font','consolas 22')
    
    global enterButton; enterButton = Button(root,text='Go!!',command=destroySelf)
    enterButton.place(relx=0.5,rely=0.7,anchor=CENTER)

def destroySelf(): 
    
    enterButton.destroy(); resetWritingLabels() 
    NAME.destroy() ; name.destroy()
    CUSTOM.destroy(); custom.destroy()
    MAIL.destroy(); mail.destroy()

def keyPress(event=None):
    
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            
            # Deleting one from right side
            labelRight.configure(text=labelRight.cget('text')[1:])
            
            # Deleting one from the right side.
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            
            #set the next Letter Lavbel
            currentLetterLabel.configure(text=labelRight.cget('text')[0],fg='blue')
            
        else:
            currentLetterLabel.configure(text=event.char.lower(),fg='red')
            global wrong ; wrong += 1
            
    except TclError: pass
    
def resetWritingLabels():
    
    # Personalizing
    
    root.option_add('*Label.Font','consolas 28')
    
    global displayName ; displayName=Label(root,text=strName,fg='black',bg='#64d7fa')
    displayName.place(relx=0.2,rely=0.1,anchor=S)
    
    possibleTexts = [
        'For writers, a random sentence can help them get their creative juices flowing. Since the topic of the sentence is completely unknown, it forces the writer to be creative when the sentence appears. There are a number of different ways a writer can use the random sentence for creativity. The most common way to use the sentence is to begin a story. Another option is to include it somewhere in the story. A much more difficult challenge is to use it to end a story. In any of these cases, it forces the writer to think creatively since they have no idea what sentence will appear from the tool.',
        'The goal of Python Code is to provide Python tutorials, recipes, problem fixes and articles to beginner and intermediate Python programmers, as well as sharing knowledge to the world. Python Code aims for making everyone in the world be able to learn how to code for free. Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.',
        'As always, we start with the imports. Because we make the UI with tkinter, we need to import it. We also import the font module from tkinter to change the fonts on our elements later. We continue by getting the partial function from functools, it is a genius function that excepts another function as a first argument and some args and kwargs and it will return a reference to this function with those arguments. This is especially useful when we want to insert one of our functions to a command argument of a button or a key binding.'
    ]
    text = random.choice(possibleTexts).lower() # one line from the list
    
    splitPoint = 0
    
    global labelLeft; labelLeft = Label(root,text=text[:splitPoint],fg='grey')
    labelLeft.place(relx=0.5,rely=0.5,anchor=E)
    
    global labelRight ; labelRight = Label(root,text=text[splitPoint:])
    labelRight.place(relx=0.5,rely=0.5,anchor=W) # relx and rely screen divide by 10 values, must in float
    
    global currentLetterLabel ; currentLetterLabel = Label(root,text=text[splitPoint],fg='blue')
    currentLetterLabel.place(relx=0.5,rely=0.6) # anchor = N

    root.option_add('*Label.Font','consolas 26')
    
    global timeleftLabel; timeleftLabel = Label(root,text='0 Seconds')
    timeleftLabel.place(relx=0.85,rely=0.4,anchor=S)
    
    file = open('score.txt','r')
    global content ;content = file.readline()
    
    root.option_add('*Label.Font','consolas 20')
    
    global highscore; highscore = Label(root,text=f'Highest Speed: {content} WPM',fg='black')
    highscore.place(relx=0.15,rely=0.25,anchor=S)
    
    # global writeAble; writeAble = True
    root.bind('<Key>',keyPress)
    
    global passedSeconds; passedSeconds = 0
    
    global min; min = 0.5
    global time; time = int(min*60*1000)
    
    root.after(time,stopTest) # after this 'time' do this 'stopTest'
    root.after(1000,addSeconds)
    
    root.option_add('*Label.Font','consolas 15')
    
    global quoteLabel; quoteLabel = Label(root,text=f'Focus on accuracy rather than speed...',fg='red',bg='#64d7fa')
    quoteLabel.place(relx=0.5,rely=0.9,anchor=CENTER)
    
def stopTest():
    
    # Calculating the amount of words
    amountOfChar = len(labelLeft.cget('text')) # split by space so word count will be found
    
    # Calculating speed
    
    speed = int((amountOfChar/5)/min)
    strSpeed = str(speed)
    
    # Calculating the accuracy
    
    global accuracy;accuracy = int(100 - (100*wrong)/amountOfChar)
    if accuracy < 0: accuracy = 0
        
    # writing score
    
    file = open('score.txt','w')
    if int(content) < speed: file.write(strSpeed)
    else: file.write(content)
    
    # Destroy all unwanted widgets
    
    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()
    
    root.option_add('*Label.Font','consolas 26')
    
    global ResultLabel; ResultLabel = Label(root,text=f'Speed: {speed} WPM(Words Per Minute)',fg='black')
    ResultLabel.place(relx=0.5,rely=0.4,anchor=CENTER)
    
    global accuracyLabel; accuracyLabel = Label(root,text=f'Accuracy: {accuracy}%',fg='black')
    accuracyLabel.place(relx=0.5,rely=0.5,anchor=CENTER)

    global resetButton; resetButton = Button(root,text='Retry',command=restart) #(root,text,function)
    resetButton.place(relx=0.44,rely=0.7,anchor=CENTER)
    
    global saveButton; saveButton = Button(root,text='Save') #(root,text,function)
    saveButton.place(relx=0.56,rely=0.7,anchor=CENTER)
    
def restart():
    
    ResultLabel.destroy()
    resetButton.destroy()
    accuracyLabel.destroy()
    saveButton.destroy()
    
    # Reseting writing labels...
    resetWritingLabels()    
    
def addSeconds():
    
    global passedSeconds; passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Seconds')
    
    if True: root.after(1000,addSeconds) # 1000 = 1 sec
        
self()
root.mainloop()
