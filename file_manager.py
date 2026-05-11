import json
import datetime

from models import Product
from models import Vendor
from models import PurchaseOrder

# Save data

def save_product_data(product_list):
    """ Function for saving product data. Receives the list of products as an argument. """
    dict_product_list = []

    for product in product_list:
        product_dict = product.convert_to_dict()
        dict_product_list.append(product_dict)

    with open("sample_product_data.json", "w") as sample_product_data:
        json.dump(dict_product_list, sample_product_data)

def save_vendor_data(vendor_list):
    """ Function for saving vendor data. Receives the list of vendors as arguments. """
    dict_vendor_list = []

    for vendor in vendor_list:
        vendor_dict = vendor.convert_to_dict()
        dict_vendor_list.append(vendor_dict)

    with open("sample_vendor_data.json", "w") as sample_vendor_data:
        json.dump(dict_vendor_list, sample_vendor_data)

def save_pending_PO_data(pending_PO_list):
    """ Function for saving pending PO data. Receives the list of pending POs as arguments. """
    dict_pending_PO_list = []

    for pending_PO in pending_PO_list:
        pending_PO_dict = pending_PO.convert_to_dict()
        dict_pending_PO_list.append(pending_PO_dict)

    with open("sample_pending_PO_data.json", "w") as sample_pending_PO_data:
        json.dump(dict_pending_PO_list, sample_pending_PO_data)

def save_PO_data(PO_list):
    """ Function for saving PO data. Receives the list of POs as arguments. """
    dict_PO_list = []

    for PO in PO_list:
        PO_dict = PO.convert_to_dict()
        dict_PO_list.append(PO_dict)

    with open("sample_PO_data.json", "w") as sample_PO_data:
        json.dump(dict_PO_list, sample_PO_data)

# Load data

def load_product_data():
    """ Function for loading product data. Returns the new product list. """
    with open("sample_product_data.json", "r") as sample_product_data:
        dict_product_list = json.load(sample_product_data)

    product_list = []

    # Convert dict to class
    for product_dict in dict_product_list:
        new_product = Product()

        new_product.product_id = product_dict["product_id"]
        new_product.product_name = product_dict["product_name"]
        new_product.category = product_dict["category"]
        new_product.qty_in_stock = product_dict["qty_in_stock"]
        new_product.reorder_lvl = product_dict["reorder_lvl"]
        new_product.reorder_qty = product_dict["reorder_qty"]
        new_product.unit_price = product_dict["unit_price"]
        new_product.vendor_id = product_dict["vendor_id"]
        new_product.is_active = product_dict["is_active"]

        product_list.append(new_product)        

    return product_list

def load_vendor_data():
    """ Function for loading vendor data. Returns the new vendor list. """
    with open("sample_vendor_data.json", "r") as sample_vendor_data:
        dict_vendor_list = json.load(sample_vendor_data)

    vendor_list = []

    # Convert dict to class
    for vendor_dict in dict_vendor_list:
        new_vendor = Vendor()

        new_vendor.vendor_id = vendor_dict["vendor_id"]
        new_vendor.vendor_name = vendor_dict["vendor_name"]
        new_vendor.contact_name = vendor_dict["contact_name"]
        new_vendor.phone = vendor_dict["phone"]
        new_vendor.email = vendor_dict["email"]
        new_vendor.city = vendor_dict["city"]
        new_vendor.state = vendor_dict["state"]

        vendor_list.append(new_vendor)

    return vendor_list

def load_pending_PO_data():
    """ Function for loading pending PO data. Returns the new pending PO list. """
    with open("sample_pending_PO_data.json", "r") as sample_pending_PO_data:
        dict_pending_PO_list = json.load(sample_pending_PO_data)

    pending_PO_list = []

    # Convert dict to class
    for pending_PO_dict in dict_pending_PO_list:
        new_pending_PO = PurchaseOrder(pending_PO_dict["PO_number"], pending_PO_dict["vendor_id"])

        new_pending_PO.date_created = datetime.datetime.fromisoformat(pending_PO_dict["date_created"])
        new_pending_PO.items_ordered = pending_PO_dict["items_ordered"]
        new_pending_PO.total_cost = pending_PO_dict["total_cost"]
        new_pending_PO.status = pending_PO_dict["status"]

        pending_PO_list.append(new_pending_PO)

    return pending_PO_list

def load_PO_data():
    """ Function for loading PO data. Returns the new PO list. """
    with open("sample_PO_data.json", "r") as sample_PO_data:
        dict_PO_list = json.load(sample_PO_data)

    PO_list = []

    # Convert dict to class
    for PO_dict in dict_PO_list:
        new_PO = PurchaseOrder(PO_dict["PO_number"], PO_dict["vendor_id"])

        new_PO.date_created = datetime.datetime.fromisoformat(PO_dict["date_created"])
        new_PO.items_ordered = PO_dict["items_ordered"]
        new_PO.total_cost = PO_dict["total_cost"]
        new_PO.status = PO_dict["status"]

        PO_list.append(new_PO)

    return PO_list