# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class booking_order__fiqih_saputra(models.Model):
#     _name = 'booking_order__fiqih_saputra.booking_order__fiqih_saputra'
#     _description = 'booking_order__fiqih_saputra.booking_order__fiqih_saputra'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
