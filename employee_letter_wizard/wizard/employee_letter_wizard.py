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

    @api.onchange('employee_id', 'letter_type')
    def _onchange_generate_content(self):
        for wizard in self:
            if wizard.employee_id and wizard.letter_type:
                wizard.letter_html = wizard._render_letter_body()
                
    def _render_letter_body(self):
        self.ensure_one()
        xmlid = f'employee_letter_wizard.letter_body_{self.letter_type}'
        return self.env['ir.qweb']._render(xmlid, self._get_render_values())
    
    def _get_render_values(self):
        self.ensure_one()
        employee = self.employee_id
        joining_date = False
        if 'contract_id' in employee._fields and employee.contract_id:
            joining_date = employee.contract_id.date_start
        return {
            'employee': employee,
            'company': employee.company_id,
            'joining_date': joining_date,
        }
