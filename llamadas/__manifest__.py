# -*- coding: utf-8 -*-
{
    'name': "llamadas",

    'summary': """
        Control de llamadas telefonicas""",

    'description': """
    Este modulo permite la gestion de las llamadas realizadas a clientes
    """,

    'author': "Leopoldo Estevez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'llamadas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # Añadimos las diferentes vistas que queremos
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/llamada.xml',
        'views/incidencia.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}