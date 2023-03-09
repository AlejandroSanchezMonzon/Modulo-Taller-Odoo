# -*- coding: utf-8 -*-
{
    'name': "Taller SGE",

    'summary': 'Módulo creado para la asignatura de Sistemas de Gestión Empresarial, dentro del CFGS de Desarrollo de Aplicaciones Multiplataforma.',

    'description': 'En este módulo vamos a ayudar a la gestión de un taller por el cual pasan una caontidad diaria de vehículos.',

    'author': 'Alejandro Sánchez Monzón',
    'website': 'https://www.linkedin.com/in/alejandrosm/',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productividad',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/taller_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
        'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
