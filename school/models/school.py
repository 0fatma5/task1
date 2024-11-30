from odoo import models, fields

class School(models.Model):
    _name = 'school'


    name = fields.Char( required=True)
    location = fields.Char()
    school_type = fields.Selection(
        selection=[
            ('private', 'Private'),
            ('governmental', 'Governmental'),
            ('international', 'International')
        ],
        string='School Type',
        required=True
    )
    no_of_students = fields.Integer()
    no_of_teachers = fields.Integer()
    campus_size = fields.Integer()
    grades_offered = fields.Selection(
        selection=[
            ('g1', 'Grade 1'),
            ('g2', 'Grade 2'),
            ('g3', 'Grade 3'),
            ('g4', 'Grade 4'),
            ('g5', 'Grade 5'),
            ('g6', 'Grade 6'),
            ('g7', 'Grade 7'),
            ('g8', 'Grade 8'),
            ('g9', 'Grade 9'),
            ('g10', 'Grade 10'),
            ('g11', 'Grade 11'),
            ('g12', 'Grade 12')
        ],
        string='Grades Offered'
    )
