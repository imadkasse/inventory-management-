# Inventory Management CLI Application

## 1. Overview & Goal
The goal of this project is to build a robust, professional **Command Line Interface (CLI) Inventory Management System** using pure Python along with standard industry libraries. This project bridges the gap between basic Python scripts and full-stack enterprise applications by utilizing Object-Oriented Programming (OOP), SQLite ORM database management, data validation, and unit testing.

## 2. Technology Stack
To achieve a real-world, production-ready standard without building a heavy web framework, we will use the following technology stack:

*   **Language:** Python 3.10+
*   **Database & ORM:** SQLite with **SQLAlchemy** (for object-relational mapping and schema management).
*   **Data Validation:** **Pydantic** (to ensure all inputs like prices and stock quantities are valid).
*   **Interface:** **Typer** and **Rich** (to build a clean, colorful, and interactive terminal user interface with tables and prompts).
*   **Environment & Config:** **python-dotenv** (for managing configuration settings safely).
*   **Testing:** **Pytest** (for writing comprehensive unit tests) (optional)

## 3. Core Features & Requirements
*   **Product Management (CRUD):** 
    *   Add new products with name, price, quantity, category, and reorder threshold.
    *   List all products in a nicely formatted table.
    *   Update product details or delete obsolete products.
*   **Stock Transactions:**
    *   Record inbound stock (purchases/restocking) and outbound stock (sales/usage).
    *   Prevent negative stock or invalid adjustments using custom exceptions.
*   **Reports & Alerts:**
    *   Generate a low-stock alert report for items falling below their reorder levels.
    *   Calculate total inventory valuation (Price $\times$ Quantity).

---

## 4. Architecture & Structure Rating

Your proposed project structure is **Outstanding (9.5 / 10)** for a professional backend/CLI application. 

### Why this structure is exceptional:
1. **Separation of Concerns:** It cleanly separates data layers (`database/`), validation (`schemas/`), business logic (`services/`), and presentation (`cli/`).
2. **Standard Industry Conventions:** This modular directory layout mimics how production-grade Python microservices and APIs are structured.
3. **Testability:** Having a dedicated `tests/` directory alongside `pytest.ini` ensures you can easily write automated unit tests for your business logic.

### Minor Recommendation:
* Consider adding a `utils/` or `exceptions.py` inside the root or core module if you want to handle custom application errors cleanly, though they can also fit inside `services/`.

### File Structure: 
    inventory_app/
    ├── .env.example
    ├── requirements.txt
    ├── README.md
    ├── pytest.ini
    ├── config.py                 # Configuration loader (Pydantic Settings)
    ├── database/
    │   ├── connection.py         # DB connection & session management
    │   └── models.py             # SQLAlchemy ORM Models
    ├── schemas/
    │   └── product_schema.py     # Pydantic Schemas for validation
    ├── services/
    │   ├── inventory_service.py  # Business Logic (OOP)
    │   └── report_service.py     # Reports & Metrics calculation
    ├── cli/
    │   └── main.py               # Typer/Rich CLI interface commands
    └── tests/
        └── test_inventory.py     # Pytest unit tests