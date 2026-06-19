from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip

# Translate Function
def translate_text():
    try:
        text = input_box.get("1.0", END).strip()

        if text == "":
            messagebox.showwarning(
                "Warning",
                "Please enter text."
            )
            return

        source_code = languages[source_lang.get()]
        target_code = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=source_code,
            target=target_code
        ).translate(text)

        output_box.delete("1.0", END)
        output_box.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Copy Function
def copy_text():
    translated = output_box.get("1.0", END)

    if translated.strip():
        pyperclip.copy(translated)
        messagebox.showinfo(
            "Success",
            "Translated text copied."
        )

# Clear Function
def clear_text():
    input_box.delete("1.0", END)
    output_box.delete("1.0", END)

# Main Window
root = Tk()
root.title("Language Translation Tool")
root.geometry("900x650")
root.resizable(False, False)

heading = Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 20, "bold")
)

heading.pack(pady=10)

languages = {
    "Auto Detect":"auto",
    "English":"en",
    "Hindi":"hi",
    "French":"fr",
    "German":"de",
    "Spanish":"es",
    "Japanese":"ja",
    "Korean":"ko",
    "Chinese":"zh-CN"
}

frame = Frame(root)
frame.pack(pady=10)

Label(
    frame,
    text="Source Language",
    font=("Arial",12)
).grid(row=0,column=0,padx=20)

source_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    width=20
)

source_lang.grid(row=1,column=0,padx=20)
source_lang.set("Auto Detect")

Label(
    frame,
    text="Target Language",
    font=("Arial",12)
).grid(row=0,column=1,padx=20)

target_lang = ttk.Combobox(
    frame,
    values=list(languages.keys())[1:],
    width=20
)

target_lang.grid(row=1,column=1,padx=20)
target_lang.set("Hindi")

Label(
    root,
    text="Enter Text",
    font=("Arial",12,"bold")
).pack()

input_box = Text(
    root,
    height=10,
    width=90,
    font=("Arial",11)
)

input_box.pack(pady=5)

Button(
    root,
    text="Translate",
    font=("Arial",12,"bold"),
    command=translate_text
).pack(pady=10)

Label(
    root,
    text="Translated Text",
    font=("Arial",12,"bold")
).pack()

output_box = Text(
    root,
    height=10,
    width=90,
    font=("Arial",11)
)

output_box.pack(pady=5)

button_frame = Frame(root)
button_frame.pack(pady=10)

Button(
    button_frame,
    text="Copy Text",
    width=15,
    command=copy_text
).grid(row=0,column=0,padx=10)

Button(
    button_frame,
    text="Clear",
    width=15,
    command=clear_text
).grid(row=0,column=1,padx=10)

root.mainloop()