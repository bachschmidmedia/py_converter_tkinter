import time
import os
from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog
import ttk

def add_files():
    window.filenames = filedialog.askopenfilenames(
        title="Select file",
        # filetypes=(
        #     ("jpeg files", "*.jpg"), ("all files", "*.*")
        # )
    )
    for num, name in enumerate(window.filenames, start=1):
        if name not in all_files.get():
            filebox.insert(0, name)


def remove_files():
    selected = filebox.curselection()
    full = all_files.get()

    all_files.set(
        [i for i in full if full.index(i) not in selected]
    )


def get_filename_extension(f):
    return os.path.splitext(f)[1]


def get_filename_without_extension(f):
    return os.path.splitext(f)[0]


def get_timestamp():
    return time.time()


def get_timestamp_string():
    return str(get_timestamp())


def get_filepath(file):
    return os.path.dirname(os.path.abspath(file))


def file_exists(file):
    return os.path.isfile(file)


def get_destination_file(file, typ):
    filename = get_filename_without_extension(file)
    path = get_filepath(file)
    dst = os.path.join(file, "{}.{}".format(filename, typ))

    # If File already exists, add timestamp
    if file_exists(dst):
        dst = os.path.join(
            path,
            "{}-{}.{}".format(filename, get_timestamp_string(), typ)
        )

    return dst


def empty_file_list():
    global all_files
    all_files.set([])


def set_result_list(results):
    result_list.set(results)


def convert_mp3_to_wav():
    results = []
    for src in all_files.get():
        typ = 'wav'
        dst = get_destination_file(src, typ)
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format=typ)
        results.append('zu {} konvertiert: "{}"'.format(typ, dst))
    empty_file_list()
    set_result_list(results)


def convert_wav_to_mp3():
    results = []
    for src in all_files.get():
        typ = 'mp3'
        dst = get_destination_file(src, typ)
        sound = AudioSegment.from_wav(src)
        sound.export(dst, format=typ)
        results.append('zu {} konvertiert: "{}"'.format(typ, dst))
    empty_file_list()
    set_result_list(results)


def reduce_noise():
    print('Reduce noise!')

window = tk.Tk()

window.title("Welcome to LikeGeeks app")
window.geometry('750x500')

lbl = tk.Label(window, text="Ausgewählte Dateien:")
lbl.grid(row=1, column=1, columnspan=2)

all_files = tk.Variable(value=[])
filebox = tk.Listbox(window, listvariable=all_files, width=90, selectmode='multiple')
filebox.grid(row=2, column=1, columnspan=2)

add_button = tk.Button(window, text="Dateien hinzufügen", command=add_files)
add_button.grid(column=1, row=3)

remove_button = tk.Button(window, text="Ausgewählte Dateien entfernen", command=remove_files)
remove_button.grid(column=2, row=3)


sep = ttk.Separator(window)
sep.grid(column=1, row=4, columnspan=5, ipady=20, ipadx=150)

tk.Button(window, text="MP3 zu WAV konvertieren", command=convert_mp3_to_wav).grid(column=1, row=5, sticky="w")
tk.Button(window, text="WAV zu MP3 konvertieren", command=convert_wav_to_mp3).grid(column=1, row=6, sticky="w")
tk.Button(window, text="Rauschen entfernen", command=reduce_noise).grid(column=1, row=7, sticky="w")

# Results
tk.Label(window, text="Prozess-Ergebnis:").grid(row=15, column=1, columnspan=2)

result_list = tk.Variable(value=[])
result_box = tk.Listbox(window, listvariable=result_list, width=90, selectmode='multiple')
result_box.grid(row=20, column=1, columnspan=2)


window.mainloop()

# All Files
src = "wavfile.wav"
dst = "test21313.mp3"



# convert mp3 to wav
# sound = AudioSegment.from_wav(src)
# sound.export(dst, format="mp3")

