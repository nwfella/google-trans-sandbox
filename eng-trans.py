from translate import Translator
import tkinter as tk
from tkinter import ttk

# Tkinter window genesis
root = tk.Tk()
root.title("Google Translate")

# input text label
input_label = tk.Label(root, text="Enter text to translate:")
input_label.pack()

# Create entry field for user text
input_entry = tk.Entry(root, width=50)
input_entry.pack()

# Create output text label
output_label = tk.Label(root, text="Translated text:")
output_label.pack()

# Text box for output text genesis
output_text = tk.Text(root, height=10)
output_text.pack()

# Perform the actual translation
def translate_text():
    # Pull text from input_entry field
    input_text = input_entry.get()
    
    # Select destination language dropdown menu
    dest_lang = language_dropdown.get()
    
    # Create translator object using destination language
    translator = Translator(to_lang=dest_lang)
    
    # Perform the actual translation
    translated_text = translator.translate(input_text)
    
    # Clear the output text box and insert the translated text
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, translated_text)

# Create a button to perform the translation
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Language dropdown label
language_label = tk.Label(root, text="Select destination language:")
language_label.pack()

# Define list of available languages
languages = ['ru', 'de', 'fr', 'he', 'zh']

# Define dropdown menu of languages
language_dropdown = ttk.Combobox(root, values=languages)
language_dropdown.pack()

# English default
language_dropdown.current(0)

# Tkinter event loop
root.mainloop()
