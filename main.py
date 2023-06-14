from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250,height=150)
window.config(padx=20,pady=20)
def km_lab():
    x = float(mile_entry.get())
    res = round(x*1.609,1)
    result_label.config(text=f"{res}")
#Entry
def del_text(a):
    mile_entry.delete(0,"end")
mile_entry = Entry(width=10)
mile_entry.insert(END,"Enter miles")
mile_entry.bind("<FocusIn>", del_text)
mile_entry.grid(column=1,row=0)
#mile label
mile_label = Label(text=" Miles")
mile_label.grid(column=2,row=0)
# is_equal_label
is_equal = Label(text="is equal to ")
is_equal.grid(column=0,row=1)
# Result_label
result_label =Label(text = "0")
result_label.grid(column=1 ,row=1)
# km_label
km_label = Label(text = " Km")
km_label.grid(column=2,row=1)
# cal_button
cal_button = Button(text="Calculate",command=km_lab)
cal_button.grid(column=1,row=2)
window.mainloop()
