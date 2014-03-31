# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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

from openerp.osv import fields, osv
import logging

_logger = logging.getLogger(__name__)

class pos_order(osv.osv):
    """ POS Order """
    _inherit = "pos.order"
    _name = "pos.order"

    def _check_credit_limit(self, cr, uid, ids, context=None):
        obj = self.browse(cr, uid, ids[0], context=context)
        if obj.state in ['paid']:
		total_check = obj.partner_id.credit_limit - (obj.partner_id.credit + obj.amount_total)
		if total_check < 0:
			raise osv.except_osv('Error','El cliente supera su limite de credito por '+\
				str(total_check*(-1) )+'$')
			return False
        return True

    _constraints = [
        (_check_credit_limit, 'La compra supera el límite de crédito del cliente.', ['state']),
    ]


pos_order()
