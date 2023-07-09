from odoo import api , models, fields, _

class SchoolClass(models.Model):
    _name="school.class"
    _description="School Class"
    
    name=fields.Char(required=True)
    
    year_id=fields.Many2one(comodel_name="school.year", string="Year",)
    
    