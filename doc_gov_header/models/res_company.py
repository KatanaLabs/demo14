from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    l10n_do_gov_text_header_document = fields.Text("Document Text Header", default="REPÚBLICA DOMINICANA")
