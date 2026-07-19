import re

from odoo import models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _post(self, soft=True):
        posted = super()._post(soft=soft)
        posted._auto_reconcile_from_so_reference()
        return posted

    def _auto_reconcile_from_so_reference(self):
        for move in self:
            move._auto_reconcile_move_from_so_reference()
        return True

    def _auto_reconcile_move_from_so_reference(self):
        self.ensure_one()
        if self.move_type != 'entry':
            return

        payable_lines = self.line_ids.filtered(
            lambda l: l.account_id.account_type in ('asset_receivable', 'liability_payable')
            and not l.reconciled
        )
        if not payable_lines:
            return

        first_line = self.line_ids.sorted('sequence')[:1]
        label = first_line.name if first_line else False
        if not label:
            return

        sale_order = self._find_sale_order_from_label(label)
        if not sale_order:
            return

        self._reconcile_with_sale_order_invoices(payable_lines, sale_order)

    def _find_sale_order_from_label(self, label):
        tokens = re.findall(r'\S+', label)
        if not tokens:
            return self.env['sale.order']
        return self.env['sale.order'].search([('name', 'in', tokens)], limit=1)

    def _reconcile_with_sale_order_invoices(self, payable_lines, sale_order):
        invoices = sale_order.invoice_ids.filtered(lambda m: m.state == 'posted')
        if not invoices:
            return

        for account in payable_lines.account_id:
            lines_for_account = payable_lines.filtered(lambda l: l.account_id == account)
            invoice_lines = invoices.line_ids.filtered(
                lambda l: l.account_id == account and not l.reconciled
            )
            if invoice_lines:
                (lines_for_account + invoice_lines).reconcile()