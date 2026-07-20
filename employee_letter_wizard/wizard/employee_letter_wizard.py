from odoo import models, fields, api


class EmployeeLetterWizard(models.TransientModel):
    _name = 'employee.letter.wizard'
    _description = 'Employee Letter Generation Wizard'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    letter_type = fields.Selection([
        ('appointment', 'Appointment Letter'),
        ('joining', 'Joining Letter'),
        ('promotion', 'Promotion Letter'),
        ('resignation', 'Resignation Letter'),
    ], string='Letter Type', required=True)
    letter_html = fields.Html(string='Letter Content', sanitize=True)
