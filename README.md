# chatbot

# Problem Statement
Build an AI (ML) based chat bot that will intelligently reply to the user’s text string. The bot should be 
extremely customizable so that it can be used for various purposes in future easily. For example, training 
the bot to handle business inquiries, act as a guide bot on websites or software, handle day to day 
casual chats, etc. 
In case of chats for which the bot can’t give a proper reply, the bot should acknowledge its lack of 
knowledge (insufficiency of training data) with replies like ‘I did not understand what you said.’ instead 
of giving out a random reply which doesn’t make any sense.
Lastly, the chat bot should be usable through a proper Graphical User Interface (GUI).

# Methodology
Python 3.8 is used to implement this project.

# Modules used

# Natural Language Toolkit (NLTK):
The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic 
and statistical natural language processing for English written in the Python programming language.
In this project, it is used for word stemming and some other string operations.

# NumPy:
NumPy is a library for the Python programming language, adding support for large, multi-dimensional 
arrays and matrices, along with a large collection of high-level mathematical functions to operate on 
these arrays.
In this project, to pass input data into neural network, we first need to convert it to numpy arrays.

# TFlearn:
TFlearn is a modular and transparent deep learning library built on top of TensorFlow. It was designed to 
provide a higher-level API to TensorFlow in order to facilitate and speed-up experimentations, while 
remaining fully transparent and compatible with it.
In this project, it is used to create neural network and pass input data into it.

# TensorFlow:
TensorFlow is a free and open-source software library for dataflow and differentiable programming 
across a range of tasks. It is a symbolic math library, and is also used for machine learning applications 
such as neural networks.
In this project, it is used to create neural network and pass input data into it.

# Random:
Generates random numbers.
In this project, it is used to pick a randomized response once the correct tag is picked as for each tag we 
have a couple of responses.

# JSON:
Read data from .json files and store it in data dictionary and vice versa.
in this project, it is used to open training data from a json file into a python data dictionary.

# Tkinter:
Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, 
and is Python's de facto standard GUI. Tkinter is included with standard Linux, Microsoft Windows and 
Mac OS X installs of Python. The name Tkinter comes from Tk interface.
in this project, it is used to create the GUI of the application.

# Image, ImageTk:
Open images and add them to Tkinter’s widgets.
In this project, it is used to add image to a window and icons to the GUI application.

# Winsound:
The winsound module provides access to the basic sound-playing machinery provided by Windows 
platforms. It includes functions and several constants. 
In this project, it is used to play a notification alert sound when the bot replies.

# Dataset
Since, we want to keep the bot highly customizable and self-controlled, so we use our own created 
dataset. The dataset currently has 16 tags, with each tag having multiple patterns and responses. We 
want to test the bot for casual day-to-day chats so the tags are simple like greeting, weather, name, age, 
etc. Using this dataset, the bot is able to properly answer tens and hundreds of input strings related to 
common daily chats. We acknowledge that the bot is working on a fairly small dataset but 
customizability is our requirement so that we can use it for future endeavors.

# Programming Approach
The program will be explained in a series of in-order steps:
• open json file containing the training data  
• extract data from this file in a data dictionary  
• extract tags, patterns and their responses in separate lists from dictionary  
• stem the words in the list which contains patterns so that we can generalize them and this will   
enable to understand words similar to the ones that are stored  
• to pass input data in neural networks, we need to convert the data that is in the form of strings   
to numerical form  
• 1 in this numerical input for a particular words indicates its presence and 0 its absence  
• convert the numerical input data to numpy arrays  
• we will use Feed Forward Neural Network to train the bot  
• pass the input data in ffnn  
• this ffnn model will contain 2 hidden layers, each with 8 neurons  

<image src="/resources/nn.png">


