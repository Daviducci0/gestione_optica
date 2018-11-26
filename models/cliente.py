from odoo import models, fields, api


class Clienti(models.Model):
    _inherit = 'res.partner'
    _description ='Permette la gestione clienti nel modulo Gestione Ottica'

    cod_fisc = fields.Char()
    birth = fields.Char()
    sf_dx_l = fields.Char(string="Sfera")
    sf_dx_v = fields.Char(string="Sfera")
    sf_sx_l = fields.Char(string="Sfera")
    sf_sx_v = fields.Char(string="Sfera")
    cil_dx_l = fields.Char(string="Cilindro")
    cil_dx_v = fields.Char(string="Cilindro")
    cil_sx_l = fields.Char(string="Cilindro")
    cil_sx_v = fields.Char(string="Cilindro")
    ax_dx_l = fields.Char(string="Asse")
    ax_dx_v = fields.Char(string="Asse")
    ax_sx_l = fields.Char(string="Asse")
    ax_sx_v = fields.Char(string="Asse")
    lente_l = fields.Text(string="Tipo Lente")
    lente_v = fields.Text(string="Tipo Lente")
    mont_l = fields.Text(string="Tipo Montatura")
    mont_v = fields.Text(string="Tipo Montatura")
    diam_l = fields.Char(string="Diametro")
    diam_v = fields.Char(string="Diametro")
    data_pre = fields.Char(string="Data Prescrizione")
    dav = fields.Char(string="DAV")
    sf_dx = fields.Char(string="Sfera")
    sf_sx = fields.Char(string="Sfera")
    cil_dx = fields.Char(string="Cilindro")
    cil_sx = fields.Char(string="Cilindro")
    ax_dx = fields.Char(string="Asse")
    ax_sx = fields.Char(string="Asse")
    metrica = fields.Selection(
        [('tabo', 'TABO'),
         ('inter', 'Sistema Internazionale')],
        'Metrica')
    currency_id = fields.Many2one(
        'res.currency', string='Valuta')
    retail_price = fields.Monetary(
        'Acconto',
        currency_field='currency_id',
    )

    oculista = fields.Many2one(
        'ottica.medico', string='Medico',
        ondelete='set null',
        context={}
    )

    class Medico(models.Model):
        _name = 'ottica.medico'

        name = fields.Char(string="Nome", required="True")
        street = fields.Char()
        city = fields.Char()
        zip = fields.Char()
        name_hospital = fields.Char()
        street_s = fields.Char()
        city_s = fields.Char()
        zip_s = fields.Char()
        paziente = fields.One2many(
            'res.partner', 'oculista',
            string="Pazienti",
            ondelete='set null',
        )

