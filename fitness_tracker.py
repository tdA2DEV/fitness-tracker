#!Python3
#This app will track daily fitness activities.
#This project will be a constantly evolving program to introduce a gui and web interface.
#I plan to make this a docker image

#Imports
import json
import csv
import os
import datetime

#------------------------------------------------------------------------------------
                                        #Variables
#Logs
exerciseLib = "./libs/exercise_library.xml"
skillLib = "./libs/skills_library.xml"
yogaLog = "./logs/yoga_tracker.csv"
medLog = "./logs/meditation_tracker.csv"
glutesLog = "./logs/glutes_tracker.csv"
abLog = "./logs/abs_tracker.csv"
cardioLog = "./logs/cardio_tracker.csv"
shoulderLog = "./logs/shoulder_tracker.csv"
backLog = "./logs/back_tracker.csv"
legsLog = "./logs/leg_tracker.csv"
chestLog = "./logs/chest_tracker.csv"
skillLog = "./logs/skill_tracker.csv"

#Lists
mainOptions = []
yogaStyles = ['Hatha', 'Iyengar', 'Bikram', 'Ashtanga', 'Vinyasa', 'Yin', 'Restorative']
medStyles = ['Mindfulness', 'Spiritual', 'Focused', 'Movement', 'Mantra', 'Trancendent', 'Progressive Relaxation', 'Loving Kindness']

#Menu Navigation
mainMenu = ['Check Progress', 'Add Activity', 'Edit Activity', 'Excercise Glossary', 'Skills Glossary', 'Exit']
addActivityMenu = ['Yoga', 'Meditation', 'Glutes', 'Shoulders', 'Abs', 'Cardio', 'Back', 'Legs', 'Chest', 'Skill', 'Exit']
editActivityMenu = ['Yoga', 'Meditation', 'Glutes', 'Shoulders', 'Abs', 'Cardio', 'Back', 'Legs', 'Chest', 'Skill', 'Exit']



yogaFileHeader = ['Date', 'Type', 'Duration', 'Link']

#Other
#yes = ['yes', 'y']
#------------------------------------------------------------------------------------

#Functions

def addYoga():
    for i in yogaStyles:
        print('{}: {}'.format(yogaStyles.index(i), i))
    choice = int(input('Choose a yoga style: '))
    length = int(input('How long was the session? '))
    addLink = input('Would you like to add a link? y/n: ')

    if addLink[0].lower() == 'y':
        link = input('Enter the URL:')
    else:
        link = None

    with open(yogaLog, 'a', newline='') as yogaFile:
        dt = datetime.datetime.now()
        date = ('{}/{}/{}'.format(dt.month, dt.day, dt.year))
        writer = csv.writer(yogaFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow((date, yogaStyles[choice], length, link))

#Check if log files exist. If not create empty ones.
try:
    with open(yogaLog, newline='') as yogaFile:
        reader = csv.reader(yogaFile, delimiter=',', quotechar='"')

except:
    with open(yogaLog, 'w', newline='') as yogaFile:
        writer = csv.writer(yogaFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(yogaFileHeader)

finally:
    yogaFile.close()

#Create Function Dictionary
addFunctions = {'Yoga': addYoga,
                #'Meditation': addMed,
                #'Glutes': addGlute,
                #'Shoulders': addShoulder,
                #'Abs': addAbs,
                #'Cardio': addCardio,
                #'Back': addBack,
                #'Legs': addLegs,
                #'Chest': addChest,
                #'Skill': addSkill
                }

#Main Menu Navigation

for i in mainMenu:
    print('{}. {}'.format(mainMenu.index(i), i))
while True:
    try:
        mainChoice = int(input('What would you like to do? '))
    except ValueError:
        print('Please enter a numerical digit')
    else:
        if mainChoice >= len(mainMenu):
            print('Please choose a valid option')
        elif mainChoice == len(mainMenu) - 1:
            break
        else:
            while True:
                if mainChoice == 0:
                    print('This feature is not yet available...')
                    break
                elif mainChoice == 1:
                    for i in addActivityMenu:
                        print('{}. {}'.format(addActivityMenu.index(i), i))
                    try:
                        addChoice = int(input('Which activity would you like to add? '))
                    except ValueError:
                        print('Please enter a numerical digit')
                    else:
                        if addChoice >= len(addActivityMenu):
                            print('Please choose a valid option')
                        elif addChoice == len(addActivityMenu) - 1:
                            break
                        else:
                            addFunctions[addActivityMenu[addChoice]]()

