# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class pranali_work(models.Model):
    _name = 'pranali_work.pranali_work'
    _rec_name = 'description'
    # _description = 'pranali_work.pranali_work'

    name = fields.Char()
    Age = fields.Integer()
    height = fields.Float()

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The name must be unique !')
    ]


    @api.constrains('name')
    def _constrains_reconcile(self):
        for record in self:
            if record.name=="Radha":
                raise UserError('This user name is blocked!')


