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
                a.gelen_wagty[date.strftime('%Y-%m-%d')]=date.strftime('%H:%M'); context['wagt1']=a.gelen_wagty[date.strftime('%Y-%m-%d')]; context['a']=a; context['bellik1']='Siz içeri girdiňiz!'
            elif date.strftime('%Y-%m-%d') in a.gelen_wagty: context['wagt1']=a.gelen_wagty[date.strftime('%Y-%m-%d')]; context['a']=a; context['bellik1']='Giriş wagt hasaba alyndy!'
            a.save(); return render(request,'derweze.html',context)
        else: context={'form':Code_getter}; context['bellik0']='Nädogry barkod görnüşi, barkodyňyzyň görnüşiniň dogrulygyny anyklaň!'; return render(request,'derweze.html',context)
    else: return render(request,'derweze.html',{'form':Code_getter})

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def delete_item(request,id,which):
    if request.user.is_authenticated:
        if request.method=='POST':
            if which==4: u=Dinleyjiler.objects.get(id=id); bold=Kurslar.objects.get(Kurs_at=u.kurs); deleted=u.at; u.delete(); bold.san-=1; bold.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{deleted} sanawdan aýryldy."})})
            elif which==5: u=Talyplar.objects.get(id=id); deleted=u.at; u.delete(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{deleted} sanawdan aýryldy."})})
        elif which==5: return render(request,'all_modal.html',{'a5':Talyplar.objects.get(id=id)})
        elif which==4: return render(request,'all_modal.html',{'a10':Dinleyjiler.objects.get(id=id)})
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
            elif which==4:
                q=Dinleyjiler.objects.get(id=id)
                if q.at==request.POST['at'] and str(q.kurs)==request.POST['wezipe'] and q.okuw_bashlayar==request.POST['wagt1'] and q.okuw_gutaryar==request.POST['wagt2']: return HttpResponse(status=204)
                else:T_A=q.at; q.at = request.POST['at']; q.kurs=Kurslar.objects.get(Kurs_at=request.POST['wezipe']); q.okuw_bashlayar = request.POST['wagt1']; q.okuw_gutaryar = request.POST['wagt2']; q.save();return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{T_A} maglumaty üýtgedildi."})})
            elif which==2:
                q=Toparlar.objects.get(id=id); o1=q.Topar_at
                if q.Topar_at==request.POST['at']: return HttpResponse(status=204)
                else:
                    q.Topar_at=request.POST['at']; q.save()
                return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{o1} maglumatlary üýtgedildi."})})
            elif which==5:
                q=Kurslar.objects.get(id=id); o1=q.Kurs_at
                if q.Kurs_at==request.POST['at']: return HttpResponse(status=204)
                else: q.Kurs_at=request.POST['at']; q.save()
                return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{o1} {q.Kurs_at}-a üýtgedildi."})})
            elif which==3:
                q=Rugsatlar.objects.get(id=id); o1=q.Rugsat_at
                if q.Rugsat_at==request.POST['at']: return HttpResponse(status=204)
                else: q.Rugsat_at=request.POST['at']; q.save()
                return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{o1} {q.Rugsat_at}-a üýtgedildi."})})
            else: return HttpResponse()
        elif which==0: return render(request,'ishgarler_form.html',{'movie':Talyplar.objects.get(id=id),'a6':Toparlar.objects.all()})
        elif which==4: return render(request,'all_modal.html',{'movie':Dinleyjiler.objects.get(id=id),'a11':Kurslar.objects.all()})
        elif which==2: return render(request,'all_modal.html',{'a7':Toparlar.objects.get(id=id)})
        elif which==3: return render(request,'all_modal.html',{'a8':Rugsatlar.objects.get(id=id)})
        elif which==5: return render(request,'all_modal.html',{'a2':Kurslar.objects.get(id=id)})
        else: return HttpResponse()
    else: return redirect('/')

def creating(request,san):
    if request.user.is_authenticated:
        if request.method=='POST':
            if san==0: wzp=Toparlar(Topar_at=request.POST['at']); wzp.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{wzp} topary döredildi."})})
            elif san==2: wzp=Rugsatlar(Rugsat_at=request.POST['at']); wzp.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{wzp} rugsady döredildi."})})
            elif san==4: wzp=Kurslar(Kurs_at=request.POST['at'], okuw_bashlayar=request.POST['wagt1'], okuw_gutaryar=request.POST['wagt2']); wzp.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{wzp} Kursy döredildi."})})
            elif san==1:
                def salam():
                    sana=0; sen=randint(1000000000000,9999999999999)
                    for i in Talyplar.objects.select_related('topar'):
                        if i.barkod_san==sen: sana+=1
                    if sana>0: return salam()
                    elif sana==0: bold=Toparlar.objects.get(Topar_at=request.POST['topar']); saving=Talyplar(at=request.POST['at'], topar=bold, gelen_wagty={None:None},ID_NO=request.POST['id_no'],barkod_san=sen);saving.save()
                salam();return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged":True,"showMessage": f"{request.POST['at']} döredildi."})})
            elif san==3:
                def hello():
                    sana=0; sen=randint(100000000000,999999999999)
                    for i in Dinleyjiler.objects.all():
                        if i.barkod_san==sen: sana+=1
                    if sana>0: return salam()
                    elif sana==0: bold=Kurslar.objects.get(Kurs_at=request.POST['wezipe']); saving=Dinleyjiler(at= request.POST['at'], kurs=bold, gelen_wagty={None:None}, giden_wagty={None:None}, okuw_bashlayar=bold.okuw_bashlayar, okuw_gutaryar=bold.okuw_gutaryar, barkod_san=sen); saving.save(); bold.san+=1; bold.save()
                hello(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{request.POST['at']} döredildi."})})
            return HttpResponse()
        elif san==3: return render(request,'all_modal.html',{'a3':Kurslar.objects.all()})
        elif san==1: return render(request,'all_modal.html',{'a4':Toparlar.objects.all()})
        elif san==0: return render(request,'all_modal.html',{'a6':'a6'})
        elif san==2: return render(request,'all_modal.html',{'a9':'a9'})
        elif san==4: return render(request,'all_modal.html',{'a1':'a1'})
        return HttpResponse()
    return HttpResponse()

def Rugsat_bermek(request,id,which):
    if request.user.is_authenticated:
        saving=Ishgarler.objects.get(id=id)
        if which==5: saving.balnoy=False; saving.all_start.pop(-1); saving.all_end.pop(-1); saving.balnoy_wagt.pop(-1); saving.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{saving.at} rugsatdan aýryldy."})})
        elif which==0: return render(request,'rugsat.html',{'movie':saving,'rugsatlar':Rugsatlar.objects.all()})
        elif which==6 and request.method=='POST':
            dt=str(datetime.date.today()); saving.balnoy_gornush=Rugsatlar.objects.get(Rugsat_at=request.POST['rugsat']); saving.balnoy_bash = request.POST['wagt1']; saving.balnoy_sony = request.POST['wagt2']; saving.balnoy_beyan = request.POST['beyan']
            if dt>=saving.balnoy_bash: saving.balnoy=True; saving.balnoy_wagt.append(dt); saving.all_start.append(saving.balnoy_bash); saving.all_end.append(saving.balnoy_sony); saving.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{saving.at}-a rugsat berildi."})})
        elif which==7 and request.method=='POST' :
            if Rugsatlar.objects.get(Rugsat_at=request.POST['rugsat'])==saving.balnoy_gornush and str(saving.balnoy_bash)==request.POST['wagt1'] and str(saving.balnoy_sony)==request.POST['wagt2'] and saving.balnoy_beyan==request.POST['beyan']: return HttpResponse()
            else: saving.balnoy_gornush=Rugsatlar.objects.get(Rugsat_at=request.POST['rugsat']); saving.balnoy_bash= request.POST['wagt1']; saving.balnoy_sony= request.POST['wagt2']; saving.balnoy_beyan= request.POST['beyan']; saving.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": "Rugsat maglumatlary üýtgedildi."})})
        return HttpResponse()
    else: return redirect('/')