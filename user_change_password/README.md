
# User Change Password

A small Odoo module that adds a "Change Password" item to the user profile dropdown and a simple wizard to change the current user's password.

# Features
 - Adds a `Change Password` item to the profile menu (top-right).
 - Opens a modal wizard to enter current password, new password and confirmation.
 - Validates current password with Odoo internals and updates password securely.

# Installation
1. Ensure the module folder is on `addons_path` (the module path here is `custom_betopia/technical-assessment`).
2. Restart Odoo and update/install the module:

```bash
cd /d F:\odoo17 python odoo-bin -u user_change_password -d <your_database>
