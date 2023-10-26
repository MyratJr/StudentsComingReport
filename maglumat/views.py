from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from django.contrib.auth import authenticate,logout,login
from dbr import*
from .forms import*
from django.db.models import Q
from django.contrib.auth.models import User

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def index_ishgarler(request):
    if not request.user.id == 3: return render(request, 'ishgarler.html',{'isgarler':'isgarler'})
    else: return HttpResponse(status=204)

def ishgarler_list(request): return render(request, 'table_ishgarler.html',{'ishgarler': Talyplar.objects.select_related('topar')})

def wezipeler(request):
    if request.user.id==3: return HttpResponse(status=204)
    return render(request,'wezipeler.html',{'wezipelers':Toparlar.objects.all()})

def wezipe_table(request): return render(request,'wezipe_table.html',{'wezipeler':Toparlar.objects.all()})

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def wagtynda_gelenler(request,date):
    if date==str(9): date=str(Talyp_Gunler.objects.all().first())
    elif request.method=='POST': date = request.POST['day']
    return render(request,'wagtynda.html',{'aaaaa':date,'day_category':Talyp_Gunler.objects.all(),'w1':'w1'})

def wagtynda_gelenler_table(request,date):
    asd=[];r=Talyplar.objects.filter(~Q(balnoy_wagt__overlap=[date]) & Q(gelen_wagty__has_key=date))
    for j in r:
        if j.gelen_wagty[date]<=j.is_bashlayar: asd.append(j)
    context={'wagtynda_gelenler':asd,'date':date}
    return render(request,'wagtynda_table.html',context)

def gija_galanlar(request,date):
    if date==str(9): date=str(Talyplar.objects.all().first())
    elif request.method=='POST': date = request.POST['day']
    return render(request,'gija_galanlar.html',{'aaaaa':date,'day_category':Talyplar.objects.all(),'g1':'g1',})

def gija_galanlar_table(request,date):
    asd=[]; r=Talyplar.objects.filter(~Q(balnoy_wagt__overlap=[date]) & Q(gelen_wagty__has_key=date))
    for j in r:
        if j.gelen_wagty[date]>j.is_bashlayar: asd.append(j)
    context={'gija_galanlar':asd,'date':date}
    return render(request,'gija_galanlar_table.html',context)

def gelmedikler(request,date):
    if date==str(9): date=str(Talyplar.objects.all().first())
    elif request.method=='POST': date = request.POST['day']
    return render(request,'gelmedikler.html',{'aaaaa':date,'day_category':Talyplar.objects.all(),'g2':'g2',})
    
def gelmedikler_table(request,date): r=Talyplar.objects.filter(~Q(gelen_wagty__has_key=date) & ~Q(balnoy_wagt__overlap=[date]));context={'gelmedikler':r};return render(request,'gelmedikler_table.html',context)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def barkod(request, pk, which):
    if which==1: return render(request,'all_modal.html',{'a12':Talyplar.objects.get(id=pk)})

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def hello(request): return render(request,'000.html')

def loginuser(request):
    if request.method=='POST':
        username = request.POST['username']; password = request.POST['password']; user = authenticate(username=username, password=password)
        if user is not None: login(request, user); return redirect('ishgarler')
        else: return redirect('loginuser')
    else: return render(request,'login.html')

def loguser_out(request): logout(request); return redirect('loginuser')

def change_login(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            context={}; user = authenticate(username=request.user, password=request.POST['1'])
            if user is not None:
                if request.POST['2']==request.POST['3']: u=User.objects.get(username=request.user); logout(request); u.set_password(request.POST['2']); u.save(); return redirect('loginuser')
                else: context['tip1']='tip1'
            else: context['tip2']='tip2'
            context['oop1']=request.POST['1']; context['oop2']=request.POST['2']; context['oop3']=request.POST['3']
            return render(request, 'chloginps.html',context)
        else: return render(request,'chloginps.html')
    else: return HttpResponse()