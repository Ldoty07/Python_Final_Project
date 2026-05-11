import datetime

class Product:
    """ Class to handle products """
    def __init__(self):
        """ Declare attributes """
        self.product_id = None
        self.product_name = None
        self.category = None
        self.qty_in_stock = 0
        self.reorder_lvl = 0
        self.reorder_qty = 0
        self.unit_price = 0
        self.vendor_id = None
        self.is_active = True

    def add_product(self, product_id, vendor_id):
        """ Function to add a new product """
        self.product_id = product_id
        self.product_name = input("Enter product name: ").strip()
        self.category = input("Enter category: ").strip()

        # Validate int input
        while True:
            self.qty_in_stock_text = input("Enter the amount in stock: ").strip()

            try:
                self.qty_in_stock = int(self.qty_in_stock_text)
                break
            except:
                print("Invalid input. Please enter a valid amount.")

        # Validate positive number
        while self.qty_in_stock < 0:
            print("Error. Input cannot be negative.")

            # Validate int input
            while True:
                self.qty_in_stock_text = input("Enter the amount in stock: ").strip()

                try:
                    self.qty_in_stock = int(self.qty_in_stock_text)
                    break
                except:
                    print("Invalid input. Please enter a valid amount.")
        
        # Validate int input
        while True:
            self.reorder_lvl_text = input("Enter reorder level: ").strip()

            try:
                self.reorder_lvl = int(self.reorder_lvl_text)
                break
            except:
                print("Invalid input. Please enter a valid reorder level.")
        
        # Validate positive number
        while self.reorder_lvl < 0:
            print("Error. Input cannot be negative.")

            # Validate int input
            while True:
                self.reorder_lvl_text = input("Enter reorder level: ").strip()

                try:
                    self.reorder_lvl = int(self.reorder_lvl_text)
                    break
                except:
                    print("Invalid input. Please enter a valid reorder level.")
        
        # Validate int input
        while True:
            self.reorder_qty_text = input("Enter reorder quantity: ").strip()

            try:
                self.reorder_qty = int(self.reorder_qty_text)
                break
            except:
                print("Invalid input. Please enter a valid reorder quantity.")

        # Validate positive number
        while self.reorder_qty < 0:
            print("Error. Input cannot be negative.")

            # Validate int input
            while True:
                self.reorder_qty_text = input("Enter reorder quantity: ").strip()

                try:
                    self.reorder_qty = int(self.reorder_qty_text)
                    break
                except:
                    print("Invalid input. Please enter a valid reorder quantity.")

        # Validate float input
        while True:
            self.unit_price_text = input("Enter unit price: ").strip()

            try:
                self.unit_price = float(self.unit_price_text)
                break
            except:
                print("Invalid input. Please enter a valid unit price.")

        # Validate positive number
        while self.unit_price < 0:
            print("Error. Input cannot be negative.")

            # Validate float input
            while True:
                self.unit_price_text = input("Enter unit price: ").strip()

                try:
                    self.unit_price = float(self.unit_price_text)
                    break
                except:
                    print("Invalid input. Please enter a valid unit price.")

        self.vendor_id = vendor_id

    def view_product(self):
        """ Function for printing product data """
        print(f"{"Product ID:":<30} {self.product_id}")
        print(f"{"Product Name:":<30} {self.product_name}")
        print(f"{"Category:":<30} {self.category}")
        print(f"{"Quantity In Stock:":<30} {self.qty_in_stock}")
        print(f"{"Reorder Level:":<30} {self.reorder_lvl}")
        print(f"{"Reorder Quantity:":<30} {self.reorder_qty}")
        print(f"{"Unit Price:":<30} ${self.unit_price:.2f}")
        print(f"{"Vendor ID:":<30} {self.vendor_id}")
        if self.is_active:
            print(f"{"Status:":<30} Active")
        else:
            print(f"{"Status:":<30} Inactive")

    def edit_product(self):
        """ Function for editing product data """

        # Get what attribute to edit
        print("\nAttributes: Product ID, Product Name, Category, Quantiy in stock, Reorder Level, Reorder Quantity, Unit Price, Vendor ID")
        product_attribute_edit = input("Enter the attribute to edit: ").upper()

        # Replace attribute
        if product_attribute_edit == "PRODUCT ID":
            self.product_id = input("Enter product ID: ").strip()
        elif product_attribute_edit == "PRODUCT NAME":
            self.product_name = input("Enter product name: ").strip()
        elif product_attribute_edit == "CATEGORY":
            self.category = input("Enter category: ").strip()
        elif product_attribute_edit == "QUANTITY IN STOCK":
            # Validate int input
            while True:
                self.qty_in_stock_text = input("Enter the amount in stock: ").strip()

                try:
                    self.qty_in_stock = int(self.qty_in_stock_text)
                    break
                except:
                    print("Invalid input. Please enter a valid amount.")

            # Validate positive number
            while self.qty_in_stock < 0:
                print("Error. Input cannot be negative.")

                # Validate int input
                while True:
                    self.qty_in_stock_text = input("Enter the amount in stock: ").strip()

                    try:
                        self.qty_in_stock = int(self.qty_in_stock_text)
                        break
                    except:
                        print("Invalid input. Please enter a valid amount.")
        elif product_attribute_edit == "REORDER LEVEL":
            # Validate int input
            while True:
                self.reorder_lvl_text = input("Enter reorder level: ").strip()

                try:
                    self.reorder_lvl = int(self.reorder_lvl_text)
                    break
                except:
                    print("Invalid input. Please enter a valid reorder level.")

            # Validate positive number
            while self.reorder_lvl < 0:
                print("Error. Input cannot be negative.")

                # Validate int input
                while True:
                    self.reorder_lvl_text = input("Enter reorder level: ").strip()

                    try:
                        self.reorder_lvl = int(self.reorder_lvl_text)
                        break
                    except:
                        print("Invalid input. Please enter a valid reorder level.")
        elif product_attribute_edit == "REORDER QUANTITY":
            # Validate int input
            while True:
                self.reorder_qty_text = input("Enter reorder quantity: ").strip()

                try:
                    self.reorder_qty = int(self.reorder_qty_text)
                    break
                except:
                    print("Invalid input. Please enter a valid reorder quantity.")

            # Validate positive number
            while self.reorder_qty < 0:
                print("Error. Input cannot be negative.")

                # Validate int input
                while True:
                    self.reorder_qty_text = input("Enter reorder quantity: ").strip()

                    try:
                        self.reorder_qty = int(self.reorder_qty_text)
                        break
                    except:
                        print("Invalid input. Please enter a valid reorder quantity.")
        elif product_attribute_edit == "UNIT PRICE":
            # Validate float input
            while True:
                self.unit_price_text = input("Enter unit price: ").strip()

                try:
                    self.unit_price = float(self.unit_price_text)
                    break
                except:
                    print("Invalid input. Please enter a valid unit price.")

            # Validate positive number
            while self.unit_price < 0:
                print("Error. Input cannot be negative.")

                # Validate float input
                while True:
                    self.unit_price_text = input("Enter unit price: ").strip()

                    try:
                        self.unit_price = float(self.unit_price_text)
                        break
                    except:
                        print("Invalid input. Please enter a valid unit price.")
        elif product_attribute_edit == "VENDOR ID":
            self.vendor_id = input("Enter vendor ID: ").strip()
        else:
            print(f"Error. No attribute called {product_attribute_edit}.")

    def deactivate_product(self):
        """ Function for deactivating a product """
        self.is_active = False
        print("\nProduct successfully deactivated.")

    def convert_to_dict(self):
        """ Function for converting class data to a dict for saving. Returns the dict. """
        product_dict = {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "category": self.category,
            "qty_in_stock": self.qty_in_stock,
            "reorder_lvl": self.reorder_lvl,
            "reorder_qty": self.reorder_qty,
            "unit_price": self.unit_price,
            "vendor_id": self.vendor_id,
            "is_active": self.is_active,
        }

        return product_dict

#----------------------------------------------------------------------------------------

class Vendor:
    """ Class to handle vendors """
    def __init__(self):
        """ Declare attributes """
        self.vendor_id = None
        self.vendor_name = None
        self.contact_name = None
        self.phone = None
        self.email = None
        self.city = None
        self.state = None

    def add_vendor(self, vendor_id):
        """ Function for adding a new vendor. Receives the vendor ID after validating that the ID is unique. """
        self.vendor_id = vendor_id
        self.vendor_name = input("Enter vendor name: ").strip()
        self.contact_name = input("Enter contact name: ").strip()
        self.phone = input("Enter vendor phone number: ").strip()
        self.email = input("Enter vendor email: ").strip()
        self.city = input("Enter city: ").strip()
        self.state = input("Enter state: ").strip()

    def view_vendor(self):
        """ Function for printing vendor data """
        print(f"{"Vendor ID:":<30} {self.vendor_id}")
        print(f"{"Vendor Name:":<30} {self.vendor_name}")
        print(f"{"Contact Name:":<30} {self.contact_name}")
        print(f"{"Vendor Phone Number:":<30} {self.phone}")
        print(f"{"Vendor Email:":<30} {self.email}")
        print(f"{"Vendor City:":<30} {self.city}")
        print(f"{"Vendor State:":<30} {self.state}")

    def edit_vendor(self):
        """ Function for editing vendor data """

        # Get what attribute to edit
        print("\nAttributes: Vendor ID, Vendor Name, Contact Name, Vendor Phone Number, Vendor Email, Vendor City, Vendor State")
        vendor_attribute_edit = input("Enter the attribute to edit: ").strip().upper()

        if vendor_attribute_edit == "VENDOR ID":
            self.vendor_id = input("\nEnter vendor ID: ").strip()
        elif vendor_attribute_edit == "VENDOR NAME":
            self.vendor_name = input("Enter vendor name: ").strip()
        elif vendor_attribute_edit == "CONTACT NAME":
            self.contact_name = input("Enter contact name: ").strip()
        elif vendor_attribute_edit == "VENDOR PHONE NUMBER":
            self.phone = input("Enter vendor phone number: ").strip()
        elif vendor_attribute_edit == "VENDOR EMAIL":
            self.email = input("Enter vendor email: ").strip()
        elif vendor_attribute_edit == "VENDOR CITY":
            self.city = input("Enter city: ").strip()
        elif vendor_attribute_edit == "VENDOR STATE":
            self.state = input("Enter state: ").strip()
        else:
            print(f"Error. No attribute called {vendor_attribute_edit}.")

    def convert_to_dict(self):
        """ Function for converting class data to a dict for saving. Returns the dict. """
        vendor_dict = {
            "vendor_id": self.vendor_id,
            "vendor_name": self.vendor_name,
            "contact_name": self.contact_name,
            "phone": self.phone,
            "email": self.email,
            "city": self.city,
            "state": self.state,
        }

        return vendor_dict

#----------------------------------------------------------------------------------------

class PurchaseOrder:
    """ Class to handle POs """
    def __init__(self, PO_number, vendor_id):
        """ Declare attributes. Receives PO number and vendor id as arguments. """
        self.PO_number = PO_number
        self.vendor_id = vendor_id
        self.date_created = datetime.datetime.now() # Set date created to user's current date
        self.items_ordered = None
        self.total_cost = 0
        self.status = "Pending"

    def view_PO(self):
        """ Function for printing PO data """
        print(f"{"PO Number:":<30} {self.PO_number}")
        print(f"{"Vendor ID:":<30} {self.vendor_id}")
        print(f"{"Date Created:":<30} {self.date_created.strftime("%x")}") # Format the date to be more human friendly
        print("Items Ordered:")
        for item in self.items_ordered:
            print(f"\t{item}")
        print(f"{"Total Cost:":<30} ${self.total_cost:.2f}")
        print(f"{"Status:":<30} {self.status}")

    def convert_to_dict(self):
        """ Function for converting class data to a dict for saving. Returns the dict. """
        PO_dict = {
            "PO_number": self.PO_number,
            "vendor_id": self.vendor_id,
            "date_created": self.date_created.isoformat(),
            "items_ordered": self.items_ordered,
            "total_cost": self.total_cost,
            "status": self.status,
        }

        return PO_dict