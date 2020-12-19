from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])
    e5.delete(0, END)
    e5.insert(END, selected_tuple[5])
    e6.delete(0, END)
    e6.insert(END, selected_tuple[6])


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(name_text.get(), address_text.get(), phone_number_text.get(), room_type_text.get(), no_of_days_text.get(), amount_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(name_text.get(), address_text.get(), phone_number_text.get(
    ), no_of_days_text.get(), room_type_text.get(), amount_text.get())
    list1.delete(0, END)
    list1.insert(END, (name_text.get(), address_text.get(), phone_number_text.get(
    ), no_of_days_text.get(), room_type_text.get(), amount_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], name_text.get(), address_text.get(
    ), phone_number_text.get(), room_type_text.get(), no_of_days_text.get(), amount_text.get())


window = Tk()

window.wm_title("HOTEL ROYZ")

l5 = Label(window, text="HOTEL ROYZZ")
l5.grid(row=0, column=2)

l1 = Label(window, text="NAME")
l1.grid(row=1, column=0)

l2 = Label(window, text="ADRRESS")
l2.grid(row=2, column=0)

l3 = Label(window, text="PHONE NUMBER")
l3.grid(row=3, column=0)

l4 = Label(window, text="NUMBER OF DAYS YOU WANT TO STAY IN ")
l4.grid(row=4, column=0)

l6 = Label(window, text="ROOM TYPE(norml,king and delux )")
l6.grid(row=5, column=0)

l7 = Label(window, text="YOUR TOTAL AMOUNT(NO NEED TO BE FILLED) ")
l7.grid(row=6, column=0)

name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=1, column=1)

address_text = StringVar()
e2 = Entry(window, textvariable=address_text)
e2.grid(row=2, column=1)

phone_number_text = StringVar()
e3 = Entry(window, textvariable=phone_number_text)
e3.grid(row=3, column=1)

no_of_days_text = StringVar()
e4 = Entry(window, textvariable=no_of_days_text)
e4.grid(row=4, column=1)

room_type_text = StringVar()
e5 = Entry(window, textvariable=room_type_text)
e5.grid(row=5, column=1)

amount_text = StringVar()
e6 = Entry(window, textvariable=amount_text)
e6.grid(row=6, column=1)

list1 = Listbox(window, height=20, width=59)
list1.grid(row=1, column=3, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=1, column=2, sticky='ns', rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=7, column=0)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=7, column=1)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=8, column=0)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=8, column=1)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=10, column=0)

window.mainloop()
