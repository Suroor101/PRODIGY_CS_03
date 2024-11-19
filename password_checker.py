import tkinter as tk
from tkinter import messagebox

# Load common passwords from a file to check against (if available)
def load_common_passwords(file_path):
    try:
        with open(file_path, "r") as file:
            return set(line.strip().lower() for line in file)  # Return set of common passwords
    except FileNotFoundError:
        messagebox.showinfo("Info", "Common password list not found, proceeding without it.")
        return set()  # Return empty set if file is not found

# Function to assess password strength based on various criteria
def assess_password_strength(password):
    strength = 0  # Start with 0 strength
    feedback = []  # Collect feedback for the user

    # Immediate check for passwords shorter than 6 characters (weak)
    if len(password) < 6:
        return "Weak", ["Password should be at least 6 characters long."]

    # Check if password is too common (if common passwords list is available)
    if password.lower() in common_passwords:
        feedback.append("This password is too common. Choose a more unique one.")
        return "Weak", feedback

    # Criteria for password strength
    if len(password) >= 8:
        strength += 1  # 8 or more characters
    elif len(password) >= 6:
        strength += 1  # 6 to 7 characters (moderate)

    # Check for lowercase, uppercase, digits, and special characters
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if any(char in "!@#$%^&*()-_+=<>?/{}~" for char in password):
        strength += 1
    else:
        feedback.append("Use at least one special character.")

    # Determine the strength based on the accumulated score
    if strength <= 2:
        strength_level = "Weak"
    elif strength == 3 or len(password) < 8:
        strength_level = "Moderate"
    else:
        strength_level = "Strong"

    return strength_level, feedback

# Function to check password strength when the user clicks "Check Strength"
def check_password():
    password = password_entry.get()  # Get password input
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")  # Show warning if input is empty
        return

    # Assess the password's strength
    strength, feedback = assess_password_strength(password)
    feedback_message = "\n".join(feedback) if feedback else "Great job! Your password is strong."

    # Display the results
    result_label.config(text=f"Password Strength: {strength}", fg="green" if strength == "Strong" else "red")
    feedback_label.config(text=f"Feedback:\n{feedback_message}")

# Function to toggle the visibility of the password input
def toggle_password_visibility():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        toggle_button.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        toggle_button.config(text="Show Password")

# Function to clear the input and result fields
def clear_fields():
    password_entry.delete(0, tk.END)  # Clear the password input field
    result_label.config(text="")  # Clear the result label
    feedback_label.config(text="")  # Clear the feedback label

# Create the main application window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x400")

# Load common passwords from a file (update with your file path)
common_passwords = load_common_passwords("common_passwords.txt")

# Create the password input field
tk.Label(root, text="Enter your password:").pack(pady=10)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack()

# Toggle visibility of the password field
toggle_button = tk.Button(root, text="Show Password", command=toggle_password_visibility)
toggle_button.pack(pady=5)

# Buttons for actions (check strength, clear)
tk.Button(root, text="Check Strength", command=check_password).pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)

# Labels to display results and feedback
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

feedback_label = tk.Label(root, text="", wraplength=350, justify="left")
feedback_label.pack(pady=10)

# Run the application
root.mainloop()
