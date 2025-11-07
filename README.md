# 🎓 Distributed Student Management System (v2)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

📘 Project Overview

The **Distributed Student Management System (DSMS)** is a **Tkinter + MySQL-based desktop application** that manages student records across multiple **distributed databases** (e.g., *DB_IT* and *DB_CS*).  
It connects both databases dynamically, allowing the admin to **view, insert, and manage student data** from different departments in a single, centralized interface.

This project demonstrates the concept of a **Distributed Database System** where multiple departmental databases operate independently but can be accessed and synchronized through one main application.

---

 🚀 Features

✅ Connects two distributed MySQL databases (`DB_IT` and `DB_CS`)  
✅ Fetches, displays, and manages student records from both databases  
✅ Allows adding new student records dynamically based on department  
✅ Calculates **total** and **average marks** automatically  
✅ Provides **department-wise search** and **"Show All"** functionality  
✅ Beautiful **Tkinter-based GUI** (user-friendly and responsive)  
✅ Demonstrates **real-world distributed data management**  

---

🧠 Conceptual Summary

This project simulates how **educational institutions** with separate department-level databases can still access and manage all student records from a **single interface**.

- **DB_IT** → stores students of the IT department  
- **DB_CS** → stores students of the Computer Science department  
- **Central Tkinter App** → connects both, merges data, and performs CRUD operations  

This reflects the **distributed database** principle where:
> “Data is stored across multiple locations but can be accessed transparently as one logical database.”

---

🏗️ System Architecture

```text
        ┌────────────────────────────────────┐
        │    Distributed Student GUI (Tkinter)│
        │-------------------------------------│
        │  - Add Student                     │
        │  - Search by Department            │
        │  - View All Records                │
        └──────────────┬─────────────────────┘
                       │
          ┌────────────┴────────────┐
          │                         │
 ┌────────────────┐       ┌────────────────┐
 │   Database:     │
