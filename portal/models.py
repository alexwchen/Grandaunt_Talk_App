from django.db import models

################
# Patient Read Article
################
class main_page(models.Model):
    title = models.CharField(max_length = 200)
    encode = models.CharField(max_length = 200)
    div_id = models.IntegerField(max_length = 200)
    def __unicode__(self):
        return self.title


