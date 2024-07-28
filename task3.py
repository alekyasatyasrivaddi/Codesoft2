import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        
        # Define the character sets for the password
        characters = ""
        if var_lowercase.get():
            characters += string.ascii_lowercase
        if var_uppercase.get():
            characters += string.ascii_uppercase
        if var_digits.get():
            characters += string.digits
        if var_special.get():
            characters += string.punctuation
        
        if not characters:
            raise ValueError("At least one character type must be selected.")
        
        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the password
        label_result.config(text=f"Generated Password: {password}")
        # Enable the Copy button
        button_copy.config(state=tk.NORMAL)
        # Store the password in a global variable for copying
        global generated_password
        generated_password = password
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(generated_password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the main window
app = tk.Tk()
app.title("Password Generator")

# Define colors
bg_color = '#f0f0f0'  # Light grey background for the main window
btn_color = '#4CAF50'  # Green background for buttons
text_color = '#000000'  # Black text color

# Set background color of the main window
app.configure(bg=bg_color)

# Define a larger font for widgets
large_font = ('Arial', 14)

# Length Input
label_length = tk.Label(app, text="Enter desired password length:", font=large_font, bg=bg_color, fg=text_color)
label_length.pack(pady=10)
entry_length = tk.Entry(app, font=large_font, width=20, bg='white', fg=text_color)
entry_length.pack(pady=10)

# Options for Complexity
var_lowercase = tk.BooleanVar()
var_lowercase.set(True)  # Default value
checkbox_lowercase = tk.Checkbutton(app, text="Include Lowercase Letters", variable=var_lowercase, font=large_font, bg=bg_color, fg=text_color, selectcolor=btn_color)
checkbox_lowercase.pack(pady=5)

var_uppercase = tk.BooleanVar()
var_uppercase.set(True)  # Default value
checkbox_uppercase = tk.Checkbutton(app, text="Include Uppercase Letters", variable=var_uppercase, font=large_font, bg=bg_color, fg=text_color, selectcolor=btn_color)
checkbox_uppercase.pack(pady=5)

var_digits = tk.BooleanVar()
var_digits.set(True)  # Default value
checkbox_digits = tk.Checkbutton(app, text="Include Digits", variable=var_digits, font=large_font, bg=bg_color, fg=text_color, selectcolor=btn_color)
checkbox_digits.pack(pady=5)

var_special = tk.BooleanVar()
var_special.set(True)  # Default value
checkbox_special = tk.Checkbutton(app, text="Include Special Characters", variable=var_special, font=large_font, bg=bg_color, fg=text_color, selectcolor=btn_color)
checkbox_special.pack(pady=5)

# Generate Button
button_generate = tk.Button(app, text="Generate Password", command=generate_password, font=large_font, width=20, bg=btn_color, fg='white')
button_generate.pack(pady=15)

# Copy Button
button_copy = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard, font=large_font, width=20, bg=btn_color, fg='white', state=tk.DISABLED)
button_copy.pack(pady=15)

# Result Label
label_result = tk.Label(app, text="Generated Password: ", font=large_font, bg=bg_color, fg=text_color)
label_result.pack(pady=10)

# Store the generated password
generated_password = ""

# Run the main event loop
app.mainloop()
