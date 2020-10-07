from django.db import models

# Create your models here.
class IndexModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '%s:%s - %s' % (self.id, self.email, self.action)
    