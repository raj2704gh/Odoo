from odoo import api,fields,models

class ProjectTask(models.Model):
    _inherit="project.task"

    patient_name=fields.Many2one("hospital.patient",string="Name")