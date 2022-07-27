from django.db import models

# Create your models here.
class brand(models.Model):
    name = models.CharField(max_length=50)
    #
    def __str__(self):
        return self.name
# class model(models.Model):
#     id_brand = models.ForeignKey('brand', on_delete=models.CASCADE, null=False)
#     name = models.CharField(max_length=255)
#     #
#     def __str__(self):
#         return self.name