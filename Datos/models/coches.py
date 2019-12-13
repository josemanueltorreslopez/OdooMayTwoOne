from odoo import models, fields, api

class Coches(models.Model):
    _name = 'coches'
    codigo = fields.Integer('Codigo', required=True)
    modelo = fields.Char('Modelo', required=True)
    marca = fields.Char('Marca', required=True)
    matricula = fields.Char('Matricula', required=True)
    promociones = fields.Many2one('promociones', 'Promociones')

