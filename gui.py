import tkinter as tk
from tkinter import ttk
import csv
import pandas as pd



FONT = ("Arial", 12, "italic")
filename = "Patient_Records.csv"
fieldname = ["ID", "Name", "Age", "Sex", "Address", "Visit 1", "Visit 2", "Visit 3", "Visit 4", "Visit 5"]

window = tk.Tk()
window.title("Title")
window.minsize(width=1000, height=1000)
window.config(padx=20, pady=20)

# with open(filename, mode="w", newline="") as file1:
#     f1writer = csv.writer(file1)
#     f1writer.writerow(fieldname)


def button_clicked_new():
    print("Creating new patient record")
    print(patient_name.get())
    with open(filename, mode="a", newline="") as file2:
        fwriter = csv.writer(file2)
        fwriter.writerow([patient_id.get(),
                          patient_name.get(),
                          patient_age.get(),
                          patient_sex.get(),
                          address_text.get(1.0, "end-1c"),
                          {date_text.get(),
                          doctor_name.get(),
                          cause_text.get(1.0, "end-1c"),
                          prescription_text.get(1.0, "end-1c")}])


# def button_clicked_old():
#     df = pd.read_csv(filename)
#     for field in filename:
#         if df.loc[patient_id.get(), field] is None:
#             df.loc[patient_id.get(), field] = {date_text.get(),
#                                                doctor_name.get(),
#                                                cause_text.get(1.0, "end-1c"),
#                                                prescription_text.get(1.0, "end-1c")}
#             break
#     df.to_csv(filename, index=False)
#
#     print("Updating old patient record")


# Labels and buttons
welcome_label = tk.Label(text="Filler Text", font=("Arial", 24, "italic"))
welcome_label.config(padx=10, pady=20)
welcome_label.grid(column=1, row=1, columnspan=4)

new_record_button = tk.Button(text="Record New Patient info", command=button_clicked_new)
new_record_button.config(padx=10, pady=20)
new_record_button.grid(column=1, row=2, padx=10, pady=10, columnspan=2)

old_record_button = tk.Button(text="Update Old Patient info", command=button_clicked_old)
old_record_button.config(padx=10, pady=20)
old_record_button.grid(column=3, row=2, padx=10, pady=10, columnspan=2)

id_label = tk.Label(text="Patient ID:", font=FONT)
id_label.config(padx=10, pady=20)
id_label.grid(column=1, row=3)

patient_id = tk.Entry(width=40)
patient_id.grid(column=2, row=3)

name_label = tk.Label(text="Patient name:", font=FONT)
name_label.config(padx=10, pady=20)
name_label.grid(column=3, row=3)

patient_name = tk.Entry(width=40)
patient_name.grid(column=4, row=3)

age_label = tk.Label(text="Age:", font=FONT)
age_label.config(padx=10, pady=20)
age_label.grid(column=1, row=4)

sex_label = tk.Label(text="Sex:", font=FONT)
sex_label.config(padx=10, pady=20)
sex_label.grid(column=3, row=4)

patient_age = tk.Entry(width=20)
patient_age.grid(column=2, row=4)

n = tk.StringVar()
patient_sex = ttk.Combobox(window, width=20, textvariable=n)
patient_sex['values'] = ('Male', 'Female', 'Other')
patient_sex.grid(column=4, row=4)
patient_sex.current()

date_label = tk.Label(text="Date:", font=FONT)
date_label.config(padx=10, pady=20)
date_label.grid(column=1, row=5)

date_text = tk.Entry(width=40)
date_text.grid(column=2, row=5)

doctor_label = tk.Label(text="Consulting Doctor:", font=FONT)
doctor_label.config(padx=10, pady=20)
doctor_label.grid(column=3, row=5)

doctor_name = tk.Entry(width=40)
doctor_name.grid(column=4, row=5)

cause_label = tk.Label(text="Cause:", font=FONT)
cause_label.config(padx=10, pady=20)
cause_label.grid(column=1, row=6)

cause_text = tk.Text(font=FONT, height=2, width=52)
cause_text.grid(column=2, row=6)

prescription_label = tk.Label(text="Prescribed drugs:", font=FONT)
prescription_label.config(padx=10, pady=20)
prescription_label.grid(column=3, row=6)

prescription_text = tk.Text(font=FONT, height=2, width=52)
prescription_text.grid(column=4, row=6)

address_label = tk.Label(text="Patient Address:", font=FONT)
address_label.config(padx=10, pady=20)
address_label.grid(column=1, row=7)

address_text = tk.Text(font=FONT, height=3, width=75)
address_text.grid(column=2, row=7, columnspan=3, pady=10, padx=10)

window.mainloop()
