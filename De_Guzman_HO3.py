import tkinter as ari
window = ari.Tk()
window.title("Ariana-G")
window.configure(bg = "#769174")
label = ari.Label(window, text = "Simple Calculator", font = ("times new roman", 15, "bold"),bg = "#769174", fg = "white")
label.grid(column = 0, row = 0, padx = 50, pady = 10, columnspan = 3)

def ariana():
    num1 = int(first_entry.get())
    num2 = int(sec_entry.get())
    sum = num1 + num2
    label = ari.Label(window, text = f"The sum of {num1} and {num2} is {sum}.", font = ("times new roman", 15, "bold"), bg = "#769174", fg = "white")
    label.grid(column = 0, row = 0, columnspan = 3)
def grande():
    num1 = int(first_entry.get())
    num2 = int(sec_entry.get())
    dif = num1 - num2
    label = ari.Label(window, text = f"The difference of {num1} and {num2} is {dif}.", font = ("times new roman", 15, "bold"), bg = "#769174", fg = "white")
    label.grid(column = 0, row = 0, columnspan = 3)
def sabrina():
    num1 = int(first_entry.get())
    num2 = int(sec_entry.get())
    prod = num1 * num2
    label = ari.Label(window, text = f"The product of {num1} and {num2} is {prod}.", font = ("times new roman", 15, "bold"), bg = "#769174", fg = "white")
    label.grid(column = 0, row = 0, columnspan = 3)
def carpenter():
    num1 = int(first_entry.get())
    num2 = int(sec_entry.get())
    quot = num1 / num2
    label = ari.Label(window, text = f"The quotient of {num1} and {num2} is {quot}.", font = ("times new roman", 15, "bold"), bg = "#769174", fg = "white")
    label.grid(column = 0, row = 0, columnspan = 3)

first = ari.Label(window, text = "Enter a number:", font = ("times new roman", 15), bg = "#769174", )
first.grid(column = 0, row = 1)
first_entry = ari.Entry(window, width = 20)
first_entry.grid(column = 1, row = 1, columnspan = 2)
sec = ari.Label(window, text = "Enter a number:", font = ("times new roman", 15), bg = "#769174", )
sec.grid(column = 0, row = 2)
sec_entry = ari.Entry(window, width = 20)
sec_entry.grid(column = 1, row = 2, columnspan = 2)

add_btn = ari.Button(window, text = "ADD", width = 10, bg = "#aec6a5", command = ariana)
add_btn.grid(column = 0, row = 3, pady = 10)
sub_btn = ari.Button(window, text = "SUBTRACT", width = 10, bg = "#aec6a5", command = grande)
sub_btn.grid(column = 1, row = 3, pady = 10)
mul_btn = ari.Button(window, text = "MULTIPLY", width = 10, bg = "#aec6a5", command = sabrina)
mul_btn.grid(column = 0, row = 4, pady = 10)
div_btn = ari.Button(window, text = "DIVIDE", width = 10, bg = "#aec6a5", command = carpenter)
div_btn.grid(column = 1, row = 4, pady = 10)

window.mainloop()