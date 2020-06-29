import tkinter as tk

def shutdown():
   import subprocess
   subprocess.call(['shutdown', '-f', '-s', '-t', a.get()])

def restart():
   import subprocess
   subprocess.call(['shutdown', '-f', '-r', '-t', a.get()])

 

window = tk.Tk()
window.title('Shutdown timer')

back = tk.Frame(master=window, width=500, height=400, bg='#37d3ff')
back.pack()

btn1 = tk.Button(master=back, text='Shut down', command=shutdown).place(relx=0.14, rely=0.300, height=30, relwidth=0.700)
btn2 = tk.Button(master=back, text='Restart', command=restart).place(relx=0.14, rely=0.400, height=30, relwidth=0.700)
btn3 = tk.Button(master=back, text='Quit').place(relx=0.14, rely=0.500, height=30, relwidth=0.700)

info = tk.Label(master=back, text='If you want to control your PC, do it!!!', bg='#37d3ff').place(relx=0.24, rely=0.200, height=30, relwidth=0.500)

a = tk.StringVar()
entry = tk.Entry(textvariable=a).place(relx=0.45, rely=0.600, height=30, width=120)
info = tk.Label(master=back, text='Put time:', bg='#37d3ff').place(relx=0.30, rely=0.604)
window.mainloop()