def product_search(product_list):
    """ Function for searching for a product. Receives the list of products as an argument. """
    print("\nSearch by: Product ID, Product Name, Category")
    product_search_means = input("Enter how you would like to search: ").strip().upper()

    if product_search_means == "PRODUCT ID":
        # Search via ID
        search_product_id = input("\nEnter product ID: ").strip()
        product_id_found = False

        print("\n" + "-" * 40)
        for product in product_list:
            if product.product_id == search_product_id: 
                product.view_product()
                print("-" * 40)
                product_found = True
        
        if product_id_found == False:
            print(f"No product with ID of {search_product_id} found.")
    elif product_search_means == "PRODUCT NAME":
        # Search via name
        search_product_name = input("\nEnter product name: ").strip().upper()
        product_name_found = False

        print("\n" + "-" * 40)
        for product in product_list:
            if product.product_name.upper() == search_product_name:
                product.view_product()
                print("-" * 40)
                product_name_found = True

        if product_name_found == False:
            print(f"No product with a name of {search_product_name} found.")
    elif product_search_means == "CATEGORY":
        # Search via category
        search_category = input("\nEnter category: ").strip().upper()
        category_found = False

        print("\n" + "-" * 40)
        for product in product_list:
            if product.category.upper() == search_category:
                product.view_product()
                print("-" * 40)
                category_found = True

        if category_found == False:
            print(f"No category of {search_category} found.")
    else:
        print("\nError. Invalid search method.")

def vendor_search(vendor_list):
    """ Function for searching for a vendor. Receives the list of vendors as an argument. """
    print("\nSearch by: Vendor ID, Vendor Name, Contact Name")
    vendor_search_means = input("Enter how you would like to search: ").strip().upper()

    if vendor_search_means == "VENDOR ID":
        # Search via ID
        search_vendor_id = input("\nEnter vendor ID: ").strip()
        vendor_id_found = False

        print("\n" + "-" * 40)
        for vendor in vendor_list:
            if vendor.vendor_id == search_vendor_id:
                vendor.view_vendor()
                print("-" * 40)
                vendor_id_found = True

        if vendor_id_found == False:
            print(f"No vendor with ID of {search_vendor_id} found.")
    elif vendor_search_means == "VENDOR NAME":
        # Search via vendor name
        search_vendor_name = input("\nEnter vendor name: ").strip().upper()
        vendor_name_found = False

        print("\n" + "-" * 40)
        for vendor in vendor_list:
            if vendor.vendor_name.upper() == search_vendor_name:
                vendor.view_vendor()
                print("-" * 40)
                vendor_name_found = True

        if vendor_name_found == False:
            print(f"No vendor with a name of {search_vendor_name} found.")
    elif vendor_search_means == "CONTACT NAME":
        # Search via contact name
        search_vendor_contact_name = input("\nnter vendor contact name: ").strip().upper()
        vendor_contact_name_found = False

        print("\n" + "-" * 40)
        for vendor in vendor_list:
            if vendor.contact_name.upper() == search_vendor_contact_name:
                vendor.view_vendor()
                print("-" * 40)
                vendor_contact_name_found = True

        if vendor_contact_name_found == False:
            print(f"No vendor with a contact name of {search_vendor_contact_name} found.")
    else:
        print("\nError. Invalid search method.")

def PO_search(pending_PO_list, PO_list):
    """ Function for searching for a PO. Receives the list of pending POs and sent/stored POs as arguments. """
    print("\nSearch by: Purchase Order Number, Vendor ID, Status")
    PO_search_means = input("Enter how you would like to search: ").strip().upper()

    if PO_search_means == "PURCHASE ORDER NUMBER":
        # Search via PO number
        search_PO_number = input("Enter purchase order number: ").strip()
        PO_number_found = False

        # Search through pending POs
        print("\n" + "-" * 40)
        for pending_PO in pending_PO_list:
            if pending_PO.PO_number == search_PO_number:
                pending_PO.view_PO()
                print("-" * 40)
                PO_number_found = True

        # Search through stored POs
        for stored_PO in PO_list:
            if stored_PO.PO_number == search_PO_number:
                stored_PO.view_PO()
                print("-" * 40)
                PO_number_found = True

        if PO_number_found == False:
            print(f"No purchase order with a number of {search_PO_number} found.")
    elif PO_search_means == "VENDOR ID":
        # Search via vendor ID
        PO_search_vendor_id = input("Enter vendor ID: ").strip()
        PO_vendor_id_found = False

        # Search through pending POs
        print("\n" + "-" * 40)
        for pending_PO in pending_PO_list:
            if pending_PO.vendor_id == PO_search_vendor_id:
                pending_PO.view_PO()
                print("-" * 40)
                PO_vendor_id_found = True

        # Search through stored POs
        for stored_PO in PO_list:
            if stored_PO.vendor_id == PO_search_vendor_id:
                stored_PO.view_PO()
                print("-" * 40)
                PO_vendor_id_found = True

        if PO_vendor_id_found == False:
            print(f"No purchase order with a vendor ID of {PO_search_vendor_id} found.")
    elif PO_search_means == "STATUS":
        # Search via PO status
        search_PO_status = input("Enter purchase order status (Pending, Sent, Received): ").strip().upper()

        if search_PO_status == "PENDING":
            print("\n" + "-" * 40)
            for pending_PO in pending_PO_list:
                pending_PO.view_PO()
                print("-" * 40)
        elif search_PO_status == "SENT":
            print("\n" + "-" * 40)
            for sent_PO in PO_list:
                if sent_PO.status == "Sent":
                    sent_PO.view_PO()
                    print("-" * 40)
        elif search_PO_status == "RECEIVED":
            print("\n" + "-" * 40)
            for received_PO in PO_list:
                if received_PO.status == "Received":
                    received_PO.view_PO()
                    print("-" * 40)
        else:
            print(f"\nError. Invalid purchase order status.")
    else:
        print("\nError. Invalid search method.")