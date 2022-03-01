# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.tools.populate import compute


class pranali_work(models.Model):
    _name = 'pranali_work.pranali_work'
    _rec_name = 'description'
    # _description = 'pranali_work.pranali_work'

    f_name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc" , store=False)
    description = fields.Text()
    age=fields.Integer()
    test_date1 = fields.Date(string='Test Date1')
    test_date2 = fields.Date(string='Test Date2')
    creation_date = fields.Datetime(string='Creation Date',default=fields.Datetime.now)
    rating_avg = fields.Selection([(' ',' '),
                                   ('poor','Poor'),
                                   ('bad','Bad'),
                                   ('average','Average'),
                                   ('good','Good'),
                                   ('very_good','Very Good'),
                                   ('excellent','Excellent')],string="Rating")
    f_name_id=fields.Many2many('res.partner.category','f_name_table',String='worker name')
    # sale_order_ids = fields.Many2many('sale.order', 'sale_order_transaction_rel', 'transaction_id', 'sale_order_id',
    #                                   string='Sales Orders', copy=False, readonly=True)
    status =fields.Selection([('default','Default'),('registered','Registered'),('in_process','In Process'),('testing','Testing'),('completed','Completed')], default='default')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def demo_button(self):
        print("object button created successfully")