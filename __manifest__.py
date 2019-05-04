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
    'website': "www.iestrassierra.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestión de Deportes',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/socios.xml',
        'views/instalaciones.xml',
        'views/reservas.xml',
        'views/deportes.xml',
        'reportes/informes_socios.xml',
    ],
    # # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'application': True,
}