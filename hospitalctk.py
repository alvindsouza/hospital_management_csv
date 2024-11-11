import csv
import customtkinter as ctk
from tkinter import messagebox, simpledialog
from datetime import datetime
from PIL import Image, ImageTk

# File paths for data
patient_data_file = 'patients.csv'
doctor_data_file = 'doctor.csv'

# Initialize customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Root window setup
root = ctk.CTk()
root.title("Hospital Database")
root.geometry("600x700")

# Load and display image at the top of the window
img_path = "hospital_logo.png"  # Replace with your image path if different
try:
    img = Image.open(img_path)
    img = img.resize((100, 100))  # Adjust size as needed
    logo_img = ImageTk.PhotoImage(img)
    logo_label = ctk.CTkLabel(root, image=logo_img, text="")
    logo_label.pack(pady=(20, 10))
except Exception as e:
    print(f"Error loading image: {e}")

# Header label
heading_label = ctk.CTkLabel(root, text="⚕ HOSPITAL DATABASE", font=("Arial", 20), text_color="red")
heading_label.pack(pady=(10, 20))

# Define functions for each operation

def add_patient():
    def submit_patient():
        with open(patient_data_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                entries['name_entry'].get(), entries['age_entry'].get(), entries['height_entry'].get(),
                entries['blood_type_entry'].get(), entries['hemoglobin_entry'].get(),
                entries['bloodpa_entry'].get(), entries['prescription_entry'].get(),
                entries['illness_entry'].get(), last_visit_entry.get(), entries['insurance_entry'].get()
            ])
            messagebox.showinfo("Info", "Patient added successfully")
        add_window.destroy()

    # New window for patient data entry
    add_window = ctk.CTkToplevel(root)
    add_window.title("Add New Patient")

    # Create patient form fields
    fields = [
        ("Name", "name_entry"), ("Age", "age_entry"), ("Height", "height_entry"),
        ("Blood Type", "blood_type_entry"), ("Hemoglobin Level", "hemoglobin_entry"),
        ("Blood Pressure", "bloodpa_entry"), ("Prescription", "prescription_entry"),
        ("Current Illness", "illness_entry"), ("Insurance Details", "insurance_entry")
    ]
    entries = {}
    for i, (label, var_name) in enumerate(fields):
        ctk.CTkLabel(add_window, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = ctk.CTkEntry(add_window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[var_name] = entry

    # Last visit date with today's date as default
    today_date = datetime.now().strftime("%Y-%m-%d")
    ctk.CTkLabel(add_window, text="Last Visit Date").grid(row=8, column=0, padx=10, pady=5)
    last_visit_entry = ctk.CTkEntry(add_window)
    last_visit_entry.grid(row=8, column=1, padx=10, pady=5)
    last_visit_entry.insert(0, today_date)

    # Submit button
    submit_button = ctk.CTkButton(add_window, text="Submit", command=submit_patient)
    submit_button.grid(row=10, column=1, pady=10)

def add_doctor():
    def submit_doctor():
        with open(doctor_data_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d"), name_entry.get(),
                gender_entry.get(), specialization_entry.get(), "Available"
            ])
            messagebox.showinfo("Info", "Doctor added successfully")
        add_window.destroy()

    # New window for doctor data entry
    add_window = ctk.CTkToplevel(root)
    add_window.title("Add New Doctor")

    # Doctor form fields
    ctk.CTkLabel(add_window, text="Name").grid(row=0, column=0, padx=10, pady=5)
    name_entry = ctk.CTkEntry(add_window)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    ctk.CTkLabel(add_window, text="Gender").grid(row=1, column=0, padx=10, pady=5)
    gender_entry = ctk.CTkEntry(add_window)
    gender_entry.grid(row=1, column=1, padx=10, pady=5)

    ctk.CTkLabel(add_window, text="Specialization").grid(row=2, column=0, padx=10, pady=5)
    specialization_entry = ctk.CTkEntry(add_window)
    specialization_entry.grid(row=2, column=1, padx=10, pady=5)

    ctk.CTkLabel(add_window, text="Last Updated Date").grid(row=3, column=0, padx=10, pady=5)
    last_visit_entry = ctk.CTkEntry(add_window)
    last_visit_entry.grid(row=3, column=1, padx=10, pady=5)
    last_visit_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

    submit_button = ctk.CTkButton(add_window, text="Submit", command=submit_doctor)
    submit_button.grid(row=4, column=1, pady=10)

def find_patient():
    patient_name = simpledialog.askstring("Input", "Enter patient's name to search")
    with open(patient_data_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == patient_name:
                patient_info = f"Name: {row[0]}\nAge: {row[1]}\nHeight: {row[2]}\nBlood Type: {row[3]}\n" \
                               f"Hemoglobin Level: {row[4]} g/dL\nBlood Pressure: {row[5]} mmHg\n" \
                               f"Prescription: {row[6]}\nCurrent Illness: {row[7]}\n" \
                               f"Last Visit Date: {row[8]}\nInsurance: {row[9]}"
                messagebox.showinfo("Patient Details", patient_info)
                return
        messagebox.showinfo("Info", "Patient not found")

def show_all_patients():
    all_patients_window = ctk.CTkToplevel(root)
    all_patients_window.title("All Patients")
    patients_display = ""

    with open(patient_data_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                patients_display += f"Name: {row[0]}, Age: {row[1]}, Height: {row[2]}, Blood Type: {row[3]}, " \
                                    f"Hemoglobin: {row[4]}, BP: {row[5]}, Prescription: {row[6]}, " \
                                    f"Illness: {row[7]}, Last Visit: {row[8]}, Insurance: {row[9]}\n\n"

    text_box = ctk.CTkTextbox(all_patients_window, width=500, height=400)
    text_box.insert("1.0", patients_display)
    text_box.configure(state="disabled")
    text_box.pack(padx=10, pady=10)

# Main button setup
buttons = [
    ("Add New Patient", add_patient),
    ("Add Doctor", add_doctor),
    ("Find Patient", find_patient),
    ("Show All Patients", show_all_patients),
]

for name, command in buttons:
    button = ctk.CTkButton(root, text=name, command=command)
    button.pack(pady=5)

# Run main loop
root.mainloop()
