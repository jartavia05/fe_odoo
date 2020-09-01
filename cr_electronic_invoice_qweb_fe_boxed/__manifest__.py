# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo is an Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, version 3 of the
#    License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'Costa Rica Factura Electronica plantilla QWEB by JA',
    'version' : '12.0',
    'author' : '@jartavia05',
    'summary': 'Actualizacion de la plantilla QWEB para cumplir con los requirimientos de la DGT de Costa Rica',
    'description': """
        Una vista mas amigable para la presentacion de documentos de Factura Electronica basada en la vista "external_layout_boxed"
    """,
    'category': 'Accounting & Finance',
    'sequence': 4,
    'website' : 'https://github.com/jartavia05',
    'depends' : ['cr_electronic_invoice', 'sale'],
    'demo' : [],
    'data' : [
        'views/res_company_view.xml',
        'views/report_sales_invoice_qweb.xml',
    ],
    'test' : [
    ],
    'auto_install': False,
    'application': True,
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
# open source prevents backdoor.
