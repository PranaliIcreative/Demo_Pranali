from odoo import models,fields

class DepartmentCourseSubject(models.Model):
    _name="department.course.subject"
    _description = "list of available department courses"
    _rec_name = 'subject_name'
    department_name_subject_id=fields.Many2one(comodel_name='department.names',string='Department')
    departmentId_subject_id=fields.Integer(string='Department Id',
                                           related='department_name_subject_id.departmentId')
    course_subject_id=fields.Many2one(comodel_name='department.course', string='Course', domain="[('department_name_course_id', '=', department_name_subject_id)]")

    # Department_Course_ids=fields.Reference([('department.names','Department'),
    #                                         ('department.course','Course')],String='Subject')
    courseId_subject_id=fields.Integer(string='Course Id',
                                           related='course_subject_id.department_courseId')
    subject_name=fields.Char(string='Subject Name')
    CourseId=fields.Integer(string='Course ID',help="course id must not be 0")
    user_signature = fields.Binary(string='Signature', required='1')
