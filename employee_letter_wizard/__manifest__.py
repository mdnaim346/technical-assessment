{
    'name': 'Employee Letter Wizard',
    'version': '1.0',
    'summary': 'Dynamic Employee Letter Generation Wizard',
    'description': 'Dynamic Employee Letter Generation Wizard',
    'author': 'Naim Reza',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/employee_letter_wizard_views.xml',
        'report/letter_templates.xml',
        'report/employee_letter_report.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
