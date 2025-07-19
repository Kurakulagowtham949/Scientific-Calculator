import tkinter as tk
import math

expression = ""

# ===== Functions =====

def update_expression(value):
    global expression
    expression += value
    entry_var.set(expression)

def clear_expression():
    global expression
    expression = ""
    entry_var.set("")

def backspace():
    global expression
    expression = expression[:-1]
    entry_var.set(expression)

def evaluate_expression():
    global expression
    try:
        exp = expression.replace("sin", "math.sin")\
                        .replace("cos", "math.cos")\
                        .replace("tan", "math.tan")\
                        .replace("log", "math.log10")\
                        .replace("sqrt", "math.sqrt")
        result = str(eval(exp))
        entry_var.set(result)
        expression = result
    except:
        entry_var.set("Error")
        expression = ""

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        evaluate_expression()
    elif text == "C":
        clear_expression()
    elif text == "⌫":
        backspace()
    else:
        update_expression(text)

def on_key_press(event):
    key = event.char
    if key in "0123456789+-*/().":
        update_expression(key)
    elif event.keysym == "Return":
        evaluate_expression()
    elif event.keysym == "BackSpace":
        backspace()

# ===== GUI Setup =====

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("380x580")
root.resizable(False, False)
root.bind("<Key>", on_key_press)

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font="Arial 22", justify="right", bd=10, relief="sunken")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=10, padx=10)

# ===== Button Layout =====

button_layout = [
    ["sin(", "cos(", "tan(", "log("],
    ["sqrt(", "(", ")", "⌫"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["=",]
]

# ===== Button Colors =====

colors = {
    "C": "red", "=": "green", "+": "orange", "-": "orange",
    "*": "orange", "/": "orange", "⌫": "lightgray",
    "sin(": "lightblue", "cos(": "lightblue", "tan(": "lightblue",
    "log(": "lightblue", "sqrt(": "lightblue"
}

# ===== Create Buttons =====

for row in button_layout:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        color = colors.get(btn_text, "white")
        btn = tk.Button(frame, text=btn_text, font="Arial 18", bg=color, relief="raised", bd=2)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", on_button_click)

root.mainloop()
