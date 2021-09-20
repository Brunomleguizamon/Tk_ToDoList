from tkinter import *
import sqlite3

root = Tk()
root.title('To Do List')
root.geometry('500x500')

conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists todo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    );
""")

conn.commit()

def renderTodo():
    rows = c.execute("SELECT * FROM todo").fetchall()

    for i in range(0, len(rows)):
        completed = rows[i][3]
        description = rows[i][2]
        l = Checkbutton(frame, text= description, width=42, anchor="w")
        l.grid(row=i, column=0, sticky="w")

def addTodo():
    todo = e.get()
    if todo:
        c.execute("""
            INSERT INTO todo (description, completed) VALUES(?, ?)
                """, (todo, False))
        conn.commit()
        e.delete(0, END)
        renderTodo()
    

l = Label(root, text="Task")
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text="Add", command= addTodo)
btn.grid(row=0, column=2)

frame = LabelFrame(root, text="My Task", padx=5, pady=5)
frame.grid(row=1,column=0, columnspan=3,sticky="nswe", padx=5)

e.focus()
root.bind('<Return>', lambda x: addTodo())


root.mainloop()
