# **Library Management System (LMS) - Python & PyQt**  

![Library Management System](https://img.shields.io/badge/Python-3.8%2B-blue)  
![PyQt](https://img.shields.io/badge/PyQt-5%2B-green)  
![SQLite](https://img.shields.io/badge/Database-SQLite-yellow)  

A **Library Management System (LMS)** built with **Python, PyQt (for GUI)**, and **SQLite (for database storage)**. This system allows librarians to manage books, members, and transactions efficiently.  

## **📌 Features**  
✔ **Book Management** – Add, update, delete, and search books.  
✔ **Member Management** – Register, update, and manage library members.  
✔ **Borrow & Return System** – Track book loans and returns.  
✔ **Fine Calculation** – Automatically calculates overdue fines.  
✔ **User-Friendly GUI** – Built with **PyQt5** for a smooth experience.  
✔ **Database Integration** – Uses **SQLite** for persistent data storage.  

## **🛠 Technologies Used**  
- **Python 3.8+**  
- **PyQt5** (for GUI)  
- **SQLite3** (for database) 

## **📂 Project Structure**  
```plaintext
Library-Management-System/
│
├── database/                # Database files
│   └── library.db           # SQLite database
│
├── src/                     # Source code
│   ├── models/              # Database models
│   │   ├── book.py          # Book model
│   │   ├── member.py        # Member model
│   │   └── transaction.py   # Transaction model
│   │
│   ├── controllers/         # Business logic
│   │   ├── book_controller.py
│   │   ├── member_controller.py
│   │   └── transaction_controller.py
│   │
│   ├── views/               # PyQt UI logic
│   │   ├── main_window.py   # Main window logic
│   │   └── dialogs/         # Popup dialogs
│   │       ├── add_book_dialog.py
│   │       └── add_member_dialog.py
│   │
│   └── main.py              # Entry point
│
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── LICENSE                  # License file (MIT/GPL)
```

## **🚀 Installation & Setup**  
### **1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/Library-Management-System.git
cd Library-Management-System
```

### **2. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3. Run the Application**  
```bash
python src/main.py
```

## **📜 Database Schema**  
```sql
-- Books Table
CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    is_available BOOLEAN DEFAULT 1
);

-- Members Table
CREATE TABLE members (
    member_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

-- Transactions Table
CREATE TABLE transactions (
    transaction_id TEXT PRIMARY KEY,
    book_id TEXT,
    member_id TEXT,
    issue_date TEXT NOT NULL,
    return_date TEXT,
    fine REAL DEFAULT 0,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);
```

## **🤝 Contributing**  
Contributions are welcome!  
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/new-feature`).  
3. Commit changes (`git commit -m "Add new feature"`).  
4. Push to the branch (`git push origin feature/new-feature`).  
5. Open a **Pull Request**.  

## **📜 License**  
This project is licensed under **MIT License** - see [LICENSE](LICENSE) for details.  

---

### **🔗 Connect with Me**  
- **GitHub:** [@jawadahmedkhawaja](https://github.com/jawadahmedkhawaja)  
- **Email:** jawadahmedkhawajaofficial@gmail.com 

---
