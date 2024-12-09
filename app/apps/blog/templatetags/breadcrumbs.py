from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def breadcrumbs(context):
    request = context['request']
    path = request.path.strip('/').split('/')
    breadcrumbs = []
    url = ""
    for part in path:
        url += f"/{part}"
        # Capitalize each part and add to breadcrumbs
        breadcrumbs.append((part.capitalize(), url))
    return breadcrumbs
