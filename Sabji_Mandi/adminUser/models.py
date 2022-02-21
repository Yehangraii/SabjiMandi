from django.db import models

# Create your models here.


class AdminDb(models.Model):
    user_id = models.AutoField(
        auto_created=True, primary_key=True, unique=True)
    username = models.CharField(max_length=100, blank=True)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.CharField(
        max_length=100, default="root@gmail.com")
    password = models.CharField(max_length=8, default="root")
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = "admin_db"
