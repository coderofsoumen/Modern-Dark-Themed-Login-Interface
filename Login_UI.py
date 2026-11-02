import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Account Login")
root.geometry("420x540")
root.resizable(False, False)
root.configure(bg="#1E1E2E")


def handle_login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning("Missing Fields", "Please enter both username and password.")
        return

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", f"Welcome back, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


card_frame = tk.Frame(root, bg="#2A2A3E", padx=30, pady=35)
card_frame.pack(padx=30, pady=40, fill="both", expand=True)

badge_label = tk.Label(
    card_frame,
    text="✦",
    font=("Segoe UI", 28),
    fg="#89B4FA",
    bg="#2A2A3E"
)
badge_label.pack(pady=(0, 5))

title_label = tk.Label(
    card_frame,
    text="Welcome Back",
    font=("Segoe UI", 18, "bold"),
    fg="#CDD6F4",
    bg="#2A2A3E"
)
title_label.pack()

subtitle_label = tk.Label(
    card_frame,
    text="Enter your credentials to continue",
    font=("Segoe UI", 9),
    fg="#A6ADC8",
    bg="#2A2A3E"
)
subtitle_label.pack(pady=(4, 25))

username_label = tk.Label(
    card_frame,
    text="USERNAME",
    font=("Segoe UI", 8, "bold"),
    fg="#BAC2DE",
    bg="#2A2A3E",
    anchor="w"
)
username_label.pack(fill="x")

username_entry = tk.Entry(
    card_frame,
    font=("Segoe UI", 11),
    bg="#1E1E2E",
    fg="#CDD6F4",
    insertbackground="#CDD6F4",
    relief="flat",
    highlightthickness=1,
    highlightbackground="#45475A",
    highlightcolor="#89B4FA"
)
username_entry.pack(fill="x", ipady=8, pady=(4, 16))

password_label = tk.Label(
    card_frame,
    text="PASSWORD",
    font=("Segoe UI", 8, "bold"),
    fg="#BAC2DE",
    bg="#2A2A3E",
    anchor="w"
)
password_label.pack(fill="x")

password_entry = tk.Entry(
    card_frame,
    font=("Segoe UI", 11),
    show="•",
    bg="#1E1E2E",
    fg="#CDD6F4",
    insertbackground="#CDD6F4",
    relief="flat",
    highlightthickness=1,
    highlightbackground="#45475A",
    highlightcolor="#89B4FA"
)
password_entry.pack(fill="x", ipady=8, pady=(4, 25))

login_button = tk.Button(
    card_frame,
    text="Log In",
    font=("Segoe UI", 11, "bold"),
    bg="#89B4FA",
    fg="#11111B",
    activebackground="#B4BEFE",
    activeforeground="#11111B",
    relief="flat",
    cursor="hand2",
    command=handle_login
)
login_button.pack(fill="x", ipady=8)

root.bind("<Return>", lambda event: handle_login())

root.mainloop()