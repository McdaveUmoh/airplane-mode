import random
import frappe


def execute():
    tickets = frappe.get_all("Airplane Ticket", filters={"seat": ""}, fields=["name"])
    
    for ticket in tickets:
        seat = str(random.randint(1, 100)) + random.choice("ABCDE")
        frappe.db.set_value("Airplane Ticket", ticket.name, "seat", seat)
    
    frappe.db.commit()