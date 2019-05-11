from django.views import View
from django.http import HttpResponse
from django.shortcuts import render,reverse,redirect
from .forms import RegisterFrom,LoginForm
from .models import UserModel

def home(request):
    name=request.session.get('username','请先登录')
    return render(request,'shuju/home1.html',
                  context={'name':name})
def home1(request):
    name=request.session.get('username','请先登录')
    return render(request,'shuju/home2.html',
                  context={'name':name})
def home2(request):
    name=request.session.get('username','请先登录')
    return render(request,'shuju/home3.html',
                  context={'name':name})
class LoginView1(View):
    def get(self,request):
        return render(request,'shuju/login.html')
    def post(self,request):
        username=request.POST.get('username')
        request.session['username']=username
        return redirect(reverse('home'))

def logout(request):
    request.session.flush()
    return redirect(reverse('home'))

class RegisterView(View):
    def get(self,request):
        form=RegisterFrom()
        return render(request,'shuju/register.html',
                      context={'form':form,
                      })
    def post(self,request):
        form =RegisterFrom(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            email = form.cleaned_data.get('email')
            if password==password_repeat:
                user=UserModel.objects.create(username=username,
                                              password=password,
                                              email=email)
                return HttpResponse('注册成功')
            else:
                return HttpResponse('注册失败')
        else:
            return HttpResponse('注册失败')

class LoginView2(View):
    def get(self,request):
        form=LoginForm()
        return  render(request,'shuju/login_new.html',
                       context={
                           'form':form,
                       })
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=UserModel.objects.filter(username=username,
                                          password=password)
            if user:
                request.session['username'] = username
                return redirect(reverse('home1'))
            else:
                return redirect(reverse('register'))



