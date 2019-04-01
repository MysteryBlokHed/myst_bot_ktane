# KTaNE Myst Bot
A bot for the game Keep Talking and Nobody Explodes.

## Overview
This is a bot I made for Keep Talking and Nobody Explodes. Normally, the game will require 2 players. A defuser, and an expert. The defuser will interact with the bomb through the game, and the expert will have a [manual](http://www.bombmanual.com/) to assist the defuser. This bot will take the place of the expert.

**This bot is a work in progress. It currently only supports two modules: wires and buttons.**

**Note: Using this bot will take a lot of the fun out of the game. If you want to experience the game as it was intended, get another player to be the expert.**

## Requirements
**Python v3+**  
If you don't already have it, download it [here](https://www.python.org/downloads/).  
**PyAudio**  
Download using `pip install PyAudio`, or download the latest wheel [here](https://pypi.org/project/PyAudio/#files) and use `pip install (.whl file)`.  
**SpeechRecognition**    
Download using `pip install SpeechRecognition`, or download the latest wheel [here](https://pypi.org/project/SpeechRecognition/#files) and use `pip install (.whl file)`.  
**pyttsx3**  
Download using `pip install pyttsx3`, or download the latest wheel [here](https://pypi.org/project/pyttsx3/#files) and use `pip install (.whl file)`.

I have only tested the bot on Windows, so I can't guarantee it will work on other platforms.

## Starting the bot
Make sure you're in the same directory as the main folder. Then, run `python main.py`.

## Instructions
The idea is to say a command, followed by the arguments required for that command.

### Bomb details
    serial number <#>        - Last digit of serial number
    batteries <#>            - Amount of batteries on bomb
    serial vowel <yes/no>    - Vowel in serial number
    car indicator <yes/no>   - Lit CAR indicator on bomb
    freak indicator <yes/no> - Lit FRK indicator on bomb
    parallel port <yes/no>   - Parallel port on bomb (long pink one)
### Reset bomb
    bomb reset
### Simple wires
    wires <wires> - <wires> is replaced with red, blue, yellow, black or white respectively.  
Example:

    wires red blue red red blue
### Button
    button <colour> <text>  
If you need to press and hold:

    button colour <strip colour>
