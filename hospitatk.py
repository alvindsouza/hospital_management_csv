import csv
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox , simpledialog , ttk
from datetime import datetime


patient_data_file = 'patients.csv'
doctor_data_file = 'doctor.csv'


# Define functions for each operation

# Function to check and create CSV file if necessary
# Function to add a new patient
def add_patient():
    def submit_patient():
        with open(patient_data_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name_entry.get(), age_entry.get(), height_entry.get(), blood_type_entry.get(),
                             hemoglobin_entry.get(),bloodpa_entry.get(), prescription_entry.get(), illness_entry.get(),
                             last_visit_entry.get(), insurance_entry.get()])
            messagebox.showinfo("Info", "Patient added successfully")
        add_window.destroy()

#new
    # New window for patient data entry
    add_window = tk.Toplevel(root)
    add_window.title("Add New Patient")


    tk.Label(add_window, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1)


    tk.Label(add_window, text="Age:").grid(row=1, column=0)
    age_entry = tk.Entry(add_window)
    age_entry.grid(row=1, column=1)


    tk.Label(add_window, text="Height:").grid(row=2, column=0)
    height_entry = tk.Entry(add_window)
    height_entry.grid(row=2, column=1)


    tk.Label(add_window, text="Blood Type:").grid(row=3, column=0)
    blood_type_entry = tk.Entry(add_window)
    blood_type_entry.grid(row=3, column=1)


    tk.Label(add_window, text="Hemoglobin Level:").grid(row=4, column=0)
    hemoglobin_entry = tk.Entry(add_window)
    hemoglobin_entry.grid(row=4, column=1)
   
    tk.Label(add_window, text="Blood Pressure:").grid(row=5, column=0)
    bloodpa_entry = tk.Entry(add_window)
    bloodpa_entry.grid(row=5, column=1)


    tk.Label(add_window, text="Prescription:").grid(row=6, column=0)
    prescription_entry = tk.Entry(add_window)
    prescription_entry.grid(row=6, column=1)


    tk.Label(add_window, text="Current Illness:").grid(row=7, column=0)
    illness_entry = tk.Entry(add_window)
    illness_entry.grid(row=7, column=1)


    # Automatically fill the last visit date with today's date
    today_date = datetime.now().strftime("%Y-%m-%d")
    tk.Label(add_window, text="Last Visit Date:").grid(row=8, column=0)
    last_visit_entry = tk.Entry(add_window)
    last_visit_entry.grid(row=8, column=1)
    last_visit_entry.insert(0, today_date)  # Set default value to today's date


    tk.Label(add_window, text="Insurance Details:").grid(row=9, column=0)
    insurance_entry = tk.Entry(add_window)
    insurance_entry.grid(row=9, column=1)


    submit_button = tk.Button(add_window, text="Submit", command=submit_patient)
    submit_button.grid(row=10, column=1)


def add_doctor():
    def get_last_visit():
        return datetime.now().strftime("%Y-%m-%d")


    def submit_doctor():
        with open(doctor_data_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([get_last_visit(), name_entry.get(), gender_entry.get(), spcl_entry.get()])
            messagebox.showinfo("Info", "Doctor added successfully")
        add_window.destroy()


    # New window for doctor data entry
    add_window = tk.Toplevel(root)
    add_window.title("Add New Doctor")


    tk.Label(add_window, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1)


    tk.Label(add_window, text="Gender:").grid(row=1, column=0)
    gender_entry = tk.Entry(add_window)
    gender_entry.grid(row=1, column=1)


    tk.Label(add_window, text="Specialization:").grid(row=2, column=0)
    spcl_entry = tk.Entry(add_window)
    spcl_entry.grid(row=2, column=1)


    tk.Label(add_window, text="Last Updated Date:").grid(row=3,column=0)
    last_visit_entry = tk.Entry(add_window)
    last_visit_entry.grid(row=3, column=1)
    last_visit_entry.insert(0, get_last_visit())  # Set default value to today's date


    submit_button = tk.Button(add_window, text="Submit", command=submit_doctor)
    submit_button.grid(row=4, column=1)


def doctor_checkin():
   
    ax=[]
    with open(doctor_data_file, 'r') as file:
       reader = csv.reader(file)
       for row in reader:
           if row[4] == "Available":
                ax.append(row)
       
    all_doctor = tk.Toplevel(root)
    all_doctor.title("All Doctors")


    tree = ttk.Treeview(all_doctor, columns=('Last Updated','Name','Gender','Specialzation','Availability'), show='headings')
    a = ('Last Updated','Name','Gender','Specialzation','Availability')
    for x in a:
        tree.heading(a,text=a)
    for row in ax:
        tree.insert('', tk.END, values=row)
               
def find_patient():
    patient_id = simpledialog.askstring("Input", "Enter patient's name to search")
    with open(patient_data_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == patient_id:
                patient_info = f"""
                Name: {row[0]}
                Age: {row[1]}
                Height: {row[2]}
                Blood Type: {row[3]}
                Hemoglobin Level: {row[4]} g/dL (Healthy levels: 13.8 to 17.2 g/dL for men, 12.1 to 15.1 g/dL for women)
                Blood Pressure: {row[5]} mmHg (Healthy levels: 120/80 mmHg)
                Prescription: {row[6]}
                Current Illness: {row[7]}
                Last Visit Date: {row[8]}
                Insurance: {row[9]}
                """
                messagebox.showinfo("Patient Details", patient_info)
                return
        messagebox.showinfo("Info", "Patient not found")
def update_patient():
        patient_name_to_update = simpledialog.askstring("Input", "Enter patient's name to update")
        patient_exists = False
        with open(patient_data_file, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == patient_name_to_update:
                    patient_exists = True
                    break


        if patient_exists:
            def submit_update():
                    updated_data = []
                    patient_found = False
                    with open(patient_data_file, 'r', newline='') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if row[0] == update_name_entry.get():
                                updated_data.append([update_name_entry.get(), update_age_entry.get(),
                                                     update_height_entry.get(), row[3],
                                                     update_hemoglobin_entry.get(), update_prescription_entry.get(),
                                                     update_illness_entry.get(), update_last_visit_entry.get(),
                                                     update_insurance_entry.get()])
                                patient_found = True
                            else:
                                updated_data.append(row)
           
                    with open(patient_data_file, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(updated_data)
                   
                    if patient_found:
                        messagebox.showinfo("Info", "Patient details updated successfully")
                    else:
                        messagebox.showinfo("Info", "Patient not found")
                    update_window.destroy()

            update_window = tk.Toplevel(root)
            update_window.title("Update Patient Details")


            tk.Label(update_window, text="Enter Patient's Name to Update:").grid(row=0, column=0)
            update_name_entry = tk.Entry(update_window)
            update_name_entry.grid(row=0, column=1)


            tk.Label(update_window, text="New Age:").grid(row=1, column=0)
            update_age_entry = tk.Entry(update_window)
            update_age_entry.grid(row=1, column=1)


            tk.Label(update_window, text="New Height:").grid(row=2, column=0)
            update_height_entry = tk.Entry(update_window)
            update_height_entry.grid(row=2, column=1)
         
            tk.Label(update_window, text="Hemoglobin Level:").grid(row=4, column=0)
            update_hemoglobin_entry = tk.Entry(update_window)
            update_hemoglobin_entry.grid(row=4, column=1)
           
            tk.Label(update_window, text="Blood Pressure:").grid(row=5, column=0)
            bloodpa_entry = tk.Entry(update_window)
            bloodpa_entry.grid(row=5, column=1)


            tk.Label(update_window, text="Prescription:").grid(row=6, column=0)
            update_prescription_entry = tk.Entry(update_window)
            update_prescription_entry.grid(row=6, column=1)


            tk.Label(update_window, text="Current Illness:").grid(row=7, column=0)
            update_illness_entry = tk.Entry(update_window)
            update_last_visit_entry.grid(row=7, column=1)


            tk.Label(update_window, text="New Last Visit Date (YYYY-MM-DD):").grid(row=8, column=0)
            update_last_visit_entry = tk.Entry(update_window)
            update_last_visit_entry.grid(row=8, column=1)


            tk.Label(update_window, text="New Insurance Details:").grid(row=9, column=0)
            update_insurance_entry = tk.Entry(update_window)
            update_insurance_entry.grid(row=9, column=1)


            submit_button = tk.Button(update_window, text="Submit Update", command=submit_update)
            submit_button.grid(row=10, column=1)


        else:
            add_new = messagebox.askyesno("Patient Not Found", "Patient not found. Would you like to add a new patient?")
            if add_new:
                add_patient()


def import_patients():
    patient_datanew = simpledialog.askstring("Input", "Enter patient data file")
    try:
        with open(patient_datanew, 'r', newline='') as src:
            reader = csv.reader(src)
            next(reader, None)  # Skip header
            data_to_append = list(reader)
       
        with open(patient_data_file, 'a', newline='') as dest:
            writer = csv.writer(dest)
            for row in data_to_append:
                writer.writerow(row)


        messagebox.showinfo("Info","Patients added successfully")
    except FileNotFoundError:
        print("File not found. Please check the file paths.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def show_all_patients():
    all_patients_window = tk.Toplevel(root)
    all_patients_window.title("All Patients")


    tree = ttk.Treeview(all_patients_window, columns=('Name', 'Age', 'Height', 'Blood Type', 'Hemoglobin', 'Prescription', 'Illness', 'Last Visit', 'Insurance'), show='headings')


    tree.heading('Name', text='Name')
    tree.heading('Age', text='Age')
    tree.heading('Height', text='Height')
    tree.heading('Blood Type', text='Blood Type')
    tree.heading('Hemoglobin', text='Hemoglobin')
    tree.heading('Prescription', text='Prescription')
    tree.heading('Illness', text='Illness')
    tree.heading('Last Visit', text='Last Visit')
    tree.heading('Insurance', text='Insurance')
    with open(patient_data_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            tree.insert('', tk.END, values=row)
    scrollbar = ttk.Scrollbar(all_patients_window, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    # Pack the Treeview
    tree.pack(expand=True, fill='both')
def delete_patient():
    def submit_delete():
        patient_name_to_delete = delete_name_entry.get()


        # Confirmation dialog box
        confirm_delete = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {patient_name_to_delete}?")
        if not confirm_delete:
            messagebox.showinfo("Cancellation", "Patient deletion cancelled.")
            delete_window.destroy()
            return


        updated_data = []
        patient_found = False
        with open(patient_data_file, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > 0 and row[0] != patient_name_to_delete:
                    updated_data.append(row)
                elif row and len(row) > 0 and row[0] == patient_name_to_delete:
                    patient_found = True


        if patient_found:
            with open(patient_data_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)
            messagebox.showinfo("Info", "Patient deleted successfully")
        else:
            messagebox.showinfo("Info", "Patient not found")


        delete_window.destroy()
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Patient")


    tk.Label(delete_window, text="Enter Patient's Name to Delete:").grid(row=0, column=0)
    delete_name_entry = tk.Entry(delete_window)
    delete_name_entry.grid(row=0, column=1)


    delete_button = tk.Button(delete_window, text="Delete", command=submit_delete)
    delete_button.grid(row=1, column=1)


# GUI setup
root = tk.Tk()
root.title("Hospital Database")
img_path = "hospital_logo.jpg"  # Replace with your image path if different
try:
    img = Image.open(img_path)
    img = img.resize((100, 100))  # Adjust size as needed
    logo_img = ImageTk.PhotoImage(img)
    logo_label = tk.Label(root, image=logo_img, text="")
    logo_label.pack(pady=(20, 10))

except Exception as e:
    print(f"Error loading image: {e}")
heading_label = tk.Label(root, text="⚕ HOSPITAL DATABASE", font=("Arial", 20), fg="red")
fram = tk. Frame(root, bg= "grey")
buttons=[("Add New Patient",add_patient),
         ("Delete Patient",delete_patient),
         ("Find Patient",find_patient),
         ("Update Patient Details",update_patient),
         ("Import Patients",import_patients),
         ("Show All Patients",show_all_patients),
         ('Add Doctor',add_doctor)]


# Header label
heading_label = tk.Label(root, text="⚕ COTTONFIELD HOSPITAL ", font=("Arial", 20))
heading_label.pack(pady=(10, 10))


fram.pack(fill='x')
for name,commmand in buttons:
    tempval = tk.Button(fram, text= name, command=commmand)
    tempval.pack(pady= 5)




root.mainloop()

