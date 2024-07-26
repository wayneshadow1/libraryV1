from  library.storage_backends import   PublicMediaStorage,PrivateMediaStorage
from django.db import models
import uuid
from django.conf import settings
User  = settings.AUTH_USER_MODEL


def getStorageClass(status):
     if status =='Private':
           return PrivateMediaStorage()
     else:
           return PublicMediaStorage()
# Create your models here.
class Project(models.Model):
      name = models.CharField(max_length=100)
      description = models.TextField(default="")
      Author = models.CharField(max_length=100)     
      def __str__(self):
          return self.name      
class asset_type(models.Model):
    Name = models.CharField(max_length=100,default=None)
    def __str__(self):
        return self.Name

class asset_grouping(models.Model):
    Group_name = models.CharField(max_length=100,default=None)
    def __str__(self):
        return self.Group_name

class asset(models.Model):
    publicity_status_choices =[("PUBLIC","PUBLIC"),("PRIVATE","PRIVATE"),("FAMILY","FAMILY"),("FRIENDS","FRIENDS")]
    item_type_choices = [
        ("DOCUMENT",(("WORD","WORD"),("PDF","PDF"))),
        ("VIDEO",(("MP4","MP4"),("H265","H265"))),
        ("OTHER","OTHER"),("NOT SPECIFIED","NOT SPECIFIED")]
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name =  models.CharField(max_length=100)
    file = models.FileField(upload_to="%Y/%M"+f"/{uuid.uuid4()}")
    publicity_status = models.CharField(max_length=100,choices=publicity_status_choices,default="PUBLIC")
    description = models.TextField(default="No descrition")
    author = models.CharField(max_length=100,default="author")
    asset_item_type = models.ForeignKey(asset_type,on_delete=models.CASCADE)
    asset_item_group = models.ForeignKey(asset_grouping,on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    project = models.ForeignKey(Project,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
    def save(self,*args,**kwargs):
         self.file.storage=getStorageClass(self.publicity_status)
         super().save(*args, **kwargs)
