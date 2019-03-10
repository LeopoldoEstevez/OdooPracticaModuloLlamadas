# -*- coding: utf-8 -*-
from odoo import http

# class Llamadas(http.Controller):
#     @http.route('/llamadas/llamadas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/llamadas/llamadas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('llamadas.listing', {
#             'root': '/llamadas/llamadas',
#             'objects': http.request.env['llamadas.llamadas'].search([]),
#         })

#     @http.route('/llamadas/llamadas/objects/<model("llamadas.llamadas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('llamadas.object', {
#             'object': obj
#         })