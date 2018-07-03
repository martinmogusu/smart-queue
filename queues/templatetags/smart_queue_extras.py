from django import template
from django.contrib.auth.models import Group

register = template.Library()

# Get list item at specified index
@register.filter(name='get_at_index')
def get_at_index(list, index):
	return list[index]

# Check if user belongs to a group
@register.filter(name='has_group')
def has_group(user, group_name):
	group = Group.objects.get(name=group_name)
	return group in user.groups.all()

# Strips underscores from word and replaces with spaces
@register.filter(name='strip_underscores')
def strip_underscores(value):
	return value.replace('_', ' ')

# Get if string starts with another string
@register.filter('startswith')
def startswith(text, starts):
	if isinstance(text, str):
		return text.startswith(starts)
	return False