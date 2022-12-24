from tkinter import *
from tkinter import messagebox


import sqlite3


class DatabaseManagement():
    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.connected_database = False


        # Variables of control
        self.account_id = StringVar()
        self.username = StringVar()
        self.password = StringVar()


        # Menu
        main_menu = Menu(self.root)


        # Configure the window
        self.root.config(menu = main_menu)


        # Add section of BBDD
        database = Menu(main_menu, tearoff = 0)
        main_menu.add_cascade(label = "BBDD", menu = database)


        database.add_command(label = "Connect-BBDD", command = self.databse_connect)
        database.add_command(label = "Exit", command = self.exit_crud)


        # Add section of Delete fields
        deleteFields = Menu(main_menu, tearoff = 0)
        main_menu.add_cascade(label = "Delete", menu = deleteFields)


        deleteFields.add_command(label = "Delete fields", command = self.delete_fields)


        # Frames
        data_frame = LabelFrame(self.root, text = " REGISTER ")
        data_frame.grid(row = 0, column = 0, pady = 5, padx = 10)


        frame_crud = LabelFrame(self.root, text = " CRUD ")
        frame_crud.grid(row = 1, column = 0, pady = 5, padx = 10, sticky = W)


        # Account id
        Label(data_frame, text = "ID:").grid(row = 0, column = 0, pady = 10, padx = 4)
        Entry(data_frame, width = 15, justify = CENTER, textvariable = self.account_id, state = "readonly").grid(row = 0, column = 1, pady = 10, padx = 4)


        # Username
        Label(data_frame, text = "Username:").grid(row = 0, column = 2, pady = 10, padx = 4)
        Entry(data_frame, width = 15, textvariable = self.username).grid(row = 0, column = 3, pady = 10, padx = 4)


        # Password
        Label(data_frame, text = "Password:").grid(row = 0, column = 4, pady = 10, padx = 4)
        Entry(data_frame, show = "*", width = 15, text = self.password).grid(row = 0, column = 5, pady = 10, padx = 4)


        # Buttons
        Button(frame_crud, text = "CREATE", command = self.query_create).grid(row = 0, column = 0, pady = 5, padx = 5)
        Button(frame_crud, text = "READ", command = self.query_read).grid(row = 0, column = 1, pady = 5, padx = 5)
        Button(frame_crud, text = "UPDATE", command = self.query_update).grid(row = 0, column = 2, pady = 5, padx = 5)
        Button(frame_crud, text = "DELETE", command = self.query_delete).grid(row = 0, column = 3, pady = 5, padx = 5)


        self.account_id.set("AUTOINCREMENT")
        self.root.mainloop()


    def delete_fields(self):
        self.account_id.set("AUTOINCREMENT")
        self.username.set("")
        self.password.set("")


    def exit_crud(self):
        exit = messagebox.askquestion("Exit", "Back to menu?")
        if exit == "yes":
            self.root.destroy()


    def databse_connect(self):
        if self.connected_database:
            messagebox.showinfo("Conected Database", "The database is alredy connected")
        else:
            self.connection = sqlite3.connect("BBDD")
            self.cursor = self.connection.cursor()
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Accounts(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    USERNAME VARCHAR(75),
                    PASSWORD VARCHAR(90)
                )
            """)
            self.connected_database = True
            messagebox.showinfo("Connect-BBDD", "Connected Database")


    def query_create(self):
        if self.connected_database:
            if len(self.username.get()) != 0 and len(self.password.get()) != 0:
                self.cursor.execute("INSERT INTO Accounts VALUES(NULL, ?, ?)", (self.username.get(), self.password.get()))
                self.connection.commit()
                self.username.set("")
                self.password.set("")


                messagebox.showinfo("BBDD", "Record created successfully")
        else:
            messagebox.showwarning("Establish Connection", "There is no connection to the database")


    def query_delete(self):
        if self.connected_database:
            if self.account_id.get() != "AUTOINCREMENT" and len(self.username.get()) != 0 and len(self.password.get()) != 0:
                self.cursor.execute("DELETE FROM Accounts WHERE ID = ?", self.account_id.get())
                self.connection.commit()


                self.account_id.set("AUTOINCREMENT")
                self.username.set("")
                self.password.set("")


                messagebox.showinfo("BBDD", "Record successfully removed")
        else:
            messagebox.showwarning("Establish Connection", "There is no connection to the database")


    def query_update(self):
        if self.connected_database:
            if self.account_id.get() != "AUTOINCREMENT" and len(self.username.get()) != 0 and len(self.password.get()) != 0:
                self.cursor.execute("SELECT * FROM Accounts WHERE ID = ?", self.account_id.get())
                data = self.cursor.fetchall()[0]


                if data != (self.account_id.get(), self.username.get(), self.password.get()):
                    self.cursor.execute("UPDATE Accounts SET USERNAME = ?, PASSWORD = ? WHERE ID = ?", (self.username.get(), self.password.get(), self.account_id.get()))


                    self.connection.commit()
                    messagebox.showinfo("BBDD", "Update completed successfully")
        else:
            messagebox.showwarning("Establish Connection", "There is no connection to the database")


    def query_read(self):
        if self.connected_database:
            window = Toplevel()
            window.resizable(0,0)


            def read_record():
                if len(ID.get()) != 0 and ID.get().isdigit():
                    try:
                        self.cursor.execute("SELECT * FROM Accounts WHERE ID = ?", ID.get())
                        registry = self.cursor.fetchall()[0]


                        self.account_id.set("")
                        self.username.set("")
                        self.password.set("")


                        self.account_id.set(registry[0])
                        self.username.set(registry[1])
                        self.password.set(registry[2])
                        window.destroy()
                    except (IndexError, sqlite3.ProgrammingError):
                        messagebox.showwarning("IndexError", "The record does not exist")


            # Variable of control
            ID = StringVar()


            # Frame
            frame = LabelFrame(window, text = " READ ")
            frame.grid(row = 0, column = 0, pady = 10, padx = 10)


            # Account id
            Label(frame, text = "Registry ID:").grid(row = 0, column = 0, pady = 5, padx = 5)
            Entry(frame, width = 10, textvariable = ID, justify = CENTER).grid(row = 0, column = 1, pady = 5, padx = 5)


            # Button
            Button(frame, text = "OK", command = lambda:read_record()).grid(row = 1, columnspan = 2, sticky = W + E)
        else:
            messagebox.showwarning("Establish Connection", "There is no connection to the database")


DatabaseManagement()