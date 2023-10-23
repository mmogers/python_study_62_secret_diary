# 👉 Day 62 Challenge

Look out, Big Brother!  Today is a project day and you are going to build your own private diary to keep your innermost thoughts secret from the world.

Your diary should:

1. Set an access password.
2. Prompt the user to type in a password.
3. If they don't get the password right, exit the program.
4. If they get it right, they enter the main menu, which gives 'Add' or 'View' diary entries. 
5. Choosing 'add' should:
    1. Prompt the user to type the entry and store it in the database with the timestamp as the key.
6. Choosing 'view' should:
    1. Show the user the previous (most recent) entry.
    2. They can then choose to see the *next* previous entry working backwards until they get to the end. Or exit back to the menu.


🥳 Extra points for adding a feature which allows the user to view an entry from an exact date.

<details> <summary> 💡 Hints </summary>
  
- Use `if passwordEntered != correctPassword` to verify the user.
- Use `os.clear()` to clear the screen between each entry viewed.
- Extra points - compare the date entered to the timestamp and only show if date entered >= timestamp.




</details>