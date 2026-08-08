# 🛒 Supermarket Management System

A desktop **Supermarket Management System** built in Python with a `tkinter` GUI. It simulates a real shopping experience — browsing and searching products, managing a shopping cart, checking out with an auto-generated receipt, and viewing a sales/inventory statistics dashboard.

Built as a team project (5 members) using **Object-Oriented Programming (OOP)** principles, with the codebase divided into independent, clearly separated modules.

---

## ✨ Features

- 🔍 **Search & Browse** — search products by ID or by name/category keyword, or browse by category
- ↕️ **Sorting** — sort any product list by name, price, stock, or discount (ascending/descending) without losing the active filter
- 🛍️ **Shopping Cart** — add products, update quantities, remove items, or clear the cart, with automatic stock reservation/restoration
- 🧾 **Receipt Generation** — auto-generated receipt number, date, and time, with the option to save the receipt as a `.txt` file
- 📊 **Statistics Dashboard** — visual charts (pie & bar) for products per category, stock levels, quantities sold, and revenue per product
- ✅ **Robust Error Handling** — validated input and graceful handling of invalid actions or empty states, all reported via message boxes

---

## 🖥️ Screenshots

> Screenshots of the application are available in the [`Screenshots`](./Screenshots) folder.

---

## 🧱 System Architecture

The project follows the **Single Responsibility Principle** and is organized into 4 core classes:

| Class | Responsibility |
|---|---|
| `Product` | Represents a single product's data (ID, category, name, price, stock, unit, discount, sold, revenue) |
| `CartItem` | Links a `Product` with a requested quantity and calculates its own total, discount, and final price |
| `Cart` | Holds a list of `CartItem` objects and manages the cart as a whole (clear, check empty, calculate grand total) |
| `SuperMarketGUI` | The main controller — builds the GUI, manages navigation between screens, and handles all user interactions |

**Relationships:**
- `SuperMarketGUI` holds a list of `Product` objects and one `Cart`
- `Cart` holds a list of `CartItem` objects
- Each `CartItem` references (not copies) its `Product`, so any change to a product (stock, sold, revenue) is reflected everywhere it's used

---

## 🚀 Getting Started

### Prerequisites

- Python 3
- The following libraries:
  - `tkinter` (usually included with Python)
  - `matplotlib`

Install matplotlib if needed:

```bash
pip install matplotlib
```

### Running the Application

```bash
python Supermarket_Management_System.py
```

The application opens directly on the home screen.

---

## 🧭 How to Use

1. From the **Home Screen**, search for a product, pick a category, or click **View All Products**.
2. Use the **Sort By** dropdown to reorder the displayed products by name, price, stock, or discount.
3. Select a product and click **Add To Cart**, then enter the desired quantity.
4. Open the **Shopping Cart** to update quantities, remove items, or clear the cart.
5. Open the **Receipt** screen to review the order, save it as a text file, and finish the order.
6. Open **Statistics** at any time to view live charts on category distribution, stock, sales, and revenue.
7. Click **Exit** on the home screen to close the application.

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| **Python 3** | Core programming language |
| **tkinter / ttk** | GUI: windows, tables (Treeview), buttons, and input dialogs |
| **datetime** | Generates the receipt number, date, and time |
| **matplotlib** | Renders the statistics dashboard (pie chart & bar charts) |

---

## 📋 Requirements Summary

The system was built to satisfy a set of functional requirements covering:

- Product catalog display, search, filtering, and sorting
- Shopping cart management (add, update, remove, clear) with stock reservation
- Checkout with subtotal, discount, and total calculation
- Receipt generation and saving
- Statistics dashboard for category, stock, sales, and revenue

...as well as non-functional requirements around usability, performance, reliability, maintainability, portability, and data consistency.

Full details are available in the [project documentation](./Supermarket_Management_System_Documentation.pdf).

---

## ⚠️ Error Handling

The system is designed to **fail safely, fail clearly, and fail early** — never crashing on invalid input. Examples include:

- Warnings for no product selected, empty search input, or insufficient stock
- Informational prompts when the cart or receipt screens are accessed while the cart is empty
- Confirmation dialogs before destructive actions like clearing the cart

---

## 👥 Team & Module Breakdown

This project was developed collaboratively by a team of 5 members, with the codebase divided into clearly commented sections, each owning an independent module of the system (e.g., product browsing and display, cart management, receipt generation, statistics).

---

## 🔮 Future Improvements

Thanks to its OOP-based structure, the system can be extended without rewriting existing code, for example:

- Customer login/accounts
- Multiple payment methods
- Persistent storage using a database
- Additional statistics and reporting options

---

## 📄 License

This project was created for educational purposes as part of a team-based programming course.
