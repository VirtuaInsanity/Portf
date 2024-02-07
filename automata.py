import datetime
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
dateT = datetime.date.today()
offset = datetime.timedelta(hours=3)
datetime.timezone(offset, name='МСК')
print("HELP_",dateT,"LMAO", sep='')
root = Tk()
root.title("Univer") 
root.geometry("400x400")
root.resizable(False, False)
root.attributes("-toolwindow", True)
testS = r"\\192.168.0.254\_autobackup_store\111.txt"
testD = r"\\192.168.0.247\_autobackup_store\111"

#\\192.168.0.254\_autobackup_store\DBBSR\BSR-50RS0016-%DD%.%MM%.%YYYY%.7z "\\192.168.0.247\_autobackup_store\DBBSR\BSR-50RS0016-%DD%.%MM%.%YYYY%.7z*" 
#\\192.168.0.254\_autobackup_store\DBSDP\SDP-50RS0016-%DD%.%MM%.%YYYY%.7z "\\192.168.0.247\_autobackup_store\DBSDP\SDP-50RS0016-%DD%.%MM%.%YYYY%.7z*"
#\\192.168.0.254\_autobackup_store\DBSK\POSTMAN_%DD%.%MM%.%YYYY%_korolev.rar "\\192.168.0.247\_autobackup_store\DBSK\POSTMAN_%DD%.%MM%.%YYYY%_korolev.rar*"
#\\192.168.0.254\_autobackup_store\DBCadry\db_cadry_%DD%.%MM%.%YYYY%_korolev.rar "\\192.168.0.247\_autobackup_store\DBCadry\db_cadry_%DD%.%MM%.%YYYY%_korolev.rar*"
#\\192.168.0.254\data\JUSTICE "\\192.168.0.247\data\Justice" /EXCLUDE:C:\Users\User\Desktop\BackupBAT\ex.txt
def CopyBases():
    print("Начало копирования базы:", dateT)
    CopyBasesButton["state"] = tk.DISABLED
    shutil.copy(testS, testD)
    listbox1.insert(END, testS)
    print("Завершение копирования")
    CopyBasesButton["state"] = tk.NORMAL
disk = ""
def copyToDisk():
    disk = fd.askdirectory()
    print(disk)
    informDisk['text'] = disk
    informDisk['foreground'] = "black"
#Добавление верхних вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill="both")
frame1 = ttk.Frame(notebook); frame2 = ttk.Frame(notebook); frame3 = ttk.Frame(notebook)
frame1.pack(fill="both", expand=True); frame2.pack(fill="both", expand=True); frame3.pack(fill="both", expand=True)
notebook.add(frame1, text="Копирование"); notebook.add(frame2, text="Удаление"); notebook.add(frame3, text="Проверка Места")

#Копирование command = copyToDisk
CopyBasesButton = ttk.Button(frame1, text = "Копировать базы", command = CopyBases)
CopyBasesButton.pack(fill="x")
listbox1 = Listbox(frame1)
listbox1.pack(fill="x")

#На какой диск будет произведено вторичное копирование
copyToDiskOpt = ttk.Button(frame1, text = "Выберите диск для копирования на него", command = copyToDisk)
copyToDiskOpt.pack(fill="x")
informDisk = ttk.Label(frame1, text="Выберите диск куда нужно скопировать файлы", foreground="gray")
informDisk.pack(fill="x")

DeleteBeforeButton = ttk.Button(frame2, text = "Удалить данные до числа:")
DeleteBeforeButton.pack(fill="x")
informDate = ttk.Label(frame2, text="Число вводить в формате ГОД-МЕСЯЦ-ДЕНЬ", foreground="gray")
informDate.pack(fill="x")
EntryDeleteBefore = ttk.Entry(frame2)
EntryDeleteBefore.pack(fill="x")


root.mainloop()
