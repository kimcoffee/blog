from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def summary(self):
        return self.body[:100] #Blog라는 클래스에 정의된 body에서 100글자만 출력하라


    