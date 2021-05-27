from tkinter import *
from Help import *
from patient import *
flag=0
user_logged_in=False
def register_login_main():
    global main_screen
    main_screen = Tk()  # create a GUI window
    main_screen.geometry("300x250")  # set the configuration of GUI window
    main_screen.title("Account Login")  # set the title of GUI window

    # create a Form label
    Label(text="Welcome our system\nChoose Login Or Register", bg="light green", width="50", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    # create a login button
    Button(text="login",bg="light green", height="2", width="30", command=login).pack()
    Label(text="").pack()


    # create a register button
    Button(text="Register",bg="light green", height="2", width="30", command=register).pack()
    main_screen.mainloop()  # start the GUI

def register():
    global register_screen
    register_screen=Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x350")
    global username,password,username_entry,password_entry,password_confirmation_entry,password_confirmation,id,id_entry
    username=StringVar()
    password=StringVar()
    password_confirmation=StringVar()
    id=StringVar()

    Label(register_screen,text="please enter details below").pack()



    #username entry
    Label(register_screen,text="").pack()
    Label(register_screen,text="username * ").pack()
    username_entry=Entry(register_screen,textvariable=username)
    username_entry.pack()


    #id entry
    Label(register_screen, text="").pack()
    Label(register_screen, text="Id * ").pack()
    id_entry=Entry(register_screen, textvariable=id)
    id_entry.pack()

    #password entry
    Label(register_screen, text="").pack()
    Label(register_screen, text="Password * ").pack()
    password_entry=Entry(register_screen, textvariable=password,show='*')
    password_entry.pack()

    #password confirmation entry
    Label(register_screen, text="").pack()
    Label(register_screen, text="Password confirmation * ").pack()
    password_confirmation_entry=Entry(register_screen, textvariable=password_confirmation,show='*')
    password_confirmation_entry.pack()




    Label(register_screen, text="").pack()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    password_confirmation_entry.delete(0, END)
    id_entry.delete(0, END)
    Button(register_screen,bg="light green",text="Register",width=10,height=1,command=register_user).pack()

def register_user():
    global flag
    error=False
    username_info=username.get()
    password_info=password.get()
    password_confirmation_info=password_confirmation.get()
    id_info=id.get()
    if password_match(password_confirmation_info,password_info)==False:
        error=True
        password_confirmation_error()

    if password_as_reuirements(password_info)==False:
        error=True
        password_register_error()


    elif username_as_requirements(username_info)==False:
        error=True
        username_register_error()
    if(len(id_info))!=9:
        error=True
        id_register_error_screen()


    if error==False:
        if flag==0:
            flag=1
            file=open("Doctors"+".txt","a")
            file.write(username_info+" "+ password_info + " "+ id_info+"\n")
            file.close()

        else:
            file = open("Doctors" + ".txt", "a")
            file.write("\n" +username_info + " " + password_info+ " "+ id_info+"\n")
            file.close()


        #clear the register label
        username_entry.delete(0,END)
        password_entry.delete(0,END)
        password_confirmation_entry.delete(0,END)
        id_entry.delete(0,END)

        Label(register_screen,text="Registration sucess",fg="green",font=("calibri",11)).pack()
        flag=0




#window ups when the passwords does not match
def password_confirmation_error():
    global password_confirmation_error_screen
    password_confirmation_error_screen = Toplevel(register_screen)
    password_confirmation_error_screen.title("Error")
    password_confirmation_error_screen.geometry("250x150")
    Label(password_confirmation_error_screen, text="Passwords does not match", fg="red", font=("Calibri", 13)).pack()
    Button(password_confirmation_error_screen, bg="light green", text="Ok", width=10, height=5, command=close_password_confirmation_error_screen).pack()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    password_confirmation_entry.delete(0, END)
    id_entry.delete(0, END)





def password_register_error():
    global password_register_error_screen
    password_register_error_screen = Toplevel(register_screen)
    password_register_error_screen.title("Error")
    password_register_error_screen.geometry("250x150")
    Label(password_register_error_screen, text="Password not as requirments", fg="red", font=("Calibri", 13)).pack()
    Button(password_register_error_screen, bg="light green", text="Ok", width=10, height=5, command=close_password_register_error_screen).pack()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    password_confirmation_entry.delete(0, END)
    id_entry.delete(0, END)


def username_register_error():
    global username_register_error_screen
    username_register_error_screen = Toplevel(register_screen)
    username_register_error_screen.title("Error")
    username_register_error_screen.geometry("250x150")
    Label(username_register_error_screen, text="Username not as requirments", fg="red", font=("Calibri", 13)).pack()
    Button(username_register_error_screen, bg="light green", text="Ok", width=10, height=5, command=close_username_register_error_screen).pack()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    password_confirmation_entry.delete(0, END)
    id_entry.delete(0, END)

def id_register_error():
    global id_register_error_screen
    id_register_error_screen = Toplevel(register_screen)
    id_register_error_screen.title("Error")
    id_register_error_screen.geometry("250x150")
    Label(id_register_error_screen, text="Your id does not include 9 digits", fg="red", font=("Calibri", 13)).pack()
    Button(id_register_error_screen, bg="light green", text="Ok", width=10, height=5, command=close_id_register_error_screen).pack()

#close the register password error screen
def close_password_confirmation_error_screen():
    password_confirmation_error_screen.destroy()

#close the register password error screen
def close_password_register_error_screen():
    password_register_error_screen.destroy()

#close the register username error screen
def close_password_confirmation_error_screen():
    password_confirmation_error_screen.destroy()

# close the register id error screen
def close_id_register_error_screen():
    id_register_error_screen.destroy()

# close the register username error screen
def close_username_register_error_screen():
    username_register_error_screen.destroy()

def login():
    global login_screen
    login_screen=Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x300")
    Label(login_screen,text="Please enter details below to login").pack()
    Label(login_screen,text="").pack()

    global username_verify_login,password_verify_login,id_verify_login
    global username_entry_login,password_entry_login,id_entry_login

    username_verify_login=StringVar()
    password_verify_login =StringVar()
    id_verify_login=StringVar()


    Label(login_screen, text="").pack()
    Label(login_screen, text="username * ").pack()
    username_entry_login = Entry(login_screen, textvariable=username_verify_login)
    username_entry_login.pack()


    # password entry
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_entry_login = Entry(login_screen, textvariable=password_verify_login, show='*')
    password_entry_login.pack()

    #id entry
    Label(login_screen, text="").pack()
    Label(login_screen, text="Id * ").pack()
    id_entry_login = Entry(login_screen, textvariable=id_verify_login)
    id_entry_login.pack()

    Label(login_screen,text="").pack()
    Button(login_screen,text="Login",bg="light green",width=10,height=1,command=login_verify).pack()


def login_verify():
    username1=username_verify_login.get()
    password1=password_verify_login.get()
    id1=id_verify_login.get()

    username_entry_login.delete(0,END)
    password_entry_login.delete(0,END)
    id_entry_login.delete(0,END)

    file=open("Doctors.txt","r")
    login_sucess=False
    username_found=False
    password_found=False
    id_found=False


    for line in file.readlines():
        login_info=line.split()
        if username1==login_info[0]:
            username_found=True
            if password1 == login_info[1] and id1 == login_info[2]:
                login_sucess=True
                username_found=True
                password_found=True
                id_found=True
                break
            elif password1 != login_info[1] or id1 != login_info[2]:
                if password1!=login_info[1]:
                    password_found=False
                    id_found=True
                if id1!=login_info[2]:
                    id_found=False
                    password_found=False
                break


    if username_found==False:
        Label(login_screen, text="Username is not exist!", fg="red", font=("calibri", 11)).pack()
        Label(login_screen, text="").pack()


    else:
        if password_found==False:
            Label(login_screen, text="Incorrect password!", fg="red", font=("calibri", 11)).pack()
            Label(login_screen, text="").pack()
        if id_found==False:
            Label(login_screen, text="Incorrect id!", fg="red", font=("calibri", 11)).pack()
            Label(login_screen, text="").pack()
        if login_sucess==True:
            login_sucess_screen()


# Test for login faild screen
def login_sucess_screen():
     global user_logged_in
     user_logged_in=True
     global login_sucess_screen
     login_sucess_screen=Toplevel(login_screen)
     login_sucess_screen.title("Login sucess")
     login_sucess_screen.geometry("300x250")
     Label(login_sucess_screen,text="Welcome Doctor").pack()
     Label(login_sucess_screen,text="").pack()
     Button(login_sucess_screen,text="Close", bg="light green", height="2", width="30", command=close_login_sucess_screen).pack()

def close_login_sucess_screen():
    login_sucess_screen.withdraw()
    login_screen.withdraw()
    main_screen.withdraw()
    doctor()


def doctor():
    global doctor_screen
    doctor_screen=Toplevel(login_sucess_screen)
    doctor_screen.geometry("300x250")
    doctor_screen.title("patient")
    Label(doctor_screen, text="Add patient and start the diagnosis").pack()
    Label(login_sucess_screen, text="").pack()
    Button(doctor_screen,text="Add patient", bg="light green", height="2", width="30",command=add_patient).pack()














register_login_main()