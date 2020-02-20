##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.title("Authorization")

def test_my_button():
    frame_auth.tkraise()

    password = ent_Password.get()
    lbl_Password.config(text = password)




# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row = 0, column = 0,sticky="news")

lbl_username = tk.Label(frame_login, text='Username:',font="comic_sans")
lbl_username.pack(pady=10)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_Password = tk.Label(frame_login, text='Password:',font="corrier")
lbl_Password.pack(padx=50)

ent_Password = tk.Entry(frame_login, bd=3, show='*')
ent_Password.pack(pady=5)

frame_auth = tk.Frame(root)
frame_auth.grid(row = 0, column = 0,sticky="news")



btn_login = tk.Button(frame_login, text='Login:',font="comic_sans",command = test_my_button)
btn_login.pack()

lbl_Password = tk.Label(frame_auth)
lbl_Password.pack()

frame_login.tkraise()
root.mainloop()