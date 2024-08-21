# Python 102

# Objective
This project will validate your knowledge of the Python 102 topics.

# Problem
You must build a GUI application to save a person's name in a file. The application should add a name, and display all names. 

# Implementation

Create Two Files: `main.py` and `names.txt`.

1. Create class `Person`
    - create object private variable `name`
    - create a `get_name` function to return the `name`
    - create a `set_name` function to set the `name`
    - create a `write_file` function to append a name to the `names.txt` file
    - create a class method `print_file` function to print the file `names.txt` content

2. Create function `check_input()` in the body do the following:
    - if `ent` is empty change `msg` to display "Please enter a name"
    - else change `msg` to display "Name added"
    - create an object called `obj1` from the Person class and pass the `ent.get()` as an argument
    - call `write_file()` from `obj1`
    - print the `total` 

6. Call `print_file()`
    - before `tk.mainloop()` call the `print_file()` from `Person` class
