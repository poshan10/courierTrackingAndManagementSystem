from django.db import models

# Create your models here.



class Branch(models.Model):
    branch_name = models.CharField(max_length=30, blank=False, unique=True)
    branch_address = models.CharField(max_length=50, blank=False)
    branch_phone_no = models.IntegerField(max_length=15, blank=False)
    branch_des = models.TextField()
    branch_pic = models.ImageField(upload_to='/img', blank=True)
    branch_created_at = models.DateTimeField(auto_now_add=True)
    branch_updated_at = models.DateTimeField(auto_now=True)





class courier_details(models.Model):
    courier_name = models.CharField(max_length=100)
    sending_branch = models.OneToOneField(Branch)
    receiving_branch = models.OneToOneField(Branch)
    delivery_address = models.CharField(max_length=100)



