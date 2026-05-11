# Import classes and functions

# models.py
from models import Product
from models import Vendor

# functions.py
from functions import product_search
from functions import vendor_search
from functions import PO_search

# inventory_manager.py
from inventory_manager import create_new_PO
from inventory_manager import add_items_to_PO
from inventory_manager import calculate_PO_cost
from inventory_manager import store_PO
from inventory_manager import mark_PO_received

# file_manager.py
from file_manager import save_product_data
from file_manager import save_vendor_data
from file_manager import save_pending_PO_data
from file_manager import save_PO_data
from file_manager import load_product_data
from file_manager import load_vendor_data
from file_manager import load_pending_PO_data
from file_manager import load_PO_data

# reports.py
from reports import full_inventory_report
from reports import low_stock_report
from reports import open_PO_report

# Import attrgetter for sorting
from operator import attrgetter

#----------------------------------------------------------------------------------------

# Define menu functions

def main_menu():
    """ Prints the main menu options """
    print("\n1. Manage Products")
    print("2. Manage Vendors")
    print("3. Manage Purchase Orders")
    print("4. Exit program")

def product_management_menu():
    """ Prints the product management menu options """
    print("\n1. Add a product")
    print("2. View all products")
    print("3. Search for products")
    print("4. Edit a product")
    print("5. Deactivate a product")
    print("6. Display low-stock products")
    print("7. Restock cost estimator")
    print("8. Sort products by ID")
    print("9. Create full inventory report and export to Excel")
    print("10. Create low stock report and export to Excel")
    print("11. Exit to main menu")

def vendor_management_menu():
    """ Prints the vendor management menu options """
    print("\n1. Add a vendor")
    print("2. View all vendors")
    print("3. Search for vendors")
    print("4. Edit a vendor")
    print("5. Sort vendors by ID")
    print("6. Exit to main menu")

def PO_management_menu():
    """ Prints the PO management menu options """
    print("\n1. Create a purchase order")
    print("2. Add products to a purchase order")
    print("3. Calculate a purchase order total")
    print("4. Store and send a purchase order")
    print("5. View all purchase orders")
    print("6. Mark a purchase order as received")
    print("7. Search for purchase orders")
    print("8. Sort purchase orders by number")
    print("9. Create open purchase order report and export to Excel")
    print("10. Exit to main menu")

#----------------------------------------------------------------------------------------

# Start the main program

product_list = []
vendor_list = []
pending_PO_list = []
PO_list = []

sorted_product_list = []
sorted_vendor_list = []
sorted_PO_list = []

# Load data
product_list = load_product_data()
vendor_list = load_vendor_data()
#pending_PO_list = load_pending_PO_data()
PO_list = load_PO_data()

# Start the main loop for the program
while True:
    main_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        # Loop for product management
        product_management_menu()
        choice = input("Enter your choice: ").strip()

        while True:
            if choice == "1":
                # Add a new product
                new_product = Product()

                new_product_id = input("\nEnter product ID: ").strip()
                vendor_id_list = []
                product_id_list = []

                for vendor in vendor_list:
                    vendor_id_list.append(vendor.vendor_id)

                for product in product_list:
                    product_id_list.append(product.product_id)

                if len(product_list) == 0:
                    new_vendor_id = input("Enter vendor ID: ").strip()
                    
                    if new_vendor_id in vendor_id_list:
                        new_product.add_product(new_product_id, new_vendor_id)
                        product_list.append(new_product)
                        print("Product successfully added.")
                    else:
                        print(f"Error. No vendor with ID of {new_vendor_id}. Please add a new vendor.")
                else:
                    if new_product_id in product_id_list:
                        print(f"Error. Product ID of {new_product_id} already exists.")
                        break
                    else:
                        new_vendor_id = input("Enter vendor ID: ").strip()
                    
                    if new_vendor_id in vendor_id_list:
                        new_product.add_product(new_product_id, new_vendor_id)
                        product_list.append(new_product)
                        print("Product successfully added.")
                    else:
                        print(f"Error. No vendor with ID of {new_vendor_id}. Please add a new vendor.")
                break
            elif choice == "2":
                # View all products
                print("\n" + "-" * 40)
                for product in product_list:
                    product.view_product()
                    print("-" * 40)
                break
            elif choice == "3":
                # Search for a product
                product_search(product_list)
                break
            elif choice == "4":
                # Edit a product
                product_to_edit = input("\nEnter product ID: ").strip()
                product_found = False

                for product in product_list:
                    if product_to_edit == product.product_id:
                        product.edit_product()
                        product_found = True

                if product_found == False:
                    print(f"No product with ID of {product_to_edit} found.")
                break
            elif choice == "5":
                # Deactivate a product
                product_to_deactivate = input("\nEnter product ID: ").strip()
                product_found = False

                for product in product_list:
                    if product_to_deactivate == product.product_id:
                        product.deactivate_product()
                        product_found = True

                if product_found == False:
                    print(f"No product with ID of {product_to_deactivate} found.")
                break
            elif choice == "6":
                # View low stock products
                low_stock_products_present = False

                print("\n" + "-" * 40)
                for product in product_list:
                    if product.qty_in_stock < product.reorder_lvl:
                        product.view_product()
                        print("-" * 40)
                        low_stock_products_present = True

                if low_stock_products_present == False:
                    print("No low stock products.")
                break
            elif choice == "7":
                # Restock cost estimator
                low_stock_products_present = False
                restock_cost = 0

                for product in product_list:
                    if product.qty_in_stock < product.reorder_lvl:
                        restock_cost += product.reorder_qty * product.unit_price
                        low_stock_products_present = True

                if low_stock_products_present == False:
                    print("No low stock products.")
                else:
                    print(f"Restock cost estimation: ${restock_cost:,.2f}")
                break
            elif choice == "8":
                # Sort products by ID and print data
                sorted_product_list = sorted(product_list, key=attrgetter("product_id"))

                print("\n" + "-" * 40)
                for product in sorted_product_list:
                    product.view_product()
                    print("-" * 40)
                break
            elif choice == "9":
                # Export full inventory report to Excel
                full_inventory_report(product_list)
                break
            elif choice == "10":
                # Export low stock report to Excel
                low_stock_report(product_list)
                break
            elif choice == "11":
                # Exit the product management loop
                break
            else:
                print("\nError. Invalid menu option.")
                break
    elif choice == "2":
        # Loop for vendor management
        vendor_management_menu()
        choice = input("Enter your choice: ").strip()

        while True:
            if choice == "1":
                # Add a new vendor
                new_vendor = Vendor()

                new_vendor_id = input("\nEnter vendor ID: ").strip()
                vendor_id_list = []

                for vendor in vendor_list:
                    vendor_id_list.append(vendor.vendor_id)

                if len(vendor_list) == 0:
                    new_vendor.add_vendor(new_vendor_id)
                    vendor_list.append(new_vendor)
                    print("Vendor successfully added.")
                else:
                    if new_vendor_id in vendor_id_list:
                        print(f"Error. Vendor ID of {new_vendor_id} already exists.")
                        break
                    else:
                        new_vendor.add_vendor(new_vendor_id)
                        vendor_list.append(new_vendor)
                        print("Vendor successfully added.")
                break
            elif choice == "2":
                # View all vendors
                print("\n" + "-" * 40)
                for vendor in vendor_list:
                    vendor.view_vendor()
                    print("-" * 40)
                break
            elif choice == "3":
                # Search for a vendor
                vendor_search(vendor_list)
                break
            elif choice == "4":
                # Edit a vendor
                vendor_to_edit = input("\nEnter vendor ID: ").strip()
                vendor_found = False

                for vendor in vendor_list:
                    if vendor_to_edit == vendor.vendor_id:
                        vendor.edit_vendor()
                        vendor_found = True

                if vendor_found == False:
                    print(f"No vendor with ID of {vendor_to_edit} found.")
                break
            elif choice == "5":
                # Sort vendors by ID and print data
                sorted_vendor_list = sorted(vendor_list, key=attrgetter("vendor_id"))

                print("\n" + "-" * 40)
                for vendor in sorted_vendor_list:
                    vendor.view_vendor()
                    print("-" * 40)
                break
            elif choice == "6":
                # Exit the vendor management loop
                break
            else:
                print("\nError. Invalid menu option.")
                break
    elif choice == "3":
        # Loop for PO management
        PO_management_menu()
        choice = input("Enter your choice: ").strip()

        while True:
            if choice == "1":
                # Create a new PO
                pending_PO_list = create_new_PO(pending_PO_list, PO_list, vendor_list)
                break
            elif choice == "2":
                # Add products to a PO
                add_items_to_PO(pending_PO_list, product_list)
                break
            elif choice == "3":
                # Calculate PO total
                calculate_PO_cost(pending_PO_list, product_list)
                break
            elif choice == "4":
                # Store and send a PO
                pending_PO_list, PO_list = store_PO(pending_PO_list, PO_list)
                break
            elif choice == "5":
                # View all POs

                # Print pending POs
                print("\n" + "-" * 40)
                print("Pending purchase orders:")
                print("-" * 40)
                for pending_PO in pending_PO_list:
                    pending_PO.view_PO()
                    print("-" * 40)

                # Print stored POs                
                print("Sent/Received purchase orders:")
                print("-" * 40)
                for PO in PO_list:
                    PO.view_PO()
                    print("-" * 40)
                break
            elif choice == "6":
                # Mark a PO as received
                mark_PO_received(PO_list, product_list)
                break
            elif choice == "7":
                # Search for a PO
                PO_search(pending_PO_list, PO_list)
                break
            elif choice == "8":
                # Sort POs by number and print data
                total_PO_list = pending_PO_list + PO_list
                sorted_PO_list = sorted(total_PO_list, key=attrgetter("PO_number"))

                print("\n" + "-" * 40)
                for PO in sorted_PO_list:
                    PO.view_PO()
                    print("-" * 40)
                break
            elif choice == "9":
                # Export open PO report to Excel
                open_PO_report(pending_PO_list, PO_list)
                break
            elif choice == "10":
                # Exit the PO management loop
                break
            else:
                print("\nError. Invalid menu option.")
                break
    elif choice == "4":
        # Exit the program
        save_product_data(product_list)
        save_vendor_data(vendor_list)
        save_pending_PO_data(pending_PO_list)
        save_PO_data(PO_list)
        break
    else:
        print("\nError. Invalid menu option.")