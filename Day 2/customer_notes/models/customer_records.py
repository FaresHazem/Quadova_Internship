from odoo import fields, models, api
from odoo.exceptions import ValidationError

class CustomerRecords(models.Model):
    _name = "customer.records"
    _description = "customer_records"

    name = fields.Char(
        string="Name",
        required=True,
        default=lambda self: self.env.user.customer_id.name,
        readonly=True
    )

    notes = fields.One2many("customer.notes", "customer_id", string="Notes")

    @api.constrains('name')
    def _check_customer_name(self):
        for record in self:
            if not record.name:
                raise ValidationError("The customer name cannot be null or empty.")
