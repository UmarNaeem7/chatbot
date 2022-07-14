import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
from tkinter import *
from PIL import Image, ImageTk
from winsound import *

#open training data from json file
file = open("resources/training intents.json", 'r')
data = json.load(file)
file.close()

words = []
labels = []
train_x = []
train_y = []

#extract data in lists
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)  #tokenize pattern into a list of words
        words.extend(wrds)
        train_x.append(wrds)     #add patterns and their corresponding tag in x & y lists respectively
        train_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

#find root words to generalize them
words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))
labels = sorted(labels)

training = []
output = []

#convert processed strings in numerical forms as neural networks require numerical input
out_empty = [0 for _ in range(len(labels))]
for x, doc in enumerate(train_x):
    bag = []
    #generalize words
    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)   #1 will indicate that word is present
        else:
            bag.append(0)   #0 will indicate that word is not present

    output_row = out_empty[:]
    output_row[labels.index(train_y[x])] = 1

    training.append(bag)
    output.append(output_row)

#convert to numpy arrays
training = numpy.array(training)
output = numpy.array(output)

#-------------------machine learning-----------------------------

#reset configurations
tensorflow.reset_default_graph()

#develop feed forward neural network (ffnn) with 2 hidden layers

#pass training data
net = tflearn.input_data(shape=[None, len(training[0])])
#pass to 1st hidden layer with 8 neurons
net = tflearn.fully_connected(net, 8)
#pass to 2nd hidden layer with 8 neurons
net = tflearn.fully_connected(net, 8)
#represent probabilities
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

#use deep neural network
model = tflearn.DNN(net)
model.fit(training, output, n_epoch=1800, batch_size=8, show_metric=True)

#------------------------------------------------------------------------

#process numerical output from neural network
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)

#-------------------------------------GUI---------------------------------------------#

#-----------------intro window--------------#
intro = Tk()
intro.title('AI Chatbot by Umar(17L-4065),Abdullah(4038),Hafiz Irshad(4273)')
intro.resizable(0,0)
intro.iconbitmap('resources/icon.ico')

#disable close
def doNothing():
    a = 4

intro.protocol('WM_DELETE_WINDOW', doNothing)
topFrame = Frame(intro)
topFrame.pack()
bottomFrame = Frame(intro)
bottomFrame.pack(side=BOTTOM)
image = Image.open("resources/bot.png")
photo = ImageTk.PhotoImage(image)

label = Label(topFrame, image=photo)
label.image = photo
label.pack()

def buttonCLick():
    intro.destroy()


startButton = Button(bottomFrame, command=buttonCLick, text='Start')
startButton.pack()

intro.mainloop()


#--------------------Chat window-----------------------#
root = Tk()
root.title('AI Chatbot by Umar(17L-4065),Abdullah(4038),Hafiz Irshad(4273)')
root.resizable(0,0)
root.iconbitmap('resources/icon.ico')

#add widgets
label1 = Label(root, text='Chat transcript:').grid(row=0, sticky=W)

chats1 = Text(root, height=15)
chats1.grid(row=1)

label2 = Label(root, text='Enter chat messages:').grid(row=2, sticky=W)

chats2 = Text(root, height=15)
chats2.grid(row=3)

#add scrollbar to chat transcript
s = Scrollbar(root)
chats1.config(yscrollcommand=s.set)
s.config(command=chats1.yview)
s.grid(row=1, column=1, sticky=N + S + W)

#callback to input user message
def inputMessage(event):
    message = chats2.get('1.0', 'end-1c')
    if not message:
        return
    chats2.delete('1.0', END)
    doChat(message)

#bind enter key event in message typing text box
chats2.bind('<Return>', inputMessage)

#callbacks to print messages in chat transcript
def printChat(message):
    chats1.insert(END, message + '\n')

def printBotReply(message):
    chats1.insert(END, message + '\n')
    return PlaySound("resources/sound.wav", SND_FILENAME)


#-------------------------------------------------------------------------------#
#function to implement chat functionality
def doChat(message):
    inp = message
    if inp[len(inp)-1] == '\n':
        inp = inp[:-1]
    printChat('You:' + inp)

    if not inp:
        printBotReply("Bot:Please type something :(")
    else:
        #store calculated probabilities of tags
        results = model.predict([bag_of_words(inp, words)])[0]
        #find tag with max probability for input string
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        #determine if tag with max probability has a very probaility as compared to all other tags
        #the set threshold is experimental
        if results[results_index] > 0.75:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']

            #print any random response from the group of responses for the tag selected
            printBotReply('Bot:' + random.choice(responses))

        #as max probability is not very high so there is a good chance that there is no available response
        #for the input string, so we should prevent a random answer that won't make any sense
        else:
            printBotReply('Bot:I didnt understand what u said')

root.mainloop()