import random
import string
from django.db import models


def create_code(size=6):
    chars = string.ascii_lowercase + string.digits
    code = ''
    for _ in range(size):
        code += random.choice(chars)
    return code


class URLModel(models.Model):
    url = models.URLField()
    shortcode = models.CharField(max_length=10, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_code()
        super(URLModel, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
