# Odoo Technical Assessment

This repository contains the solutions for the practical Odoo technical assessment,
covering three custom modules built on Odoo 17.

## Setup Instructions

1. Clone this repository into your Odoo custom addons directory:
   ```bash
   git clone <repo-url> technical-assessment
2. Add the folder to your addons_path in odoo.conf:

   addons_path = addons,...,its_addons/technical-assessment,...

3. Restart the Odoo server and update the apps list (Developer mode → Apps → Update Apps List).
4. Install the relevant module(s) from the Apps menu.

 ==> Task 2: Change Password (user_change_password)

## Approach
   * Adds a "Change Password" entry to the top-right user profile dropdown using Odoo's native user_menuitems JS registry (the same mechanism Odoo core uses for "Preferences" / "Log out"), so it integrates cleanly with the existing menu instead of patching templates.
   * Clicking the option opens a change.password.wizard (TransientModel) as a modal, with Current Password / New Password / Confirm New Password fields.
   * On submit, the wizard calls Odoo's own res.users.change_password(), which validates the current password and hashes the new one — no custom hashing or credential-checking logic was written.
   * Changing the password invalidates the current session token; the wizard immediately redirects to /web/session/logout, forcing the user to log in again with the new password.
   * An ir.rule restricts each wizard record to its own creator, so no user can read another user's in-flight password input via the ORM.


## How to Test

1. Install the User Change Password module.
2. Click the user avatar (top-right) → Change Password.
3. Try a wrong current password → should show an access error.
4. Try mismatched new/confirm passwords → should show a validation error.
5. Enter correct current password + matching new/confirm → on submit, you should be logged out immediately and redirected to the login page. Log back in with the new password to confirm the change persisted.

==> Task 1: Automatic Payment Reconciliation (account_so_reconciliation)
(to be documented once implemented)

==> Task 3: Dynamic Employee Letter Generation Wizard (employee_letter_wizard)
(to be documented once implemented)