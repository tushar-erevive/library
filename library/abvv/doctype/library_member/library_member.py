# Copyright (c) 2023, erevive and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class LibraryMember(Document):
	
	#this method will run every time a document is saved
    # def before_save(self):
    #     self.full_name = f'{self.first_name} {self.last_name or ""}'
	# pass


    # check before submitting this document
    def before_submit(self):
        exists = frappe.db.exists(
            "Library Member",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                # check if the member's end date is later than this member's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active member for this member")

        # get loan period and compute to_date by adding loan_period to from_date
        loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
        self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)