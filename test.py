import tkinter as tk

def on_enter_pressed(event):
    """Handle ENTER key press event."""
    # Perform actions when ENTER key is pressed
    text = entry_var.get()
    print("Entered text:", text)
    # You can add further actions here

root = tk.Tk()

# Create a StringVar
entry_var = tk.StringVar()

# Function to handle changes to the StringVar
def on_entry_change(*args):
    """Handle changes to the Entry field."""
    print("Entry changed to:", entry_var.get())

# Attach StringVar to Entry field
entry = tk.Entry(root, textvariable=entry_var)
entry.pack()

# Add a trace to detect changes in the StringVar
entry_var.trace_add("write", on_entry_change)

# Bind ENTER key press event
entry.bind("<Return>", on_enter_pressed)

root.mainloop()
