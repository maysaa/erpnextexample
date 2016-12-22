from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

# def new_person(doc,method):
#     frappe.get_doc({"doctype":"Person", "pname":doc.pname,"age":doc.age,"notes":doc.notes}).insert()


def save_person(doc,method):
    if int(doc.age)>20:
        frappe.get_doc({"doctype":"shadow", "person_name":doc.person_name,"age":doc.age}).insert()

def filterPerson(test):
    return "age<20"
