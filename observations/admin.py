from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,

)
from .models import ObsField

# Register your models here.

class ObsFieldAdmin(ModelAdmin):

    model = ObsField
    menu_label = "Observation Field"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("field_no", "field_name",)
    search_fields = ("field_no", "field_name",)

modeladmin_register(ObsFieldAdmin)