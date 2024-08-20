from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CustomerNotes(models.Model):
    _name = "customer.notes"
    _description = "Customer Notes"

    # Field Definitions
    title = fields.Char(string="Title", required=True)
    note = fields.Text(string="Note", required=True)
    customer_id = fields.Many2one(
        "customer.records",
        string="Customer",
        default=lambda self: self.env.user.customer_id.id,
        required=True,
        readonly=True
    )
    
    # Constraint to Validate the Fields
    @api.constrains('title', 'note')
    def _check_note_content(self):
        for record in self:
            if not record.title:
                raise ValidationError("The note title cannot be null or empty.")
            if not record.note:
                raise ValidationError("The note content cannot be null or empty.")
