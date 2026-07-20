# Odoo Technical Assessment

Solutions for the practical Odoo technical assessment (Odoo 17). Three modules.

## Setup

1. Clone into your addons folder.
2. Add to `addons_path` in `odoo.conf`.
3. Restart Odoo, update apps list.
4. Install:
   - `account_so_reconciliation` (Task 1)
   - `user_change_password` (Task 2)
   - `employee_letter_wizard` (Task 3)

---

## Task 1: Automatic Payment Reconciliation (`account_so_reconciliation`)

Hooks `account.move._post()` (covers Journal Entries and Bank Statement Lines, both post through this). Reads the first journal item's label, extracts word tokens, looks up a matching `sale.order` by name (no hardcoded number format). If the label matches more than one SO, it's skipped instead of guessing.

Reconciliation itself uses Odoo's built-in `account.move.line.reconcile()` against the payment line and the SO's outstanding invoice lines — handles partial payments, multiple invoices, and refunds without custom logic.

**Limitations:** label needs the SO number as a clean token (punctuation touching it can break the match); doesn't check that the move's partner matches the SO's customer.

**Test:** confirm SO → invoice → post it. Create a journal entry / statement line with the SO number in the first line's label, post it. Invoice should reconcile (full or partial). Try with 2 invoices on one SO too.

---

## Task 2: Change Password (`user_change_password`)

Adds "Change Password" to the user profile dropdown (same `user_menuitems` registry Odoo uses for Preferences/Log out). Opens a wizard (old/new/confirm password), uses Odoo's own `_check_credentials()` / `_change_password()` — no custom hashing. On success, redirects to `/web/session/logout` so the user has to log back in.

**Limitation:** access is only group-level right now (`base.group_user`), no per-record `ir.rule` yet.

**Test:** click avatar → Change Password. Wrong old password → error. Mismatched new/confirm → error. Correct flow → logged out, log back in with new password.

---

## Task 3: Employee Letter Wizard (`employee_letter_wizard`)

Dynamic wizard to generate formatted employee letters (Appointment, Joining, Promotion, Resignation). Uses QWeb templates with employee data (name, job title, department, company, joining date). Auto-populates letter content when employee and letter type are selected. Renders as HTML in the wizard for editing, then exports to PDF.

**Features:**
- Four letter templates (appointment, joining, promotion, resignation)
- Auto-population from employee contract/HR data
- HTML editor for customization before export
- PDF generation with company letterhead
- Accessible from HR module menu → Employee Tools

**Test:** HR → Employee Tools → Generate Employee Letter. Select employee and letter type. Verify HTML populates with employee details. Click "Generate PDF" to export.
