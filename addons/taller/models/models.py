from datetime import datetime
from odoo import models, fields, api

class taller_vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Información del vehículo.'

    nombre = fields.Char(string='Matrícula', required=True)
    marca_id = fields.Many2one('taller.marca', string='Marca', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    tipo = fields.Selection([('coche', 'Coche'), ('caravana', 'Caravana'), ('camion', 'Camión'), ('moto', 'Moto'), ('motocicleta', 'Motocicleta')], string='Tipo', required=True)
    matriculacion = fields.Integer(string='Año de matriculación', required=True)
    valor_nuevo = fields.Float(string='Valor nuevo', required=True)
    valor_actual_estimado = fields.Float(string='Valor actual estimado', compute='calcular_estimado')

    @api.depends('matriculacion')
    def calcular_estimado(self):
        for record in self:
            record.valor_actual_estimado = record.valor_nuevo / (datetime.now().year - record.matriculacion)


class taller_marca(models.Model):
    _name = 'taller.marca'
    _description = 'Marca del vehículo.'

    nombre = fields.Char(string='Marca', required=True)
    vehiculos = fields.One2many('taller.vehiculo', 'marca_id', string='Vehículo')
