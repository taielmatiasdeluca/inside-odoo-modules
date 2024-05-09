from odoo import api, fields, models

class Task(models.Model):
    _name = "taskmanager.task"
    _description = "Simple modelo de prubea para generar una tarea por hacer"

    titulo = fields.Char(name="titulo", required=True)
    descripcion = fields.Text()
    estado = fields.Boolean(default=False)


