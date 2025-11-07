import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# -------------------- DATABASE CONNECTIONS --------------------

def connect_it():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mca1",  # Change this to your MySQL password
        database="DB_IT"
    )

def connect_cs():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mca1",  # Change this to your MySQL password
        database="DB_CS"
    )

# -------------------- FUNCTIONS --------------------

def show_all_students():
    """Fetch and display all students from both databases."""
    try:
        con_it = connect_it()
        con_cs = connect_cs()
        cur_it = con_it.cursor()
        cur_cs = con_cs.cursor()

        cur_it.execute("SELECT * FROM student_it")
        it_data = cur_it.fetchall()

        cur_cs.execute("SELECT * FROM student_cs")
        cs_data = cur_cs.fetchall()

        all_data = it_data + cs_data
        update_treeview(all_data)

        con_it.close()
        con_cs.close()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))


def search_by_department():
    """Show records of selected department (IT or CS)."""
    dept = dept_var.get()
    try:
        if dept == "IT":
            con = connect_it()
            cur = con.cursor()
            cur.execute("SELECT * FROM student_it")
        else:
            con = connect_cs()
            cur = con.cursor()
            cur.execute("SELECT * FROM student_cs")

        data = cur.fetchall()
        update_treeview(data)
        con.close()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def add_student():
    """Insert a new student in selected department database."""
    sid = entry_id.get()
    name = entry_name.get()
    dept = entry_dept.get()
    addr = entry_addr.get()
    course = entry_course.get()
    daa = entry_daa.get()
    adbms = entry_adbms.get()
    python_marks = entry_python.get()
    ds = entry_ds.get()

    try:
        if dept.upper() == "IT":
            con = connect_it()
            cur = con.cursor()
            cur.execute("INSERT INTO student_it VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (sid, name, dept, addr, course, daa, adbms, python_marks, ds))
        elif dept.upper() == "CS":
            con = connect_cs()
            cur = con.cursor()
            cur.execute("INSERT INTO student_cs VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (sid, name, dept, addr, course, daa, adbms, python_marks, ds))
        else:
            messagebox.showwarning("Invalid", "Department must be IT or CS")
            return

        con.commit()
        con.close()
        messagebox.showinfo("Success", "Record added successfully!")
        show_all_students()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def calculate_total_and_avg(data):
    """Calculate total and average marks for each student."""
    result = []
    for row in data:
        total = row[5] + row[6] + row[7] + row[8]
        avg = total / 4
        result.append(row + (total, avg))
    return result


def update_treeview(data):
    """Display data in the table."""
    for row in tree.get_children():
        tree.delete(row)
    processed = calculate_total_and_avg(data)
    for record in processed:
        tree.insert('', tk.END, values=record)

# -------------------- GUI SETUP --------------------

root = tk.Tk()
root.title("Distributed Student Management System (v2)")
root.geometry("1100x600")
root.config(bg="#e8f5e9")

title = tk.Label(root, text="Distributed Student Management System",
                 font=("Arial", 18, "bold"), bg="#1b5e20", fg="white", pady=10)
title.pack(fill=tk.X)

# Frame for Input
frame = tk.Frame(root, bg="#a5d6a7", pady=10)
frame.pack(fill=tk.X)

tk.Label(frame, text="Student ID:", bg="#a5d6a7").grid(row=0, column=0, padx=5)
entry_id = tk.Entry(frame, width=10)
entry_id.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Name:", bg="#a5d6a7").grid(row=0, column=2, padx=5)
entry_name = tk.Entry(frame, width=15)
entry_name.grid(row=0, column=3, padx=5)

tk.Label(frame, text="Dept (IT/CS):", bg="#a5d6a7").grid(row=0, column=4, padx=5)
entry_dept = tk.Entry(frame, width=8)
entry_dept.grid(row=0, column=5, padx=5)

tk.Label(frame, text="Address:", bg="#a5d6a7").grid(row=1, column=0, padx=5)
entry_addr = tk.Entry(frame, width=15)
entry_addr.grid(row=1, column=1, padx=5)

tk.Label(frame, text="Course:", bg="#a5d6a7").grid(row=1, column=2, padx=5)
entry_course = tk.Entry(frame, width=10)
entry_course.grid(row=1, column=3, padx=5)

# Subject marks input
tk.Label(frame, text="DAA:", bg="#a5d6a7").grid(row=2, column=0, padx=5)
entry_daa = tk.Entry(frame, width=6)
entry_daa.grid(row=2, column=1, padx=5)

tk.Label(frame, text="ADBMS:", bg="#a5d6a7").grid(row=2, column=2, padx=5)
entry_adbms = tk.Entry(frame, width=6)
entry_adbms.grid(row=2, column=3, padx=5)

tk.Label(frame, text="Python:", bg="#a5d6a7").grid(row=2, column=4, padx=5)
entry_python = tk.Entry(frame, width=6)
entry_python.grid(row=2, column=5, padx=5)

tk.Label(frame, text="Data Science:", bg="#a5d6a7").grid(row=2, column=6, padx=5)
entry_ds = tk.Entry(frame, width=6)
entry_ds.grid(row=2, column=7, padx=5)

add_btn = tk.Button(frame, text="Add Student", bg="#2e7d32", fg="white",
                    command=add_student)
add_btn.grid(row=3, column=0, columnspan=2, pady=5)

# -------------------- SEARCH SECTION --------------------

search_frame = tk.Frame(root, bg="#81c784", pady=5)
search_frame.pack(fill=tk.X)

tk.Label(search_frame, text="Select Department:", bg="#81c784").pack(side=tk.LEFT, padx=10)
dept_var = tk.StringVar(value="IT")
ttk.Combobox(search_frame, textvariable=dept_var, values=["IT", "CS"], width=10).pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="Search", bg="#1b5e20", fg="white",
          command=search_by_department).pack(side=tk.LEFT, padx=10)
tk.Button(search_frame, text="Show All", bg="#1b5e20", fg="white",
          command=show_all_students).pack(side=tk.LEFT, padx=10)

# -------------------- TREEVIEW TABLE --------------------

table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

columns = ("ID", "Name", "Department", "Address", "Course",
           "DAA", "ADBMS", "Python", "Data Science", "Total", "Average")

tree = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=90)
tree.pack(fill=tk.BOTH, expand=True)

# Load data initially
show_all_students()

root.mainloop()
