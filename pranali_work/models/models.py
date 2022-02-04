# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pranali_work(models.Model):
    _name = 'pranali_work.pranali_work'
    # _description = 'pranali_work.pranali_work'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float()
    description = fields.Text()
    age=fields.Integer()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
