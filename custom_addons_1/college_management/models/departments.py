from odoo import models,fields

class Department(models.Model):
    _name="department.names"
    _description = "list of availabledepartment"
    _rec_name = 'name_department'

    name_department=fields.Char(string="Department Name",help="Enter the name of department")
    departmentId=fields.Integer(string="Department Id")