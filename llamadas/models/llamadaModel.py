from odoo import models, fields, api

# Clase simple de llamadas realizadas
class llamada(models.Model):
    _name = "llamadas.llamada"
    _description = "llamadas"
    
    # Los fields son aquellos que podran ser llamados y mostrados en la web, el resto solo son valores
    llamada_id = fields.Char(String="id")
    motivo = fields.Char(String="Motivo",required=True)
    notas = fields.Text()