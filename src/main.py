from tkinter import * 


# 1- Create class Person with __init__ method wit private __name

    # create variable total = 0
    
    # in __init__ set self.__name = __name
    
        # private variable name
        
        # increment total by 1
        

    # create set_name() function

    # create get_name() function
    
    # create a method write_file() function
        # open file names.txt in append mode
            # write self.name to file
        # close file
    
    # create a classmethod print_file() 
        # open file names.txt in read mode
            # print file name 
    

tk = Tk()  
tk.title("Python 102")
tk.geometry("900x600") # set window size

lab = Label(tk, text="Enter a name") # defined
lab.pack() # display

ent = Entry(tk) 
ent.pack()

# ____ Your code here ____
# 2- Create function check_inputs()

    # check if ent.get() is empty True then msg.config text = "Error message"
  
        
    # else create object from Task class pass ent.get() as argument 

        # print total 
        
        # edit msg using .config to display the name added ex: "Ahmed added" use f-string 
        
        # call write_file() method from obj1   
        

msg = Label(tk, text="") 
msg.pack() 

btn = Button(tk, text="Save", command=check_inputs)
btn.pack()

print("_____________")
# 3- Call print_file() method from Person class


tk.mainloop()
