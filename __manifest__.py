# -*- coding: utf-8 -*-
{
    'name': "CDPELOTAS3763Y",

    'summary': """
        Modulo de para tarea Online 4 de Sistemas de Gestión Empresarial
    """,

    'description': """
        Modulo de para tarea Online 4 de Sistemas de Gestión Empresarial
    """,

    'author': "Antonio Olmo López",
    'website': "www.iestrassierra.conm",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestión de Deportes',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/socios.xml',
        'views/deportes.xml',
        # 'views/instalaciones.xml',
    ],
    # # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'application': True,

}