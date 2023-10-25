from django.core.exceptions import ObjectDoesNotExist;from random import randint;from datetime import datetime; from django.shortcuts import render,redirect; from django.http import HttpResponse; from .models import*; from django.contrib.auth import authenticate,logout,login; from dbr import*; from .forms import*; import json; from django.db.models import Q; from django.contrib.auth.models import User; from dateutil.relativedelta import relativedelta; from django.views.decorators.csrf import requires_csrf_token

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def index_dinleyjiler(request):
    if request.user.id==1 or request.user.id==3: return render(request, 'dinleyjiler.html',{'d7':'d7'})
    else: return HttpResponse(status=204)

def dinleyji_list(request): return render(request, 'table_dinleyji.html', {'dinleyjiler': Dinleyjiler.objects.select_related('kurs')})

def index_ishgarler(request):
    if not request.user.id == 3: return render(request, 'ishgarler.html',{'isgarler':'isgarler'})
    else: return HttpResponse(status=204)

def ishgarler_list(request): return render(request, 'table_ishgarler.html',{'ishgarler': Ishgarler.objects.select_related('wezipe')})

def wezipeler(request):
    if request.user.id==3: return HttpResponse(status=204)
    return render(request,'wezipeler.html',{'wezipelers':Wezipeler.objects.all()})

def wezipe_table(request): return render(request,'wezipe_table.html',{'wezipeler':Wezipeler.objects.all()})

def rugsatlar(request):
    if request.user.id==1 or request.user.id==2: return render(request,'rugsatlar.html',{'rugsatlar':'rugsatlar'})
    else: return HttpResponse(status=204)

def rugsat_table(request): return render(request,'rugsatlar_table.html',{'rugsatlar':Rugsatlar.objects.all()})

def kurslar(request):
    if request.user.id==1 or request.user.id==3: return render(request,'kurslar.html',{'kurslar':Kurslar.objects.all(),'d8':'d8'})
    else: return HttpResponse(status=204)

def kurs_table(request): return render(request,'kurs_table.html',{'kurslar':Kurslar.objects.all()})

def active(request):return render(request,'active.html',{'ok':'ok'})

def active_table(request): context={'Ishgarler':Ishgarler.objects.order_by('-activesagat','-activeminut')}; return render(request,'active_table.html',context)

def home(request): context={'q':Ishgarler.objects.all().count(),'q1':Wezipeler.objects.all().count(),'q2':Kurslar.objects.all().count(),'wezipeler':Wezipeler.objects.all(),'kurslar':Kurslar.objects.all()}; return render(request,'home.html',context)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def wagtynda_gelenler(request,date):
    if date==str(9): date=str(Isgar_Gunler.objects.all().first())
    elif request.method=='POST': date = request.POST['day']
    return render(request,'wagtynda.html',{'aaaaa':date,'day_category':Isgar_Gunler.objects.all(),'w1':'w1'})

def wagtynda_gelenler_table(request,date):
    asd=[];r=Ishgarler.objects.filter(~Q(balnoy_wagt__overlap=[date]) & Q(gelen_wagty__has_key=date))
    for j in r:
        if j.gelen_wagty[date]<=j.is_bashlayar: asd.append(j)
    context={'wagtynda_gelenler':asd,'date':date}
    return render(request,'wagtynda_table.html',context)

def gija_galanlar(request,date):
    if date==str(9): date=str(Isgar_Gunler.objects.all().first())
    elif request.method=='POST': date = request.POST['day']
    return render(request,'gija_galanlar.html',{'aaaaa':date,'day_category':Isgar_Gunler.objects.all(),'g1':'g1',})

def gija_galanlar_table(request,date):
    asd=[]; r=Ishgarler.objects.filter(~Q(balnoy_wagt__overlap=[date]) & Q(gelen_wagty__has_key=date))
    for j in r:
        if j.gelen_wagty[date]>j.is_bashlayar: asd.append(j)
    context={'gija_galanlar':asd,'date':date}
    return render(request,'gija_galanlar_table.html',context)

def ir_gidenler(request,date):
    if date==str(9): date=str(Isgar_Gunler.objects.all().first())
    elif request.method=='POST': date = request.POST['day']
    return render(request,'ir_gidenler.html',{'aaaaa':date,'day_category':Isgar_Gunler.objects.all(),'i':'i',})

def ir_gidenler_table(request,date):
    asd=[]; r=Ishgarler.objects.filter(~Q(balnoy_wagt__overlap=[date]) & Q(gelen_wagty__has_key=date))
    for i in r:
        if (date in i.giden_wagty and i.giden_wagty[date]<i.is_gutaryar) or date not in i.giden_wagty: asd.append(i)
    context={'ir_gidenler':r,'date':date}
    return render(request,'ir_gidenler_table.html',context)

def gelmedikler(request,date):
    if date==str(9): date=str(Isgar_Gunler.objects.all().first())
    elif request.method=='POST': date = request.POST['day']
    return render(request,'gelmedikler.html',{'aaaaa':date,'day_category':Isgar_Gunler.objects.all(),'g2':'g2',})
    
def gelmedikler_table(request,date): r=Ishgarler.objects.filter(~Q(gelen_wagty__has_key=date) & ~Q(balnoy_wagt__overlap=[date]));context={'gelmedikler':r};return render(request,'gelmedikler_table.html',context)

def rugsatlylar(request,date):
    if date==str(9): date=str(Isgar_Gunler.objects.all().first())
    elif request.method=='POST': date = request.POST['day']
    context={'day_category':Isgar_Gunler.objects.all(),'aaaaa':date,'r1':'r1'}
    if str(datetime.date.today())==date: context['green']='green'
    return render(request,'rugsatlylar.html',context)
    
def rugsatlylar_table(request,date):
    dt=str(datetime.date.today()); m5=Ishgarler.objects.filter(balnoy_wagt__overlap=[date])
    if dt!=date:
        for k in m5: k.each_start=k.all_start[k.balnoy_wagt.index(date)]; k.each_end=k.all_end[k.balnoy_wagt.index(date)]; k.save()
    elif dt==date:
        for k in m5: k.each_start=str(k.balnoy_bash); k.each_end=str(k.balnoy_sony); k.save()
    context={'rugsatlylar':m5}
    if dt==date:context['green']='green'
    return render(request,'rugsatlylar_table.html',context)

def gatnasyk1(request,date,kurs):
    if date==str(9): date=str(Dinleyji_Gunler.objects.all().first())
    elif request.method=='POST' and request.POST['day']: date = request.POST['day']; kurs=request.POST['da12']
    context={'aaaaa':date,'day_category':Dinleyji_Gunler.objects.all(),'d9':'d9','kurs':kurs,'kurslar':Kurslar.objects.all()}; return render(request,'gatnasyk.html',context)

def gatnasyk1_table(request,date,kurs):
    if kurs=='all': dinleyjiler=Dinleyjiler.objects.select_related('kurs')
    else: aq=Kurslar.objects.get(Kurs_at=kurs); dinleyjiler=Dinleyjiler.objects.filter(kurs=aq)
    context={'dinleyjiler':dinleyjiler,'date':date,'kurs':kurs}; return render(request,'gatnasyk_table.html',context)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def barkod(request, pk, which):
    if which==1: return render(request,'all_modal.html',{'a12':Ishgarler.objects.get(id=pk)})
    elif which==2: return render(request,'all_modal.html',{'a12':Dinleyjiler.objects.get(id=pk)})

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def hello(request): return render(request,'000.html')

def loginuser(request):
    if request.method=='POST':
        username = request.POST['username']; password = request.POST['password']; user = authenticate(username=username, password=password)
        if user is not None: login(request, user); return redirect('home')
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