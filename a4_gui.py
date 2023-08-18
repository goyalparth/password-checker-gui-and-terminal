import tkinter

class myGui():
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.title('Password Tracker')
        self.password_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()
        

        password_label = tkinter.Label(self.password_frame, text = "Enter a string for password: ")
        self.password_entry = tkinter.Entry(self.password_frame, bg = 'light blue', bd = 2 ,width = '20')
        password_label.pack(side = 'left')
        self.password_entry.pack(side = 'left')

        calc_button = tkinter.Button(self.button_frame, text = 'Check Validity', command = self.check_password)
        calc_button.pack(side = 'left')
        quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        quit_button.pack(side='left')

        self.result_ta = tkinter.Text(self.result_frame, bg = 'light blue', height = 10, width = 35)
        self.result_ta.pack()
        
        self.password_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()

        tkinter.mainloop()

    def check_password(self):
            
        password = (self.password_entry.get())
        ls_number = list("0123456789")
        ls_alphabets = list("qwertyuiopasdfghjklzxcvbnm")

        digit_count = 0
        ls_password = list(password)

        if len(password)>= 8:
            for i in ls_password:
                if i in ls_alphabets or i in ls_number:
                    if i in ls_number:
                        digit_count += 1
           
                else:
                    result = ("invalid password")
                    break
    
            if digit_count>=2:
                result = ("valid password")
            else:
                result = ("invalid password")
        else:
            result = ("invalid password") 
        
        self.result_ta.insert('1.0',result)
                
my_gui = myGui()
