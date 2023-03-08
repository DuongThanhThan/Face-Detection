import json
from djongo import models


# Create your models here.
class Face_Detection(models.Model):
    _id = models.ObjectIdField()
    user_id  = models.IntegerField()
    full_name = models.CharField(max_length = 150)
    email = models.CharField(null = True, blank = True, max_length = 150)
    image = models.CharField(null = True, blank = True, max_length = 150)
    created_time = models.CharField(null = True, blank = True, max_length = 150)
    
    class Meta:
        db_table = "Face_Detection"
    
    def __str__(self):
        db = {
            "id" : str(self._id),
            "user_id" : str(self.user_id),
            "full_name" : str(self.full_name),
            "email" : str(self.email),
            "image" : str(self.image),
            "created_time" : str(self.created_time),
        }
        return json.dumps(db,indent = 6)
    
    
class Time(models.Model):
    _id = models.ObjectIdField()
    user_id  = models.CharField(null = False, blank = False, max_length = 50)
    time = models.TextField(null = True, blank = True)

    class Meta:
        db_table = "Time"




