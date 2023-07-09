from odoo import api, models, fields, _
from odoo.exceptions import ValidationError
from datetime import date


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student"
    _rec_name = "student_name"

    _sql_constraints = [
        (
            'uniq_student_id',
            'unique(student_id)',
            'This ID is exist make sure and try again!'
        ),
    ]

    
    student_name = fields.Char(required=True, string="Student name")
    student_img=fields.Binary()
    student_id = fields.Char(required=True, string="Student ID")
    birth_date = fields.Date(
        string="Birth Date", default=date(date.today().year-7, 1, 1))
    age = fields.Integer(compute="_compute_age")
    gender=fields.Selection(selection=[('male','Male'),('female','Female')],default='male')
    class_id = fields.Many2one(comodel_name="school.class", string="Class",)

    subjects_ids = fields.One2many(
        comodel_name="school.subject", inverse_name="student_id", string="Subjects")

    year = fields.Integer(related='class_id.year_id.year')

    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for record in self:
            record.age = today.year-record.birth_date.year - \
                ((today.month, today.day) <
                 (record.birth_date.month, record.birth_date.day))
    
    
    @api.constrains('birth_date')
    def _check_birth_date(self):
        for record in self:
            if record.age < 6:
                raise ValidationError(_('Age should be 6 years orld or more!'))
    