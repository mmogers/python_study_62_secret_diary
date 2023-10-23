# Solution (No Peeking!)
![](https://www.youtube.com/watch?v=Xckgpc0-5eA)

<details> <summary> 👀 Answer </summary>

```python
from replit import db
import datetime, os, time

def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

def viewEntry():
  keys = db.keys()
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0]=="e"):
      break


password = input("Password: ")
if password != "baldy1":
  print("Incorrect")
  exit()
while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()

```

</details>

- Join our [100 Days Community](https://replit.com/100-days-help)
- Join our [Discord](https://replit.com/discord)
- Want [live support?](https://replit.com/replit-101)