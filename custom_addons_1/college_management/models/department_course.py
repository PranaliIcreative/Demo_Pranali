from odoo import models,fields,api
from odoo.tools.populate import compute


class Department_course(models.Model):
    _name="department.course"
    _description = "list of available department courses"
    _rec_name = 'department_course'

    department_name_course_id=fields.Many2one(comodel_name='department.names',string='Department')
    departmentId_course_id=fields.Integer(string='Department Id',  related='department_name_course_id.departmentId',)
    department_course=fields.Char(string="Course Name",help="Enter the name of department")
    department_courseId=fields.Integer(string="Course Id")

