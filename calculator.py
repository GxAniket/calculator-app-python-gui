import tkinter as tk
from tkinter import messagebox

# Main application window
root = tk.Tk()
root.title("Calculator made with Aniket ")
root.geometry("350x500")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# Global expression variable
expression = ""

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except ZeroDivisionError:
        input_text.set("Error: Division by 0")
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

# Clear the input
def clear():
    global expression
    expression = ""
    input_text.set("")

# Input text variable
input_text = tk.StringVar()

# Display frame
frame = tk.Frame(root, bg="#2d2d44")
frame.pack(expand=True, fill="both")

# Input field
input_field = tk.Entry(frame, textvariable=input_text, font=("Arial", 24), bg="#1e1e2f", fg="#ffffff", bd=0, justify="right")
input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, padx=10, pady=20, sticky="we")

# Button style
btn_style = {
    "font": ("Arial", 18),
    "bd": 0,
    "bg": "#3e3e5e",
    "fg": "#ffffff",
    "activebackground": "#54bc48",
    "activeforeground": "#ffffff",
    "width": 4,
    "height": 2
}

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

# Create buttons dynamically
for (text, row, col, colspan) in [(*btn, 1) if len(btn) == 3 else btn for btn in buttons]:
    action = lambda x=text: press(x) if x not in ('=', 'C') else (equalpress() if x == '=' else clear())
    tk.Button(frame, text=text, command=action, **btn_style).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# Make rows/columns expand with window (optional)
for i in range(6):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

# Start the GUI
root.mainloop()