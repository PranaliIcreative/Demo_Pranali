from odoo import models, fields, api



class wizardDemo(models.TransientModel):
    _name = 'wizard.demo'

    name_wizard = fields.Char(string='Name')

    def submit_button(self):
        print("object button created successfully")

    def cancel_button(self):
        print("object button created successfully")
