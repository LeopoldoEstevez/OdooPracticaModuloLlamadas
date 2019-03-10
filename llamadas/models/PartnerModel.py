
   # -*- coding: utf-8 -*-
from odoo import models, fields, api

# Campos que queremos que tenga añadidos los partners 

class Partner(models.Model):
    # Hereda los campos de partners y añades un booleano de si es incidente y cuales son 
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not instructors
    incidente= fields.Boolean("Incidente", default=False)

    # Recupera todas las incidencias en las que está presente , a su vez puede estar en multiples incidencias
    incidencia_ids = fields.Many2many('llamadas.incidencia',
        string="incidencias realizadas", readonly=True)