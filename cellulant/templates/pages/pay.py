from frappe import _

def get_context(context):
    context['title'] = _('Card Payment')
    return context
