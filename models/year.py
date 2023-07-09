# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolYear(models.Model):
    _name = "school.year"
    _description = "School Year"
    _rec_name="year"  
    _sql_constraints = [
        (
            'constraint_uniq_year',
            'unique(year)',
            'This year found, please check again!!'
        ),
    ]
    
    year = fields.Integer(required=True)
    
    num_of_classes= fields.Integer(required=True)
    
    