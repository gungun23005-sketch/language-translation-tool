from tkinter import *
from deep_translator import GoogleTranslator

def translate_text():
    text = input_text.get("1.0", END)

    translated = GoogleTranslator(
        source='auto',
        target=target_lang.get()
    ).translate(text)

    output_text.delete("1.0", END)
    output_text.insert(END, translated)

root = Tk()
root.title("Language Translation Tool")
root.geometry("700x500")

Label(root, text="Enter Text", font=("Arial", 12)).pack()

input_text = Text(root, height=6, width=60)
input_text.pack(pady=10)

Label(root, text="Target Language Code").pack()

target_lang = StringVar()
target_lang.set("hi")

Entry(root, textvariable=target_lang).pack()

Button(root, text="Translate", command=translate_text).pack(pady=10)

Label(root, text="Translated Text", font=("Arial", 12)).pack()

output_text = Text(root, height=6, width=60)
output_text.pack(pady=10)

root.mainloop()