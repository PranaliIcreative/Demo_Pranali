# -*- coding: utf-8 -*-
import string

from odoo import models, fields, api
from datetime import datetime
from odoo.tools.populate import compute


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # _description = 'pranali_work.pranali_work'

    customer_id= fields.Char(string="customer Id")
    customer_ref =fields.Char(string="customer Reference")


