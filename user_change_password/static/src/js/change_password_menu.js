/** @odoo-module **/

import { registry } from "@web/core/registry";
import { _t } from "@web/core/l10n/translation";

function changePasswordItem(env) {
    return {
        type: "item",
        id: "change_password",
        description: _t("Change Password"),
        callback: () => {
            env.services.action.doAction({
                type: "ir.actions.act_window",
                res_model: "user.change.password",
                views: [[false, "form"]],
                target: "new",
                name: _t("Change Password"),
            });
        },
        sequence: 45,
    };
}

registry.category("user_menuitems").add("change_password", changePasswordItem, { sequence: 45 });