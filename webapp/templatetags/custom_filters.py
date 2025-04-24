from django import template
from datetime import datetime

register = template.Library()

@register.filter
def format_gitlab_date(iso_str):
    try:
        dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return iso_str  

