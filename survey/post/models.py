from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

 
income_list=[('$0 - $24,999','$0 - $24,999'),
('$25,000 - $49,999','$25,000 - $49,999'),
("$50,000 - $74,999","$50,000 - $74,999"),
("$75,000 - $99,999","$75,000 - $99,999"),
("$100,000 - $149,999","$100,000 - $149,999"),
("$150,000 or more","$150,000 or more")]

    

User=get_user_model()
class Post(models.Model):
    user=models.OneToOneField(User,related_name='post_detail',on_delete=models.CASCADE)
    gender= models.CharField(max_length=100,choices=[('male','Male'),('female','Female'),('na',"N/A")])
    age=models.CharField(max_length=100,choices=[("0 - 17","0 - 17"),("18 - 24","18 - 24"),("25 - 34","25 - 34"),("35 - 44","35 - 44"),("45 - 54","45 - 54"),("55 - 64","55 - 64"),("65 or more","65 or more")])
    income=models.CharField(max_length=100, choices=income_list)

    education=models.CharField(max_length=100,choices=[("Less than HS diploma","Less than HS diploma"),("High school","High school"),("Some college","Some college"),("Bachelors degree","Bachelors degree"),("Graduate degree","Graduate degree")])



    def __str__(self):
        return self.user.AboutUser.first_name


    def get_success_url(self):
        return reverse('post:post_detail',kwargs={'pk':self.pk})

    
    





