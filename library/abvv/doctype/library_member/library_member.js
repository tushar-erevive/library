// Copyright (c) 2023, erevive and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Library Member', {
// 	// refresh: function(frm) {

// 	// }
// });


frappe.ui.form.on('Library Member', {
	refresh: function (frm) {
		frm.add_custom_button('Create Member', () => {
			frappe.new_doc('Library Member', {
				library_member: frm.doc.name
			})
		})
		frm.add_custom_button('Create Transaction', () => {
			frappe.new_doc('Library transaction', {
				library_member: frm.doc.name
			})
		})
	}
});
