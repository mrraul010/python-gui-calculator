
#Calculator Gui For fun

import  tkinter as tk


def click(event):
    current=display.get()
    text=event.widget.cget('text')

    if text == "=" :
      try:
          result=eval(current)
          display.delete(0,tk.END)
          display.insert(tk.END,result)
      except ZeroDivisionError:
          display.delete(0,tk.END)
          display.insert(tk.END,"Cannot Divide by 0")
      except Exception:
          display.delete(0,tk.END)
          display.insert(tk.END,"Syntax Error")
    elif text == "clr":
         display.delete(0,tk.END)
    else :
          display.insert(tk.END,text)


window=tk.Tk()

window.title("Calculator")

window.geometry("400x500")

window.grid_rowconfigure(0,weight=0)
window.grid_rowconfigure(1,weight=1)
window.grid_columnconfigure(0,weight=1)

display=tk.Entry(window,font=("Arial",25),justify="right")
display.grid(row=0,column=0,sticky="ew",padx=10,pady=10,ipady=10)

# display.pack(fill=tk.X,padx=10,pady=10,ipady=10)

btn_frame=tk.Frame(window)
# btn_frame.pack()
btn_frame.grid(row=1,column=0,sticky="nsew",padx=10,pady=10)

for r in range(4):
    btn_frame.grid_rowconfigure(r,weight=1)
for c in range(4):
    btn_frame.grid_columnconfigure(c,weight=1)


button_labels=[
    "7","8","9","+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "clr", "0", "=", "/",
]

i=0
for label in button_labels:
    button=tk.Button(btn_frame,text=label,font=("Arial",18),padx=20,pady=20)
    button.grid(row=i//4,column=i%4,padx=10,pady=10)
    button.bind("<Button-1>",click)
    i+=1

window.mainloop()