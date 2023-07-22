# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary': """
        Manage students data and main information about school""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Abdel-fatah Mohamad",
    'website': "abdelfatah.mohamad.99@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education/School',
    'version': '15.0.0.0',
    'license':'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/subject.xml',
        'views/student.xml',
        'views/class.xml',
        'views/year.xml',
        'views/menus.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    
    'application': True,
    'installable': True,
    'autoinstall':False,
}
