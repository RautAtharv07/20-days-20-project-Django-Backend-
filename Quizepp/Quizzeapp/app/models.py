from django.db import models
import uuid 

class Quize(models.Model):
    tittle=models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True,editable=False)
    
    def __str__(self):
        return self.tittle
    
class question(models.Model):
    
    quize=models.ForeignKey(Quize,on_delete=models.CASCADE,related_name="questions")
    text=models.TextField()
    question1=models.CharField(max_length=100,null=False)
    question2=models.CharField(max_length=100)
    question3=models.CharField(max_length=100)
    question4=models.CharField(max_length=100)
    context = {
        'question1':question1,
        'question2':question2,
        'question3':question3,
        'question4':question4,
    }
    correct = models.CharField(max_length= 50,choices=context,default ='NULL')
    
    
    def __str__(self):
        return self.text

    