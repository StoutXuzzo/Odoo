# -*- coding: utf-8 -*-
# from odoo import http


# class Enter(http.Controller):
#     @http.route('/enter/enter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/enter/enter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('enter.listing', {
#             'root': '/enter/enter',
#             'objects': http.request.env['enter.enter'].search([]),
#         })

#     @http.route('/enter/enter/objects/<model("enter.enter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('enter.object', {
#             'object': obj
#         })
