from replit import db
import os
import time
import datetime
import pytz
import getpass

rigaTZ = pytz.timezone("Europe/Riga")
LIMIT = 1 
#-------------------------------------------------
def myInputPrint(text):  #prints input text with green clolor
  result = input(f"""{text} \033[32m""")
  print("\033[0m", end="")
  return result
#--------------------------------------------------
def addEntry():
  entry = myInputPrint("\nEnter your upadte:\n> ").capitalize()
  timestamp = datetime.datetime.now(rigaTZ)
  db[timestamp] = entry
#---------------------------------------------------
def viewEntry():
  keys = list(db.prefix("2023")) #the list of all keys  - entries
  keys.sort(reverse=True) #sort in reverse order
  limitCounter = 0  #how much to show at once counter
  counter = 0 #printed tweets counter
  while True:
      entryList = []
      startIndex = limitCounter * LIMIT
      endIndex = (limitCounter + 1) * LIMIT

      for key in keys[startIndex:endIndex]:
        entryList.append({key: db[key]}) #key value pairs

      if not entryList:
          print("\nNo entries to display.")
          break

      for entry in entryList:
          entryKey = list(entry.keys())[0]
          print(f"{entryKey}: {entry[entryKey]}")
          counter += 1
          time.sleep(1)
      time.sleep(3)

      if counter < len(keys): #show next entry (amount to show - LIMIT)
        answer = myInputPrint(f"\nDo you want to see the next {LIMIT} entry? (y/n)\n> ").lower()
        if answer == "y":
          limitCounter += 1
        else:
            break
      else:
        print("\nNo more entries to display.")
        time.sleep(3)
        break
#---------------------------------------------------
def printMenu():  
  while True:
    os.system("clear")
    print(f"\033[1;32mWelcome to your secret diary, {user}!\033[0m")
    choice = int(myInputPrint("\nPress 1 to Add a new entry\nPress 2 to View a recent entry\n> ")) #check integer
    if choice == 1:
      addEntry()
      print("Added!")
      time.sleep(2)
    elif choice == 2:
      viewEntry()
      time.sleep(2)
    else:
      print("Invalid choice")
      time.sleep(2)
      continue
#-------------------------START--------------------
  
keys = db.keys()
user = input("Enter your username:\n> ")
if user in keys:
  password = getpass.getpass("Enter your password:\n> ")
  if db[user] == password:
    print(f"Welcome {user}!")
    time.sleep(2)
    printMenu()
  else:
    print("Incorrect password.")
    time.sleep(1)
    exit("Bye!")
else:
  print("User not found.")
  time.sleep(1)
  exit("Bye!")
#----------------------END--------------------------









