from django.contrib import admin
from .models import  Employee,Attendance,Timespend
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountInline(admin.StackedInline):
    model=Employee
    can_delete=False
    verbose_name_plural='Newusers'

class CustomizedUserAdmin(UserAdmin):
    inlines=(AccountInline,)
admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)


class register1Admin(admin.ModelAdmin):
    list_display = ('id','fullname','fathername','mothername' ,'phonenumber',
    'emergencynumber','bloodgroup','address','position','user_id','code','image')
admin.site.register(Employee, register1Admin)

class AttendanceInline(admin.StackedInline):
    model=Timespend
    can_delete=False
    verbose_name_plural='Newusers'



class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee','date')
    inlines = [
        AttendanceInline,
    ]
admin.site.register(Attendance, AttendanceAdmin)

class timespendAdmin(admin.ModelAdmin):
    list_display = ('attendance','punchin','punchout')
  
admin.site.register(Timespend, timespendAdmin)
