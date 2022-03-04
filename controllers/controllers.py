# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrderFiqihSaputra(http.Controller):
#     @http.route('/booking_order__fiqih_saputra/booking_order__fiqih_saputra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order__fiqih_saputra/booking_order__fiqih_saputra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order__fiqih_saputra.listing', {
#             'root': '/booking_order__fiqih_saputra/booking_order__fiqih_saputra',
#             'objects': http.request.env['booking_order__fiqih_saputra.booking_order__fiqih_saputra'].search([]),
#         })

#     @http.route('/booking_order__fiqih_saputra/booking_order__fiqih_saputra/objects/<model("booking_order__fiqih_saputra.booking_order__fiqih_saputra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order__fiqih_saputra.object', {
#             'object': obj
#         })
