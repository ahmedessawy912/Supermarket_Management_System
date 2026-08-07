# ==========================================================
#                 MEMBER 1
# ==========================================================

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime
import matplotlib.pyplot as plt


class Product:

    def __init__(self, product_id, category, name, price, stock, unit, discount):

        self.id = product_id
        self.category = category
        self.name = name
        self.price = price
        self.stock = stock
        self.unit = unit
        self.discount = discount

        self.sold = 0
        self.revenue = 0


class CartItem:

    def __init__(self, product, quantity):

        self.product = product
        self.quantity = quantity

    def total_price(self):

        return self.product.price * self.quantity

    def discount(self):

        return self.total_price() * self.product.discount / 100

    def final_price(self):

        return self.total_price() - self.discount()


class Cart:

    def __init__(self):

        self.items = []

    def clear(self):

        self.items.clear()

    def is_empty(self):

        return len(self.items) == 0

    def total(self):

        total = 0

        for item in self.items:

            total += item.final_price()

        return total


class SuperMarketGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("SuperMarket Management System")

        self.root.geometry("1200x700")

        self.root.resizable(False, False)

        self.root.configure(bg="#F0F4F7")

        self.cart = Cart()

        self.categories = [
            "Fruits",
            "Vegetables",
            "Dairy",
            "Drinks",
            "Snacks",
            "Bakery",
            "Frozen Food",
            "Grocery",
        ]

        self.products = [
            # Fruits
            Product(1, "Fruits", "Apple", 40, 20, "kg", 10),
            Product(2, "Fruits", "Banana", 25, 25, "kg", 0),
            Product(3, "Fruits", "Orange", 35, 18, "kg", 5),
            Product(4, "Fruits", "Mango", 60, 15, "kg", 15),
            Product(5, "Fruits", "Grapes", 75, 12, "kg", 10),
            Product(6, "Fruits", "Watermelon", 90, 8, "pcs", 5),
            # Vegetables
            Product(7, "Vegetables", "Tomato", 15, 50, "kg", 0),
            Product(8, "Vegetables", "Potato", 12, 60, "kg", 0),
            Product(9, "Vegetables", "Onion", 18, 45, "kg", 5),
            Product(10, "Vegetables", "Carrot", 22, 35, "kg", 10),
            Product(11, "Vegetables", "Cucumber", 16, 40, "kg", 0),
            Product(12, "Vegetables", "Pepper", 30, 20, "kg", 5),
            # Dairy
            Product(13, "Dairy", "Milk", 35, 30, "pcs", 0),
            Product(14, "Dairy", "Cheese", 80, 20, "pcs", 10),
            Product(15, "Dairy", "Butter", 55, 25, "pcs", 5),
            Product(16, "Dairy", "Yogurt", 18, 50, "pcs", 0),
            # Drinks
            Product(17, "Drinks", "Water", 10, 100, "pcs", 0),
            Product(18, "Drinks", "Cola", 22, 70, "pcs", 5),
            Product(19, "Drinks", "Orange Juice", 30, 50, "pcs", 10),
            Product(20, "Drinks", "Coffee", 85, 25, "box", 15),
            # Snacks
            Product(21, "Snacks", "Chips", 10, 120, "pcs", 0),
            Product(22, "Snacks", "Chocolate", 40, 60, "pcs", 10),
            Product(23, "Snacks", "Biscuit", 18, 70, "pcs", 5),
            Product(24, "Snacks", "Popcorn", 25, 40, "pcs", 0),
            # Bakery
            Product(25, "Bakery", "Bread", 15, 40, "pcs", 0),
            Product(26, "Bakery", "Croissant", 25, 25, "pcs", 5),
            # Frozen
            Product(27, "Frozen Food", "Chicken", 180, 20, "kg", 10),
            Product(28, "Frozen Food", "Beef", 260, 15, "kg", 5),
            # Grocery
            Product(29, "Grocery", "Rice", 45, 60, "kg", 0),
            Product(30, "Grocery", "Sugar", 35, 50, "kg", 0),
            Product(31, "Grocery", "Oil", 75, 30, "pcs", 10),
            Product(32, "Grocery", "Pasta", 22, 70, "pcs", 5),
        ]

        self.current_products = self.products

        self.home_screen()

    # ==========================================================
    #                 MEMBER 2
    # ==========================================================

    def clear_window(self):

        for widget in self.root.winfo_children():

            widget.destroy()

    def find_product(self, product_id):

        for product in self.products:

            if product.id == product_id:

                return product

        return None
    
    def show_all_products(self):

        self.show_products(self.products)

    # =============================
    # Sorting Support
    # =============================

    SORT_OPTIONS = [
        "Default",
        "Name (A → Z)",
        "Name (Z → A)",
        "Price (Low → High)",
        "Price (High → Low)",
        "Stock (Low → High)",
        "Stock (High → Low)",
        "Discount (Low → High)",
        "Discount (High → Low)",
    ]

    def sort_products(self, products):

        # self.sort_option remembers the user's last choice across views

        if not hasattr(self, "sort_option"):

            self.sort_option = "Default"

        option = self.sort_option

        if option == "Name (A → Z)":

            return sorted(products, key=lambda p: p.name.lower())

        elif option == "Name (Z → A)":

            return sorted(products, key=lambda p: p.name.lower(), reverse=True)

        elif option == "Price (Low → High)":

            return sorted(products, key=lambda p: p.price)

        elif option == "Price (High → Low)":

            return sorted(products, key=lambda p: p.price, reverse=True)

        elif option == "Stock (Low → High)":

            return sorted(products, key=lambda p: p.stock)

        elif option == "Stock (High → Low)":

            return sorted(products, key=lambda p: p.stock, reverse=True)

        elif option == "Discount (Low → High)":

            return sorted(products, key=lambda p: p.discount)

        elif option == "Discount (High → Low)":

            return sorted(products, key=lambda p: p.discount, reverse=True)

        else:

            return products

    def on_sort_selected(self, event=None):

        self.sort_option = self.sort_combo.get()

        self.populate_tree(self.current_products)

    def populate_tree(self, products):

        for row in self.tree.get_children():

            self.tree.delete(row)

        for product in self.sort_products(products):

            self.tree.insert(
                "",
                tk.END,
                values=(
                    product.id,
                    product.category,
                    product.name,
                    product.price,
                    f"{product.stock} {product.unit}",
                    f"{product.discount}%",
                ),
            )

    def show_products(self, products):

        self.current_products = products

        if not hasattr(self, "sort_option"):

            self.sort_option = "Default"

        self.clear_window()

        title = tk.Label(
            self.root,
            text="Available Products",
            font=("Arial", 22, "bold"),
            bg="#F0F4F7",
            fg="#2C3E50",
        )

        title.pack(pady=15)

        # =============================
        # Sort Bar
        # =============================

        sort_frame = tk.Frame(self.root, bg="#F0F4F7")

        sort_frame.pack(pady=5)

        tk.Label(
            sort_frame,
            text="Sort By:",
            font=("Arial", 12, "bold"),
            bg="#F0F4F7",
            fg="#2C3E50",
        ).grid(row=0, column=0, padx=5)

        self.sort_combo = ttk.Combobox(
            sort_frame,
            values=self.SORT_OPTIONS,
            state="readonly",
            width=22,
            font=("Arial", 11),
        )

        self.sort_combo.set(self.sort_option)

        self.sort_combo.grid(row=0, column=1, padx=5)

        self.sort_combo.bind("<<ComboboxSelected>>", self.on_sort_selected)

        self.tree = ttk.Treeview(
            self.root,
            columns=("ID", "Category", "Name", "Price", "Stock", "Discount"),
            show="headings",
            height=18,
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Name", text="Product")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Discount", text="Discount")

        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Category", width=150, anchor="center")
        self.tree.column("Name", width=220, anchor="center")
        self.tree.column("Price", width=90, anchor="center")
        self.tree.column("Stock", width=120, anchor="center")
        self.tree.column("Discount", width=100, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=20, pady=15)

        self.populate_tree(products)

        button_frame = tk.Frame(self.root, bg="#F0F4F7")

        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="➕ Add To Cart",
            width=18,
            bg="#2ECC71",
            fg="white",
            command=self.add_to_cart,
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            button_frame,
            text="⬅ Back",
            width=18,
            bg="#3498DB",
            fg="white",
            command=self.home_screen,
        ).grid(row=0, column=1, padx=10)

    def home_screen(self):

        self.sort_option = "Default"

        self.clear_window()

        title = tk.Label(
            self.root,
            text="🛒 SuperMarket Management System",
            font=("Arial", 24, "bold"),
            bg="#F0F4F7",
            fg="#2C3E50",
        )

        title.pack(pady=15)

        # =============================
        # Search Bar
        # =============================

        search_frame = tk.Frame(self.root, bg="#F0F4F7")

        search_frame.pack(pady=10)

        self.search_entry = tk.Entry(search_frame, width=35, font=("Arial", 12))

        self.search_entry.grid(row=0, column=0, padx=10)

        tk.Button(
            search_frame,
            text="🔍 Search",
            bg="#3498DB",
            fg="white",
            width=15,
            command=self.search_product,
        ).grid(row=0, column=1, padx=5)

        # =============================
        # Categories
        # =============================

        category_frame = tk.LabelFrame(
            self.root, text="Categories", font=("Arial", 13, "bold"), padx=10, pady=10
        )

        category_frame.pack(fill="x", padx=20, pady=15)

        row = 0
        col = 0

        for category in self.categories:

            tk.Button(
                category_frame,
                text=category,
                width=18,
                height=2,
                bg="#27AE60",
                fg="white",
                command=lambda c=category: self.show_products(
                    [p for p in self.products if p.category == c]
                ),
            ).grid(row=row, column=col, padx=8, pady=8)

            col += 1

            if col == 4:

                col = 0

                row += 1

        # =============================
        # Main Buttons
        # =============================

        bottom = tk.Frame(self.root, bg="#F0F4F7")

        bottom.pack(pady=20)

        tk.Button(
            bottom,
            text="📋 View All Products",
            width=22,
            height=2,
            bg="#2980B9",
            fg="white",
            command=self.show_all_products,
        ).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(
            bottom,
            text="🛒 Shopping Cart",
            width=22,
            height=2,
            bg="#8E44AD",
            fg="white",
            command=self.view_cart,
        ).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(
            bottom,
            text="📊 Statistics",
            width=22,
            height=2,
            bg="#E67E22",
            fg="white",
            command=self.statistics_menu,
        ).grid(row=1, column=0, padx=10, pady=10)

        tk.Button(
            bottom,
            text="🧾 Receipt",
            width=22,
            height=2,
            bg="#16A085",
            fg="white",
            command=self.show_receipt,
        ).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(
            self.root,
            text="Exit",
            width=20,
            bg="red",
            fg="white",
            command=self.root.destroy,
        ).pack(pady=15)

    def search_product(self):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            messagebox.showwarning("Warning", "Please Enter Product Name Or ID.")

            return

        result = []

        # Search By ID

        if keyword.isdigit():

            product = self.find_product(int(keyword))

            if product:

                result.append(product)

        # Search By Name

        else:

            for product in self.products:

                if (
                    keyword.lower() in product.name.lower()
                    or keyword.lower() in product.category.lower()
                ):

                    result.append(product)

        if len(result) == 0:

            messagebox.showerror("Not Found", "No Product Found.")

            return

        self.show_products(result)

    # ==========================================================
    #                 MEMBER 3
    # ==========================================================

    def add_to_cart(self):

        selected = self.tree.focus()

        if selected == "":

            messagebox.showwarning("Warning", "Please Select A Product.")

            return

        values = self.tree.item(selected, "values")

        product_id = int(values[0])

        product = self.find_product(product_id)

        quantity = simpledialog.askinteger("Quantity", "Enter Quantity :", minvalue=1)

        if quantity is None:

            return

        if quantity > product.stock:

            messagebox.showerror("Stock", "Not Enough Stock.")

            return

        found = False

        for item in self.cart.items:

            if item.product.id == product.id:

                item.quantity += quantity

                found = True

                break

        if not found:

            self.cart.items.append(CartItem(product, quantity))

        product.stock -= quantity

        messagebox.showinfo("Success", "Product Added To Cart Successfully.")

        self.show_products(self.current_products)

    def view_cart(self):
        if self.cart.is_empty():

            messagebox.showinfo("Cart", "Shopping Cart Is Empty.")

            self.home_screen()

            return

        self.clear_window()

        tk.Label(
            self.root,
            text="🛒 Shopping Cart",
            font=("Arial", 22, "bold"),
            bg="#F0F4F7",
            fg="#2C3E50",
        ).pack(pady=15)

        self.cart_tree = ttk.Treeview(
            self.root,
            columns=("ID", "Product", "Quantity", "Price", "Discount", "Total"),
            show="headings",
            height=15,
        )

        self.cart_tree.heading("ID", text="ID")
        self.cart_tree.heading("Product", text="Product")
        self.cart_tree.heading("Quantity", text="Qty")
        self.cart_tree.heading("Price", text="Price")
        self.cart_tree.heading("Discount", text="Discount")
        self.cart_tree.heading("Total", text="Total")

        self.cart_tree.column("ID", width=60, anchor="center")
        self.cart_tree.column("Product", width=200, anchor="center")
        self.cart_tree.column("Quantity", width=80, anchor="center")
        self.cart_tree.column("Price", width=100, anchor="center")
        self.cart_tree.column("Discount", width=100, anchor="center")
        self.cart_tree.column("Total", width=120, anchor="center")

        self.cart_tree.pack(fill="both", expand=True, padx=20, pady=10)

        for item in self.cart.items:

            self.cart_tree.insert(
                "",
                tk.END,
                values=(
                    item.product.id,
                    item.product.name,
                    item.quantity,
                    item.product.price,
                    f"{item.product.discount}%",
                    f"{item.final_price():.2f}",
                ),
            )

        total = tk.Label(
            self.root,
            text=f"Total : {self.cart.total():.2f} EGP",
            font=("Arial", 16, "bold"),
            bg="#F0F4F7",
            fg="green",
        )

        total.pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#F0F4F7")

        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="✏ Update Quantity",
            width=18,
            bg="#3498DB",
            fg="white",
            command=self.update_quantity,
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            button_frame,
            text="❌ Remove Product",
            width=18,
            bg="#E74C3C",
            fg="white",
            command=self.remove_product,
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            button_frame,
            text="🗑 Clear Cart",
            width=18,
            bg="#8E44AD",
            fg="white",
            command=self.clear_cart,
        ).grid(row=0, column=2, padx=10)

        tk.Button(
            button_frame,
            text="⬅ Back",
            width=18,
            bg="#2ECC71",
            fg="white",
            command=self.home_screen,
        ).grid(row=0, column=3, padx=10)

    def update_quantity(self):

        selected = self.cart_tree.focus()

        if selected == "":

            messagebox.showwarning("Warning", "Please Select A Product.")

            return

        values = self.cart_tree.item(selected, "values")

        product_id = int(values[0])

        for item in self.cart.items:

            if item.product.id == product_id:

                new_quantity = simpledialog.askinteger(
                    "Update Quantity", "Enter New Quantity:", minvalue=1
                )

                if new_quantity is None:

                    return

                available = item.product.stock + item.quantity

                if new_quantity > available:

                    messagebox.showerror("Stock", "Not Enough Stock.")

                    return

                item.product.stock += item.quantity
                item.product.stock -= new_quantity

                item.quantity = new_quantity

                break

        messagebox.showinfo("Updated", "Quantity Updated Successfully.")

        self.view_cart()

    def remove_product(self):

        selected = self.cart_tree.focus()

        if selected == "":

            messagebox.showwarning("Warning", "Please Select A Product.")

            return

        values = self.cart_tree.item(selected, "values")

        product_id = int(values[0])

        for item in self.cart.items[:]:

            if item.product.id == product_id:

                # Return the reserved quantity back to stock.

                item.product.stock += item.quantity

                self.cart.items.remove(item)

                break

        messagebox.showinfo("Removed", "Product Removed Successfully.")

        self.view_cart()

    def clear_cart(self):

        if self.cart.is_empty():

            messagebox.showwarning("Cart", "Shopping Cart Is Empty.")

            return

        answer = messagebox.askyesno(
            "Confirm", "Are You Sure You Want To Clear The Cart?"
        )

        if not answer:

            return

        for item in self.cart.items:

            item.product.stock += item.quantity

        self.cart.clear()

        messagebox.showinfo("Done", "Shopping Cart Cleared.")

        self.home_screen()

    # ==========================================================
    #                 MEMBER 4
    # ==========================================================

    def show_receipt(self):

        if self.cart.is_empty():

            messagebox.showwarning("Warning", "Shopping Cart Is Empty.")

            return

        self.clear_window()

        tk.Label(
            self.root,
            text="🧾 Receipt",
            font=("Arial", 24, "bold"),
            bg="#F0F4F7",
            fg="#2C3E50",
        ).pack(pady=15)

        receipt_no = datetime.now().strftime("%Y%m%d%H%M%S")

        tk.Label(
            self.root,
            text=f"Receipt No : {receipt_no}",
            font=("Arial", 12),
            bg="#F0F4F7",
        ).pack()

        tk.Label(
            self.root,
            text=f"Date : {datetime.now().strftime('%d/%m/%Y')}",
            font=("Arial", 12),
            bg="#F0F4F7",
        ).pack()

        tk.Label(
            self.root,
            text=f"Time : {datetime.now().strftime('%H:%M:%S')}",
            font=("Arial", 12),
            bg="#F0F4F7",
        ).pack(pady=(0, 15))

        tree = ttk.Treeview(
            self.root,
            columns=("Product", "Qty", "Price", "Discount", "Total"),
            show="headings",
            height=15,
        )

        tree.heading("Product", text="Product")
        tree.heading("Qty", text="Qty")
        tree.heading("Price", text="Price")
        tree.heading("Discount", text="Discount")
        tree.heading("Total", text="Total")

        tree.column("Product", width=220, anchor="center")
        tree.column("Qty", width=80, anchor="center")
        tree.column("Price", width=100, anchor="center")
        tree.column("Discount", width=100, anchor="center")
        tree.column("Total", width=120, anchor="center")

        tree.pack(fill="both", expand=True, padx=20, pady=10)

        subtotal = 0
        total_discount = 0
        final_total = 0

        for item in self.cart.items:

            subtotal += item.total_price()

            total_discount += item.discount()

            final_total += item.final_price()

            tree.insert(
                "",
                tk.END,
                values=(
                    item.product.name,
                    item.quantity,
                    f"{item.total_price():.2f}",
                    f"{item.discount():.2f}",
                    f"{item.final_price():.2f}",
                ),
            )

        summary = tk.Frame(self.root, bg="#F0F4F7")

        summary.pack(pady=10)

        tk.Label(
            summary,
            text=f"Subtotal : {subtotal:.2f} EGP",
            font=("Arial", 13, "bold"),
            bg="#F0F4F7",
        ).pack()

        tk.Label(
            summary,
            text=f"Discount : {total_discount:.2f} EGP",
            font=("Arial", 13, "bold"),
            fg="red",
            bg="#F0F4F7",
        ).pack()

        tk.Label(
            summary,
            text=f"Total : {final_total:.2f} EGP",
            font=("Arial", 16, "bold"),
            fg="green",
            bg="#F0F4F7",
        ).pack(pady=5)

        button_frame = tk.Frame(self.root, bg="#F0F4F7")

        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="💾 Save Receipt",
            width=18,
            bg="#3498DB",
            fg="white",
            command=self.save_receipt,
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            button_frame,
            text="🏠 Home",
            width=18,
            bg="#2ECC71",
            fg="white",
            command=self.finish_order,
        ).grid(row=0, column=1, padx=10)

    def save_receipt(self):

        receipt_no = datetime.now().strftime("%Y%m%d%H%M%S")

        filename = f"Receipt_{receipt_no}.txt"

        subtotal = 0
        total_discount = 0
        final_total = 0

        with open(filename, "w", encoding="utf-8") as file:

            file.write("=" * 50 + "\n")
            file.write("      SuperMarket Management System\n")
            file.write("=" * 50 + "\n\n")

            file.write(f"Receipt No : {receipt_no}\n")
            file.write(f"Date : {datetime.now().strftime('%d/%m/%Y')}\n")
            file.write(f"Time : {datetime.now().strftime('%H:%M:%S')}\n\n")

            file.write("-" * 50 + "\n")

            for item in self.cart.items:

                subtotal += item.total_price()
                total_discount += item.discount()
                final_total += item.final_price()

                file.write(
                    f"{item.product.name}\n"
                    f"Qty : {item.quantity}\n"
                    f"Price : {item.total_price():.2f}\n"
                    f"Discount : {item.discount():.2f}\n"
                    f"Total : {item.final_price():.2f}\n"
                )

                file.write("-" * 50 + "\n")

            file.write(f"\nSubtotal : {subtotal:.2f} EGP\n")
            file.write(f"Discount : {total_discount:.2f} EGP\n")
            file.write(f"Final Total : {final_total:.2f} EGP\n")

            file.write("\nThank You For Shopping With Us ❤️")

        messagebox.showinfo("Saved", f"Receipt Saved Successfully\n\n{filename}")

    def finish_order(self):

        for item in self.cart.items:

            item.product.sold += item.quantity

            item.product.revenue += item.quantity * item.product.price

        self.cart.clear()

        messagebox.showinfo("Done", "Thank You For Shopping With Us ❤️")

        self.home_screen()

    # ==========================================================
    # MEMBER 5
    # ==========================================================

    def statistics_menu(self):

        self.clear_window()

        tk.Label(
            self.root, text="📊 Statistics", font=("Arial", 24, "bold"), bg="#F0F4F7"
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Products Per Category",
            width=30,
            height=2,
            bg="#3498DB",
            fg="white",
            command=self.category_chart,
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Stock Levels",
            width=30,
            height=2,
            bg="#27AE60",
            fg="white",
            command=self.stock_chart,
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Products Sold",
            width=30,
            height=2,
            bg="#E67E22",
            fg="white",
            command=self.sold_chart,
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Revenue",
            width=30,
            height=2,
            bg="#9B59B6",
            fg="white",
            command=self.revenue_chart,
        ).pack(pady=10)

        tk.Button(self.root, text="⬅ Back", width=25, command=self.home_screen).pack(
            pady=20
        )

    # ==========================================
    # Products Per Category (Pie Chart)
    # ==========================================

    def category_chart(self):

        categories = {}

        for product in self.products:

            categories[product.category] = categories.get(product.category, 0) + 1

        plt.figure(figsize=(7, 7))

        plt.pie(
            categories.values(),
            labels=categories.keys(),
            autopct="%1.1f%%",
            startangle=90,
        )

        plt.title("Products Per Category")

        plt.axis("equal")

        plt.show()

    # ==========================================
    # Stock Levels
    # ==========================================

    def stock_chart(self):

        names = []

        stocks = []

        for product in self.products:

            names.append(product.name)

            stocks.append(product.stock)

        plt.figure(figsize=(12, 6))

        plt.bar(names, stocks, color="steelblue", edgecolor="black")

        plt.xticks(rotation=45, ha="right")

        plt.ylabel("Stock")

        plt.grid(axis="y", linestyle="--", alpha=0.5)

        plt.title("Current Stock")

        plt.tight_layout()

        plt.show()

    # ==========================================
    # Products Sold
    # ==========================================

    def sold_chart(self):

        names = []

        sold = []

        for product in self.products:

            names.append(product.name)

            sold.append(product.sold)

        plt.figure(figsize=(12, 6))

        plt.bar(names, sold, color="darkorange", edgecolor="black")

        plt.xticks(rotation=45, ha="right")

        plt.ylabel("Quantity Sold")

        plt.grid(axis="y", linestyle="--", alpha=0.5)

        plt.title("Products Sold")

        plt.tight_layout()

        plt.show()

    # ==========================================
    # Revenue
    # ==========================================

    def revenue_chart(self):

        names = []

        revenue = []

        for product in self.products:

            names.append(product.name)

            revenue.append(product.revenue)

        plt.figure(figsize=(12, 6))

        plt.bar(names, revenue, color="seagreen", edgecolor="black")

        plt.xticks(rotation=45, ha="right")

        plt.ylabel("Revenue")

        plt.grid(axis="y", linestyle="--", alpha=0.5)

        plt.title("Revenue Per Product")

        plt.tight_layout()

        plt.show()


# ==========================================================
# Run Program
# ==========================================================

if __name__ == "__main__":

    app = SuperMarketGUI()

    app.root.mainloop()
