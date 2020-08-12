from django.template.defaulttags import register

@register.filter
def get_field(form, field):
    return 'asdasa'