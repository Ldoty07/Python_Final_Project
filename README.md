Inventory Management and PO System

This program creates a system for managing products, vendors, and purchase orders for a business.

Features include:
    Adding a product
    Viewing products
    Searching for products
    Editing a product
    Deactivating a product
    Viewing low-stock products
    Estimating the cost to restock inventory
    Sorting products by ID
    Exporting full inventory and low-stock reports to Excel

    Adding a vendor
    Viewing vendors
    Searching for vendors
    Editing a vendor
    Sorting vendors by ID

    Creating a PO
    Adding products to a PO
    Calculating a PO total
    Storing and sending a PO
    Viewing all POs
    Marking a PO as received
    Searching for POs
    Sorting POs by number
    Exporting an open PO report to Excel

Required files:
    main.py
    models.py
    inventory_manager.py
    file_manager.py
    reports.py
    sample_product_data.json
    sample_vendor_data.json
    sample_PO_data.json
    sample_pending_PO_data.json

To run the program, download all the necessary files in the same folder. Open main.py and run the program.

Data is mainly stored in lists. On execution, the program will load saved data from the json files.

I included the extra feature of calculating the cost to restock the entire inventory. The program will run through the products and calculate how much it will cost to fully restock every low stock item.

Lily Doty
ITT-070-54197