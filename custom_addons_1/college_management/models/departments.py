from odoo import models,fields,api


class Department(models.Model):
    _name="department.names"
    _description = "list of availabledepartment"
    _rec_name = 'name_department'

    name_department=fields.Char(string="Department Name",help="Enter the name of department")
    departmentId=fields.Integer(string="Department Id")
    course_count = fields.Integer(string='course count', compute="compute_course_count")

    @api.depends('course_count')
    def compute_course_count(self):
        count=0
        for value in self:
            if value.departmentId !=0:
                count+=1

        self.course_count = count