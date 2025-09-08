import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")
root.geometry("400x200")

text1 = tk.StringVar(value="Hello, Tkinter!")
text2 = tk.StringVar(value="Click the button")

label1 = tk.Label(root, textvariable=text1, font=("Arial", 16))
label1.pack(pady=20)

label2 = tk.Label(root, textvariable=text2, font=("Arial", 14))
label2.pack(pady=10)

def say_hello():
    text2.set("Button Clicked!")

button = tk.Button(root, text="Click me", command=say_hello)
button.pack(pady=10)

root.mainloop()
