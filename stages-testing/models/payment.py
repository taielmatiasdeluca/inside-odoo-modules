from odoo import api, fields, models

class Payment(models.Model):
    _name = "stages.payment"
    _description = "Modelo que simula unp pago"
    
    titulo = fields.Char(name="titulo", req=True)
    descripcion = fields.Text()
    precio = fields.Float()
    stages = fields.Selection([('waiting', 'En espera'), ('working', "Trabajando"), ("staging", "Esperando aprobacion"),('approved', "Aprobado")])
    
