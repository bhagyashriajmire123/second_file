
from django.db import models
from functools import reduce

# Create your models here.

class Activestud(models.Manager):   # custom mdel manager
    def get_queryset(self):
        return super(Activestud, self).get_queryset().filter(is_active1=1)
class InActivestud(models.Manager):
    def get_queryset(self):                                  ## override the get_queryset1 method
        return super().get_queryset().filter(is_active1=0)



class Sons(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Salary = models.FloatField()
    Mark = models.FloatField(null=True)
    is_active1 = models.BooleanField(default=1)


    active_field1 = Activestud()
    Inactive1 = InActivestud()
    objects = models.Manager()
  
    
    class Meta:
        db_table = 'shell'


    def __str__(self):
        return self.Name
    
#     def get_stud_details(self):
#         print(f"""stud_id:-{self.id}
# stud_Name:- {self.Name}
# stud_Age:-{self.Age}
# stud_Salary:-{self.Salary} 
# stud_Marks:- {self.Mark}
#     """)
    # get_stud_details()

    @classmethod
    def get_all_stud_details(cls):
        data = cls.objects.all()
        for i in data:
            print(f"""stud_id:-{i.id}
stud_Name:- {i.Name}
stud_Age:-{i.Age}
stud_Salary:-{i.Salary} 
stud_Marks:- {i.Mark}
    """)
    # get_all_stud_details()


    # @classmethod
    # def get_active_stud(cls):
    #     data = cls.objects.filter(is_active1 =1)
    #     return data

    # @classmethod
    # def get_avg_marks(cls):
    #     data = cls.objects.all()
    #     total= 0
    #     for i in data:
    #         total+=i.Mark
    #     avg = total/len(data)
    #     return avg

    # get_avg_marks()

# lambda
   


    @classmethod
    def get_avg_marks_reduce(cls):
        data = cls.objects.all()
        l = []
        for i in data:
            l.append(i.Mark)
        res = reduce((lambda x, y : x+y),l)
        avg_marks= res/len(data)
        return avg_marks
    # get_avg_marks_reduce()

   