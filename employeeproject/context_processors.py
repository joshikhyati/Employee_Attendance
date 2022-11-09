
from employeeproject.models import Employee



def Profile(request):
    if request.user.is_authenticated:
       
        check=Employee.objects.filter(user_id=request.user)
        if len(check)>0:
          proobj=Employee.objects.get(user_id=request.user)
          pic=proobj.image
          return{"pic":pic}
    return{}