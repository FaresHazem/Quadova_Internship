from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CustomerNotes(models.Model):
    _name = "customer.notes"  # Defines the model name for the customer notes
    _description = "customer_notes"  # Provides a description for the model

    # Field Definitions
    title = fields.Char(string="Title", required=True)  # Defines a Char field for the note title and makes it mandatory
    note = fields.Text(string="Note", required=True)  # Defines a Text field for the note content and makes it mandatory
    customer_id = fields.Many2one("customer.records", string="Customer") # Defines a Many2one field for a relationship with the customer.records model, linking notes to customers

    # Constraint to Validate the Fields
    @api.constrains('title', 'note')  # Ensures validation is applied whenever 'title' or 'note' fields are modified
    def _check_note_content(self):
        for record in self:
            if not record.title:
                # Validation error if 'title' is empty or null
                raise ValidationError("The note title cannot be null or empty.")
            if not record.note:
                # Validation error if 'note' is empty or null
                raise ValidationError("The note content cannot be null or empty.")
