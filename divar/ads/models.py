from django.db import models
from django.contrib.auth.models import User

class Category (models.Model) :
    title = models.CharField(max_length=20)

    def str(self) -> str:
        return self.title
    

class Ad(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    city = models.CharField(max_length=10)
    caption = models.TextField()
    imidietly = models.BooleanField(default = False)
    image = models.ImageField(upload_to='ads/' , blank=True , null= True)

    def str(self) -> str:
        return self.title
    
    
# Create your models here.
# Create your models here.
