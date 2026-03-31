# SmartProcure Inventory System 📦

A robust inventory management backend built with **Python**, **SQLAlchemy 2.0**, and **PostgreSQL**. This system tracks parts, categories, suppliers, and stock movements with high data integrity.

## 🚀 Key Features

- **Modern ORM:** Implements SQLAlchemy 2.0 `Mapped` and `mapped_column` declarations.
- **Stock Tracking:** Automated tracking of incoming and outgoing movements.
- **Data Validation:** Uses PostgreSQL Native Enums to enforce strict movement types (`incoming`, `outgoing`).
- **Automated Timestamps:** Server-side timestamping using `func.now()`.
- **Unit Testing:** Comprehensive test suite to validate database relationships and constraints.

---

## 🛠 Prerequisites

- **Python 3.10+**
- **PostgreSQL** (Installed and running)
- **Virtual Environment** (`venv` or `conda`)

---

## 📦 Installation & Setup

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/idoelarat/SmartProcure.git](https://github.com/idoelarat/SmartProcure.git)
    cd SmartProcure
    ```

2.  **Create a Virtual Environment:**

    ```bash
    python -m venv .venv
    # Activate on Windows:
    .venv\Scripts\activate
    # Activate on Mac/Linux:
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Configuration:**
    Ensure your `database.py` reflects your PostgreSQL credentials in the .env file:
    `postgresql://USER:PASSWORD@localhost:5432/DB_NAME`

---

## 🚦 Running Tests

To verify the database models and relationships, run the test suite:

```bash
python app/test_db.py
```

### 📂 Project Structure

- **app/models.py**: Database schema, relationships, and Enum definitions.
- **app/database.py**: SQLAlchemy engine, session maker, and connection logic.
- **app/test_db.py**: Unit tests for validating CRUD operations and foreign key constraints.

### 🛠 Tech Stack

| Technology     | Role                                           |
| :------------- | :--------------------------------------------- |
| **Python**     | Core Programming Language                      |
| **SQLAlchemy** | SQL Toolkit and Object Relational Mapper (ORM) |
| **PostgreSQL** | Relational Database Management System          |
| **Unittest**   | Built-in Python Testing Framework              |
