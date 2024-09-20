from django.db import models


class URL(models.Model):
    key = models.CharField(max_length=155, default='xxxxx')
    url = models.CharField(max_length=1000)
    short_url = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url
