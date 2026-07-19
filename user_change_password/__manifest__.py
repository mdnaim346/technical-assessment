{
    'name': 'User Change Password',
    'version': '1.0',
    'summary': 'User Change Password',
    'description': 'User Change Password',
    'author': 'Naim Reza',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/user_change_password.xml',
        'views/res_users_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

}