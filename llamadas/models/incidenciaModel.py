from odoo import models, fields, api
from datetime import timedelta

# Clase incidencia con todo lo interesante
class Incidencia(models.Model):


    # nombre y descripcion
    _name = 'llamadas.incidencia'
    _description = "Incidencias"

    # Campos que queremos que aparezcan en la web
    titulo = fields.Char(required=True)
    fecha = fields.Date(default=fields.Date.today)
    causa = fields.Text()

    # Relacion many to one , pilla todos los usuarios y los mete en un dropdown
    # Con la relación many2one me permite seleccionar un usuario o crearlo directamente
    encargado = fields.Many2one('res.users', ondelete='set null',string="Encargado", index=True)

    # Permite añadir nuevas llamadas a la incidencia , cada llamada solo puede estar en una incidencia pero una incidencia puede tener muchas llamadas
 # En la relacion one2many
    llamadas_ids = fields.One2many(
        'llamadas.llamada', 'id', string="Llamadas de la incidencia")

    # Recupera todos los contactos que puedes setear como incidente
    # puedo elegir uno(partner/cliente) que ya existe o crear uno nuevo
    incidentes_ids = fields.Many2many('res.partner', string="Incidentes")
