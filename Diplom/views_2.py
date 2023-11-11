from django.core.exceptions import ObjectDoesNotExist;from random import randint;import datetime; from django.shortcuts import render,redirect; from django.http import HttpResponse; from .models import*; from django.contrib.auth import authenticate,logout,login; from dbr import*; from .forms import*; import json; from django.db.models import Q; from django.contrib.auth.models import User; from dateutil.relativedelta import relativedelta; from django.views.decorators.csrf import requires_csrf_token

@requires_csrf_token
def maglumat(request):
    dtgun=datetime.date.today(); date=datetime.datetime.now()
    if request.method == "POST":
        form=Code_getter(request.POST)
        if form.is_valid():
            got=form.cleaned_data['barkod']; context={'form':Code_getter}
            if len(str(got)) == 13:
                q=Talyp_Gunler.objects.filter(day=dtgun).count()
                if q==0:
                    p=Talyp_Gunler(day=dtgun)
                    p.save()
                try: a=Talyplar.objects.get(barkod_san=got)
                except ObjectDoesNotExist: context['bellik0']='Talyp tapylmady, täzeden synanyşyň!'; return render(request,'derweze.html',context)
            else: context['bellik0']='Barkod nädogry, täzeden synanyşyň!'; return render(request,'derweze.html',context)
            if date.strftime('%Y-%m-%d') not in a.gelen_wagty:
                a.gelen_wagty[date.strftime('%Y-%m-%d')]=date.strftime('%H:%M'); context['wagt1']=a.gelen_wagty[date.strftime('%Y-%m-%d')]; context['a']=a
                if date.strftime('%H:%M')<="13:00":
                    context['bellik1']='Siz wagtynda geldiňiz'
                    context['bellik2']='Giriş wagt hasaba alyndy!'
                else:
                    context['bellik0']='Siz gijä galdyňyz'
                    context['bellik1']="Giriş wagt hasaba alyndy!"
            elif date.strftime('%Y-%m-%d') in a.gelen_wagty: context['wagt1']=a.gelen_wagty[date.strftime('%Y-%m-%d')]; context['a']=a; context['bellik1']='Giriş wagt hasaba alyndy!'
            a.save(); return render(request,'derweze.html',context)
        else: context={'form':Code_getter}; context['bellik0']='Nädogry barkod görnüşi, barkodyňyzyň görnüşiniň dogrulygyny anyklaň!'; return render(request,'derweze.html',context)
    else: return render(request,'derweze.html',{'form':Code_getter})

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def delete_item(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            u=Talyplar.objects.get(id=id); deleted=u.at; u.delete(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{deleted} sanawdan aýryldy."})})
        return render(request,'all_modal.html',{'a5':Talyplar.objects.get(id=id)})
    else: return redirect('/')

def update(request,id,which):
    if request.user.is_authenticated:
        if request.method=='POST':
            if which==0:
                id_ishgar=Talyplar.objects.get(id=id)
                if id_ishgar.at==request.POST['at'] and str(id_ishgar.topar)==request.POST['topar'] and str(id_ishgar.ID_NO)==request.POST['ID_NO']: return HttpResponse()
                else:
                    T_A=id_ishgar.at
                    id_ishgar.at = request.POST['at']
                    id_ishgar.ID_NO=request.POST['ID_NO']
                    id_ishgar.topar=Toparlar.objects.get(Topar_at=request.POST['topar'])
                    id_ishgar.save();
                    return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{T_A} maglumaty üýtgedildi."})})
            elif which==2:
                q=Toparlar.objects.get(id=id); o1=q.Topar_at
                if q.Topar_at==request.POST['at']: return HttpResponse(status=204)
                else:
                    q.Topar_at=request.POST['at']; q.save()
                return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{o1} maglumatlary üýtgedildi."})})
            else: return HttpResponse()
        elif which==0: return render(request,'ishgarler_form.html',{'movie':Talyplar.objects.get(id=id),'a6':Toparlar.objects.all()})
        elif which==2: return render(request,'all_modal.html',{'a7':Toparlar.objects.get(id=id)})
        else: return HttpResponse()
    else: return redirect('/')

def creating(request,san):
    if request.user.is_authenticated:
        if request.method=='POST':
            if san==0: wzp=Toparlar(Topar_at=request.POST['at']); wzp.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{wzp} topary döredildi."})})
            elif san==1:
                def salam():
                    sana=0; sen=randint(1000000000000,9999999999999)
                    for i in Talyplar.objects.select_related('topar'):
                        if i.barkod_san==sen: sana+=1
                    if sana>0: return salam()
                    elif sana==0: bold=Toparlar.objects.get(Topar_at=request.POST['topar']); saving=Talyplar(at=request.POST['at'], topar=bold, gelen_wagty={None:None},ID_NO=request.POST['id_no'],barkod_san=sen);saving.save()
                salam();return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged":True,"showMessage": f"{request.POST['at']} döredildi."})})
            return HttpResponse()
        elif san==1: return render(request,'all_modal.html',{'a4':Toparlar.objects.all()})
        elif san==0: return render(request,'all_modal.html',{'a6':'a6'})
        return HttpResponse()
    return HttpResponse()