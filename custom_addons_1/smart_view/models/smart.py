# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class SmartView(models.Model):
    _name = 'smart.view'
    _inherit = ['mail.thread','mail.activity.mixin']


    # _description = 'Smart features practice'

    name = fields.Char(tracking=True)
    mobile_number = fields.Char()
    last_name=fields.Char()
    height = fields.Float()

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The name must be unique !')
    ]


    @api.constrains('name', 'mobile_number')
    def constrains_reconcile(self):
        for record in self:
            if record.name=="Radha" or record.name=="radha" :
                raise UserError('This user name is blocked!')
            elif not record.name.isalpha():
                raise UserError('Name must have only alphabets')

            if record.mobile_number.isalpha():
                raise ValidationError('Mobile must have only numbers')
            elif not len(record.mobile_number) == 10:
                raise ValidationError('the digits must be 10')
            # elif len(record.mobile_number) < 10:
            #     raise UserError('the digits must be 10')

    def Conferm(self):
        print("-------------------------------------->",type(self.id))
        display_message ="user confermed"
        self.message_post(body=display_message)


    def action_testing(self):
        print("------test successful-----")

