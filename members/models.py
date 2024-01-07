from django.db import models

class Member(models.Model):
  name      = models.CharField( max_length=22  , null= False ) 
  email     = models.CharField( max_length=101 , null= False )
  password  = models.CharField( max_length=22  , null= False )
  
  def __str__(self):
    return f"{self.name}"


class Book(models.Model):
  name     = models.CharField(max_length=255) 
  writer   = models.CharField(max_length=255)
  link_photo = models.CharField(max_length=255)
  category = models.CharField(max_length=255,null= True)
  date     = models.CharField(max_length=255,null= True)
  brief    = models.TextField(null= True)
  number_of_pages = models.PositiveSmallIntegerField(null= True)
  link_download = models.CharField(max_length=255,null= True)

  def __str__(self):
    return f"{self.name} - {self.writer}"


class reading(models.Model):
  user = models.ForeignKey(Member, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.user} - {self.book}"


