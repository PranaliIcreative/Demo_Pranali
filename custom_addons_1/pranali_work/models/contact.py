# -*- coding: utf-8 -*-
import string

from odoo import models, fields, api
from datetime import datetime
from odoo.tools.populate import compute


class SaleOrder(models.Model):
    _inherit = 'res.partner'
    # _description = 'pranali_work.pranali_work'

    date_of_birth = fields.Date(string="Date of Birth")
    street3= fields.Text(string="Street3")
    customer_reference = fields.Char(string="customer Reference")

