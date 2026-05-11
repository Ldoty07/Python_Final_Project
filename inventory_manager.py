from models import PurchaseOrder

def create_new_PO(pending_PO_list, PO_list, vendor_list):
    """ Function for creating a new PO. Receives the list of pending POs and the list of vendors as arguments. Returns the new pending PO list. """
    new_PO_number = input("Enter purchase order number: ").strip()
    vendor_id_list = []
    total_PO_list = pending_PO_list + PO_list
    PO_number_list = []

    for vendor in vendor_list:
        vendor_id_list.append(vendor.vendor_id)

    for PO in total_PO_list:
        PO_number_list.append(PO.PO_number)

    if len(total_PO_list) == 0:
        new_PO_vendor_id = input("Enter vendor id: ").strip()

        if new_PO_vendor_id not in vendor_id_list:
            print(f"Error. No vendor with ID of {new_PO_vendor_id} exists. Please add a new vendor.")
        else:
            new_PO = PurchaseOrder(new_PO_number, new_PO_vendor_id)
            pending_PO_list.append(new_PO)
            print("Purchase order successfully added.")
    else:
        if new_PO_number in PO_number_list:
            print(f"Error. Purchase order number {new_PO_number} already exists.")
        else:
            new_PO_vendor_id = input("Enter vendor id: ").strip()
            
            if new_PO_vendor_id not in vendor_id_list:
                print(f"Error. No vendor with ID of {new_PO_vendor_id} exists. Please add a new vendor.")
            else:
                new_PO = PurchaseOrder(new_PO_number, new_PO_vendor_id)
                pending_PO_list.append(new_PO)
                print("Purchase order successfully added.")

    return pending_PO_list

def add_items_to_PO(pending_PO_list, product_list):
    """ Function for adding items to a PO. Receives the list of pending POs and the list of products as arguments. """
    PO_search = input("\nEnter purchase order number: ").strip()
    PO_number_found = False
    items_added_successfully = True

    for PO in pending_PO_list:
        if PO.PO_number == PO_search:
            if PO.status == "Received":
                # Stop if the PO has been received
                print("Error. Purchase order already received.")
                items_added_successfully = False
                break
            else:
                PO.items_ordered = input("Enter items to order separated by commas: ").strip().split(",")
                product_name_list = []

                for product in product_list:
                    product_name_list.append(product.product_name.upper())

                for item in PO.items_ordered:
                    if item.upper() in product_name_list:
                        continue
                    else:
                        print("Error. One or more items not created. Please create a new product for the missing item(s).")
                        PO.items_ordered = None
                        items_added_successfully = False
                        break
            PO_number_found = True
            break

    if items_added_successfully == True:
        print("Items added to purchase order successfully.")

    if PO_number_found == False:
        print(f"Error. No pending purchase order with a number of {PO_search} found.")

def calculate_PO_cost(pending_PO_list, product_list):
    """ Function to calculate a PO's cost. Receives the list of pending POs and the list of products as arguments """
    total_cost = 0
    PO_search = input("\nEnter purchase order number: ").strip()
    PO_number_found = False

    for PO in pending_PO_list:
        if PO.PO_number == PO_search:
            for item in PO.items_ordered:
                for product in product_list:
                    if item.upper() == product.product_name.upper():
                        total_cost += product.reorder_qty * product.unit_price

            PO.total_cost = total_cost
            print(f"Total purchase order cost: ${PO.total_cost:.2f}")
            PO_number_found = True
            break

    if PO_number_found == False:
        print(f"Error. No pending purchase order with a number of {PO_search} found.")

def store_PO(pending_PO_list, PO_list):
    """ Function for storing and sending a PO. Receives the list of pending POs and the list of stored POs as arguments. 
    Returns the new pending PO list and stored PO list. """
    PO_search = input("\nEnter purchase order number: ").strip()
    PO_found = False

    for PO in pending_PO_list:
        if PO_search == PO.PO_number:
            PO.status = "Sent"
            PO_list.append(PO)
            PO_index = pending_PO_list.index(PO)
            pending_PO_list.pop(PO_index)
            print("Purchase order successfully stored and sent.")
            PO_found = True
            break

    if PO_found == False:
        print(f"No pending purchase order with a number of {PO_search} found.")

    return pending_PO_list, PO_list

def mark_PO_received(PO_list, product_list):
    """ Function for marking a PO as received. Receives the list of stored POs and the list of products as arguments. """
    PO_search = input("\nEnter purchase order number: ").strip()
    PO_number_found = False

    for PO in PO_list:
        if PO.PO_number == PO_search:
            # Stop if the PO has been received
            if PO.status == "Received":
                print("Error. Purchase order already marked as received.")
                break
            else:
                for item in PO.items_ordered:
                    for product in product_list:
                        if item.upper() == product.product_name.upper():
                            product.qty_in_stock += product.reorder_qty
                            
                PO.status = "Received"
            PO_number_found = True
            break

    if PO_number_found == False:
        print(f"Error. No purchase order with a number of {PO_search} found.")