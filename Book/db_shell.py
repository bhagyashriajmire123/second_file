# exec(open(r"E:\My_Revesion\django\Starbus\Book\db_shell.py","r").read())

from Book.models import Sons

# data = Sons.objects.all()
# obj = Sons(Name="Bhagyashri", Age= 26, Salary=50000, Mark=89 )
# obj.save()
# obj1 = Sons(Name="shri", Age= 29, Salary=5000, Mark=80 )
# obj1.save()
# boj = Sons.objects.create(Name="Akash", Age= 23, Salary=45000, Mark=80)   # no need fr save
obj= Sons()
obj.get_all_stud_details()
# obj.get_stud_details()
# print(Sons.get_avg_marks())
# print(Sons.get_avg_marks_lambda())
# obj.get_avg_marks_reduce()
# print(Sons.get_active_stud())
# print(Sons.get_active_stud())
# print(Sons.active_field.all())
# print(Sons.Inactive1.all())
# print(Sons.object.all())
# print(Sons.get_avg_marks_
# reduce())
# print(type(data))
# obj = Sons()
# Sons.get_all_stud_details()
# data = Sons.objects.filter(id__gte=7)
# # print(data)

# try:
#     obj = Sons()
#     obj.get_all_stud_details()
#     print("-----------")
#     print(type(obj))
#     data = Sons.objects.get(id =5)
#     print(type(data))
#     print("-----------")
#     data.get_stud_details()
#     # data.Name = "Abhijit"
#     # data.save()
#     print(data)
# except Sons.DoesNotExist:
#     print("No data found")


# def get_increment_marks():
#     data = Sons.objects.all()
#     for std in data:
#         std.Mark += (std.Mark * (5/100))
#         std.save()

# get_increment_marks()

# def get_salary_increment():
#     data = Sons.objects.all()
#     for i in data:
#         i.Salary += (i.Salary * (8/100))
#         i.save()

# get_salary_increment()



