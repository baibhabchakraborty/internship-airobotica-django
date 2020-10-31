from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.IntegerField()
    description=models.TextField()
    


    def __str__(self):
         return self.email +" "+"by"+" "+ self.name

         
class BlogPosts(models.Model):
    username=models.CharField(max_length=100)
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.CharField(max_length=100)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)



    def __str(self):
      
       return self.username
