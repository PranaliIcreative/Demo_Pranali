# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class SmartView(models.Model):
    _name = 'smart.view'

    # _description = 'Smart features practice'

    name = fields.Char()
    mobile_number = fields.Char()
    height = fields.Float()

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The name must be unique !')
    ]


    @api.constrains('name')
    def constrains_reconcile(self):
        for record in self:
            if record.name=="Radha" or record.name=="radha" :
                raise UserError('This user name is blocked!')

    @api.constrains('mobile_number')
    def constrain_mobileno(self):
        for record in self:
            if record.name.isalpha() != True:
                raise UserError('Name must have only alphabets')
            if len(record.mobile_number)>10:
                raise UserError('the digits must be 10')
            elif len(record.mobile_number)<10:
                raise UserError('the digits must be 10')


    def action_testing(self):
        print("------test successful-----")

