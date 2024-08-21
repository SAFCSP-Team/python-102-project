# Python 102

# Objective
This project will validate your knowledge of the Python 102 topics.

# Problem
You must build a GUI application to save a person's name in a file. The application should add a name, and display all names. 

# Implementation

Create Two Files: `main.py` and `names.txt`.

1. Create class `Person`
    - create object private variable `name`
    - create a `get_name` function to return name
    - create a `set_name` function to set name
    - create a `write_task` function to append a name to the file `names.txt`

2. Create a Tkinter window with the following specifications:
    - Name: tk
    - Title: Task Tracker
    - Geometry: 900x600

3. Create Label and Entry to add tasks. 
    - Create a Label: Enter Task called `task_label`
    - Create an Entry: To enter the task called `task_entry`

4. Create message Label
    - Create an **empty** Label called `message_label` to display messages 

5. Create function `check_input()`
    - if `task_input` is empty config message_label to display "Please enter a task"
    - else config message_label to display "Task Added" and create object of `Task` class, pass `task_input` as parameter and call `write_task()` function

6. Create Button to add tasks
    - create a Button called `save_button` with text "Save Task" and command `check_input`

7. call `mainloop()` to run the window
