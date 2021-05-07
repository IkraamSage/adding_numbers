# adding_numbers exercise
# this exercise consists of adding 2 numbers with a third prompt showing the answer
import tkinter
import tkinter as tk


root= tk.Tk()
# size of window
root.geometry("450x220")
label1 = tk.Label(root, text = "Please enter the first number")

# placing buttons
label1.grid(row=0, column=0)
label2 = tk.Label(root, text = "Please enter second number")
label2.grid(row=1, column=0)
label3 = tk.Label(root, text = "sum of two numbers is:")
label3.grid(row=2, column=0)

# defining clearing functions
def clear():
    entry1.delete(0,tkinter.END)
    entry2.delete(0,tkinter.END)
    entry3.delete(0,tkinter.END)

# button and entry funtions
button2 = tk.Button(root, text = "clear", command = clear)
button2.grid(row=4, column=1)
button3 = tk.Button(root, text = "exit", command = exit)
button3.grid(row=4, column= 2)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)
entry3 = tk.Entry(root)
entry3.grid(row= 2, column=1)

# defining the functions of the entries
def addNumbers():
    # prompt that allows to enter numbers that are about to be added
    sum=int(entry1.get())+int(entry2.get())
    entry3.insert(0,str(sum))

button1 = tk.Button(root, text="add", command=addNumbers)

button1.grid(row=4, column=0)

# adding a mainloop in order for it to run
root.mainloop()

