{
    'name': 'User Change Password',
    'version': '1.0',
    'summary': 'User Change Password',
    'description': 'User Change Password',
    'author': 'Naim Reza',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/change_password_views.xml',
    ],
    'assets':{
            'web.assets_backend': [
                'user_change_password/static/src/js/change_password_menu.js',
            ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

}