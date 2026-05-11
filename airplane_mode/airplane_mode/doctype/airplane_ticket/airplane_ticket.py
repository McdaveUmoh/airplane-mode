# Copyright (c) 2026, mcdave and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document


class AirplaneTicket(Document):
	def validate(self):
		
		seen = set()
		unique_addons = []
		duplicates = []
		for addon in self.add_ons:
			if addon.item not in seen:
				seen.add(addon.item)
				unique_addons.append(addon)

			else:
				duplicates.append(addon.item)

		if duplicates:
			frappe.msgprint(
				f"Duplicate add-ons removed: {', '.join(duplicates)}",
				indicator="orange",
				title="Duplicates Removed"
			)
		
		self.add_ons = unique_addons

		if not self.flight_price:
			frappe.throw("please provide a Flight Price")
			
		total_addons = 0
		for add_on in self.add_ons:
			total_addons += add_on.amount

		self.total_amount = total_addons + self.flight_price
		
	
	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw("Status must be boarded")

	def before_insert(self):
		self.seat = str(random.randint(1, 100)) + random.choice("ABCDE")



		


#ticket = frappe.get_doc("Airplane Ticket","Air Peace-001-ABJ-to-LAG-002")
