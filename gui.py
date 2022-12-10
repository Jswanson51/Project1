import csv
from tkinter import *
from tkcalendar import Calendar


class GUI:
    """
    A class creating the GUI for the program
    """

    def __init__(self, window) -> None:
        """
        Constructor that creates widgets on the main window
        :param window: The main window
        """

        self.window = window

        self.frame_ID = Frame(self.window, background='#838B8B')
        self.label_ID = Label(self.frame_ID, text='ID', background='#838B8B')
        self.entry_ID = Entry(self.frame_ID)
        self.label_ID.pack(padx=5, side='left')
        self.entry_ID.pack(padx=5, side='left')
        self.frame_ID.pack(anchor='w', pady=10)

        self.frame_age = Frame(self.window, background='#838B8B')
        self.label_age = Label(self.frame_age, text='Age', background='#838B8B')
        self.button_age = Button(self.frame_age, text='Select a date', command=self.calendar_clicked)
        self.label_age.pack(padx=15, side='left')
        self.button_age.pack(padx=15, side='left')
        self.frame_age.pack(anchor='w', pady=10)

        self.frame_username = Frame(self.window, background='#838B8B')
        self.label_username = Label(self.frame_ID, text='Username', background='#838B8B')
        self.entry_username = Entry(self.frame_ID)
        self.label_username.pack(padx=7, side='left')
        self.entry_username.pack(padx=5, side='right')
        self.frame_username.pack(anchor='w', pady=10)

        self.frame_password = Frame(self.window, background='#838B8B')
        self.label_password = Label(self.frame_age, text='Password', background='#838B8B')
        self.entry_password = Entry(self.frame_age)
        self.label_password.pack(padx=5, side='left')
        self.entry_password.pack(padx=3, side='right')
        self.frame_password.pack(anchor='w', pady=10)

        self.frame_status = Frame(self.window, background='#838B8B')
        self.label_status = Label(self.frame_status, text='Status', background='#838B8B')
        self.radio_status = IntVar()
        self.button_status_Student = Radiobutton(self.frame_status, text='Student', variable=self.radio_status, value=1, background='#838B8B')
        self.button_status_Staff = Radiobutton(self.frame_status, text='Staff', variable=self.radio_status, value=2, background='#838B8B')
        self.button_status_Both = Radiobutton(self.frame_status, text='Both', variable=self.radio_status, value=3, background='#838B8B')

        self.label_status.pack(padx=25, side='left' )
        self.button_status_Student.pack(padx=25, side='right')
        self.button_status_Staff.pack(padx=25,side='right')
        self.button_status_Both.pack(padx=25, side='right')
        self.frame_status.pack(anchor='w', pady=10)

        self.frame_bottom = Frame(self.window, background='#838B8B')
        self.button_Save = Button(self.frame_bottom, text='SAVE', command=self.clicked)
        self.button_Save.pack()
        self.frame_bottom.pack()

    def calendar_clicked(self) -> None:
        """
        Method that creates a calendar pop-up gui
        :return: None
        """
        cal_window = Tk()
        cal_window.title('Calendar')
        cal_window.resizable(False,False)

        cal = Calendar(cal_window, selectmode='day', year=2022, month=12, day=9)

        cal.pack(pady=5)

        button_date = Button(cal_window, text="Select Date", command=cal.get_date())

        button_date.pack(pady=15)

        label_date = Label(cal_window, text='')
        label_date.config(text=cal.get_date())
        label_date.pack(pady=15)

    def clicked(self) -> None:
        """
        Method that is triggered by button_save and receives input from entry boxes to write to csv file
        :return: None
        """

        ID = self.entry_ID.get()
        if ID == "":
            raise ValueError('Please enter an ID number')
        elif ID.isnumeric() == False:
            raise ValueError('Please only enter numeric characters for ID')

        username = self.entry_username.get()
        if username == "":
            raise ValueError('Please enter a username')

        password = self.entry_password.get()
        if password == "":
            raise ValueError('Please enter a password')

        if self.radio_status.get() == 1:
            status = 'Student'
        elif self.radio_status.get() == 2:
            status = 'Staff'
        elif self.radio_status.get() == 3:
            status = 'Both'
        else:
            raise ValueError('Please select a status.')

        with open('records.csv', 'r') as csvreader:
            ID_list = {line[0]: line[3] for line in csv.reader(csvreader)}

            with open('records.csv', 'a', newline='') as csvfile:
                content = csv.writer(csvfile)
                line = ID_list.get(ID)

                if line:
                    if username in ID_list.values():
                        print('Successful Login')
                    else:
                        print('Invalid Username')
                else:
                    print('New User')
                    content.writerow([ID, status, username, password])

        self.entry_ID.delete(0, END)
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        self.radio_status.set(0)
