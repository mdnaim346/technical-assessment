from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessDenied

class ChangePasswordWizard(models.TransientModel):
    _name='user.change.password'
    _description='User Change Password Wizard'

    old_password = fields.Char(string="Old Password", required=True )
    new_password =fields.Char(string="New Password", required=True )
    confirm_password = fields.Char(string= "Confirm Password",required=True)

    def action_change_password(self):
        self.ensure_one()
        if self.new_password != self.confirm_password:
            raise ValidationError(_("New Password and Confirm Password do not match."))
        try:
            self.env.user._check_credentials(self.old_password, {'interactive': True})
        except AccessDenied:
            raise ValidationError(_("Old Password is incorrect."))
        if self.new_password == self.old_password:
            raise ValidationError(_("New Password cannot be the same as Old Password."))
        user = self.env.user
        user._change_password(self.new_password)

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/session/logout?redirect=/web/login',
            'target': 'self'
        }