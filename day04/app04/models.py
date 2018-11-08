from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(
        max_length=20
    )
    desc = models.CharField(
        max_length=30
    )

    def get_desc(self):
        return "爱你的理由：%s"% self.desc
