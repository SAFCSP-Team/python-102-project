from tkinter import * 

# Create class Person with __init__ method
    # in __init__ set self.name = name
    # create set_name() and get_name() functions
    # create write_file() function
        # open file tasks.txt in append mode
        # write self.name to file
        # close file

tk = Tk()  
tk.geometry("900x600") # set window size

lab = Label(tk, text="Enter a name") # defined
lab.pack() # display

ent = Entry(tk) 
ent.pack()

msg = Label(tk, text="") 
msg.pack() 

# Your code here
# create function check_inputs()
    # check if ent.get() is empty True then msg.config text = "Error message"
    # else create obj1 from Task class pass ent.get() as argument 
    # call write_file() method from obj1   

btn = Button(tk, text="Save")
btn.pack()

tk.mainloop()