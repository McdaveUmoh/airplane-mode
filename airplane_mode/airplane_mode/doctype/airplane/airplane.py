# Copyright (c) 2026, mcdave and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airplane(Document):
	def autoname(self):
		if not self.airline:
			frappe.throw("Airline is required to generate the airplane name.")
        
        # Get the last used number for this airline
		last = frappe.db.sql("""
            SELECT name FROM `tabAirplane`
            WHERE name LIKE %s
            ORDER BY name DESC
            LIMIT 1
        """, (f"{self.airline}-%",))
        
		if last:
            # Extract the number part and increment
			last_num = int(last[0][0].split("-")[-1])
			new_num = last_num + 1
		else:
			new_num = 1
        
        # Format: IndiGo-001, IndiGo-002, etc.
		self.name = f"{self.airline}-{str(new_num).zfill(3)}"
