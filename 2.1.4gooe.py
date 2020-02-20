import tkinter as tk

root = tk.Tk()
root.grid()


blue = tk.Canvas(height = 100, width = 125,bg= "blue")
blue.grid(row = 0, column =0)


green = tk.Canvas(height = 100, width = 100,bg= "green")
green.grid(row = 0, column =1)



orange = tk.Canvas(height = 100, width = 125,bg= "orange")
orange.grid(row = 1, column =0)


yellow = tk.Canvas(height = 100, width = 100,bg= "yellow")
yellow.grid(row = 1, column =1)

root.wm_geometry("200x200")
root.mainloop()