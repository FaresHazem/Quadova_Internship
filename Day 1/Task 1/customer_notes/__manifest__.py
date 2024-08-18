{
    "name": "customer_notes",
    "version": "17.0.0.0.0",
    "license": "OEEL-1",
    "depends": ["base"],
    "application": True,
    "data": [
        # SECURITY
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        # VIEWS
        #"views/customer_records_views.xml",
        "views/customer_notes_views.xml",
        # MENUS
        "views/customer_menu.xml",
    ],
}
