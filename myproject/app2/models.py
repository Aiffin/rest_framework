from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class User(models.Model):
	name=models.CharField(max_length=10)
	address=models.CharField(max_length=10)
	dob=models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
	highlighted = models.TextField()
	
def save(self, *args, **kwargs):
    
    lexer = get_lexer_by_name(self.language)
    linenos = self.linenos and 'table' or False
    options = self.title and {'title': self.title} or {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(User, self).save(*args, **kwargs)