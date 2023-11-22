from django.shortcuts import render,redirect
from newapp.models import  user_details
from newapp.models import Book_details

# Create your views here.

def userlogin(request):
    if request.method=='POST':
        a=request.POST.get("User_id")
        b=request.POST.get("userpws")
        try:
            obj=user_details.objects.get(User_Name=a,Password=b)

            return redirect('bookdetails')

        except:
            pass
    return render(request ,'user_login.html')

def login(request):
    if request.method=='POST':
        a=request.POST.get('Fname')
        b=request.POST.get('Lname')
        c=request.POST.get('User_Name')
        d=request.POST.get('Password')
        g=request.POST.get('number')
        obj=user_details.objects.create(Fname=a,Lname=b,User_Name=c,Password=d)
        return redirect('user_login')
    return render(request,'Newuser.html')

def addbook(request):
    if request.method == 'POST':
        library=Book_details.objects.create(Book_Name=request.POST.get('Name'),Code=request.POST.get('Code'),
                                        Author_Name=request.POST.get('Author'),Status=request.POST.get('Status'),
                                        Amount=request.POST.get('Amount'),Created_date=request.POST.get('Created'),
                                        Updated_date=request.POST.get('Updated'))
    return render(request,'addbook.html')


def bookdetails(request):
    data=Book_details.objects.all()
    return render(request,'bookdetails.html',{'data':data})
def updatebook(request,pk):
    obj=Book_details.objects.get(id=pk)
    if request.method=='POST':
        library =Book_details.objects.filter(id=pk).update(Book_Name=request.POST.get('Name'),
                                        Code=request.POST.get('Code'),
                                        Author_Name=request.POST.get('Author'),
                                        Amount=request.POST.get('Amount'),
                                        Updated_date=request.POST.get('Updated'))
        return redirect('bookdetails')
    return render(request,'update.html',{'obj':obj})

def deletebook(request,pk):
    obj=Book_details.objects.filter(id=pk).delete()
    return redirect('bookdetails')






