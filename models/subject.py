from odoo import fields, models, api, _


class SchoolSubject(models.Model):
    _name = "school.subject"
    _description = "School Subject"
    _rec_name = "subject"

    _sql_constraints = [
        (
            "constraint_unique_subject", "unique(subject)", "This subject is found!!"
        )
    ]
    subject = fields.Char(required=True)

    year_id = fields.Many2one(comodel_name="school.year", string="Year",)

    student_id = fields.Many2one(comodel_name='school.student')