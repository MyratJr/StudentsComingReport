from django.core.exceptions import ObjectDoesNotExist;from random import randint;from datetime import datetime; from django.shortcuts import render,redirect; from django.http import HttpResponse; from .models import*; from django.contrib.auth import authenticate,logout,login; from dbr import*; from .forms import*; import json; from django.db.models import Q; from django.contrib.auth.models import User; from dateutil.relativedelta import relativedelta; from django.views.decorators.csrf import requires_csrf_token


@requires_csrf_token
def maglumat(request):
    dtgun=datetime.date.today(); date=datetime.datetime.now()
    if request.method == "POST":
        form=Code_getter(request.POST)
        if form.is_valid():
            got=form.cleaned_data['barkod']; context={'form':Code_getter}
            if len(str(got)) == 13:
                q=Isgar_Gunler.objects.filter(day=dtgun).count()
                if q==0:
                    p=Isgar_Gunler(day=dtgun);p.save();n1=Ishgarler.objects.filter
                    for i in n1(balnoy=True,balnoy_sony=dtgun): i.balnoy=False; i.save()
                    for i in n1(balnoy=False,balnoy_bash=dtgun): i.balnoy=True; i.save()
                    for i in n1(~Q(balnoy_wagt__overlap=[str(dtgun)]),balnoy=True): i.balnoy_wagt.append(str(dtgun)); i.all_start.append(i.balnoy_bash); i.all_end.append(i.balnoy_sony); i.save()
                try: a=Ishgarler.objects.get(barkod_san=got)
                except ObjectDoesNotExist: context['bellik0']='Işgär tapylmady, täzeden synanyşyň!'; return render(request,'derweze.html',context)
            elif len(str(got)) == 12:
                q=Dinleyji_Gunler.objects.filter(day=dtgun).count()
                if q==0: p=Dinleyji_Gunler(day=dtgun); p.save()
                try: a=Dinleyjiler.objects.get(barkod_san=got)
                except ObjectDoesNotExist: context['bellik0']='Diňleýji tapylmady, täzeden synanyşyň!'; return render(request,'derweze.html',context)
            else: context['bellik0']='Barkod nädogry, täzeden synanyşyň!'; return render(request,'derweze.html',context)
            if date.strftime('%Y-%m-%d') not in a.gelen_wagty:
                if date.strftime('%H:%M:%S')<='12:00:00': a.gelen_wagty[date.strftime('%Y-%m-%d')]=date.strftime('%H:%M'); context['wagt1']=a.gelen_wagty[date.strftime('%Y-%m-%d')]; context['a']=a; context['bellik1']='Siz içeri girdiňiz!'
                else: context['gic']=date.strftime('%H:%M'); context['a']=a; context['bellik0']="'12:00:00'-dan soň giriş kabul edilmeýär!"
            elif date.strftime('%Y-%m-%d') not in a.giden_wagty:
                ae=datetime.datetime.strptime((a.gelen_wagty[date.strftime('%Y-%m-%d')]),'%H:%M')
                if (date.hour*60)+(date.minute)-(ae.hour*60)+(ae.minute)>10:
                    a.giden_wagty[date.strftime('%Y-%m-%d')]=date.strftime('%H:%M'); context['wagt']=a.giden_wagty[date.strftime('%Y-%m-%d')]; context['wagt1']=a.gelen_wagty[date.strftime('%Y-%m-%d')]
                    if len(str(got)) == 13:
                        b=datetime.datetime.strptime(context['wagt'], '%H:%M').time(); b1=datetime.datetime.strptime(context['wagt1'], '%H:%M').time(); z=((b.hour*60)+(b.minute))-((b1.hour*60)+(b1.minute)); a.activesagat+=z//60; a.activeminut+=z%60
                        if a.activeminut>=60: p1=a.activeminut//60; a.activesagat+=p1; a.activeminut-=p1*60
                    context['a']=a; context['bellik1']='Siz çykdyňyz!'
                else: context['a']=a; context['bellik0']='Bagyşlaň siz diňe 10 minut soňra çykyp bilýäňiz!'; context['wagt1']=a.gelen_wagty[date.strftime('%Y-%m-%d')]
            elif date.strftime('%Y-%m-%d') in a.giden_wagty and date.strftime('%Y-%m-%d') in a.gelen_wagty: context['wagt']=a.giden_wagty[date.strftime('%Y-%m-%d')]; context['wagt1']=a.gelen_wagty[date.strftime('%Y-%m-%d')]; context['a']=a; context['bellik0']='Bagyşlaň siziň görkezmäňiz ozal kabul edildi!'
            a.save(); return render(request,'derweze.html',context)
        else: context={'form':Code_getter}; context['bellik0']='Nädogry barkod görnüşi, barkodyňyzyň görnüşiniň dogrulygyny anyklaň!'; return render(request,'derweze.html',context)
    else: return render(request,'derweze.html',{'form':Code_getter})

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def delete_item(request,id,which):
    if request.user.is_authenticated:
        if request.method=='POST':
            if which==4: u=Dinleyjiler.objects.get(id=id); bold=Kurslar.objects.get(Kurs_at=u.kurs); deleted=u.at; u.delete(); bold.san-=1; bold.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{deleted} sanawdan aýryldy."})})
            elif which==5: u=Ishgarler.objects.get(id=id); bold=Wezipeler.objects.get(Wezipe_at=u.wezipe); deleted=u.at; u.delete(); bold.san-=1; bold.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{deleted} sanawdan aýryldy."})})
        elif which==5: return render(request,'all_modal.html',{'a5':Ishgarler.objects.get(id=id)})
        elif which==4: return render(request,'all_modal.html',{'a10':Dinleyjiler.objects.get(id=id)})
    else: return redirect('/')

def update(request,id,which):
    if request.user.is_authenticated:
        if request.method=='POST':
            if which==0:
                id_ishgar=Ishgarler.objects.get(id=id)
                if id_ishgar.at==request.POST['at'] and str(id_ishgar.wezipe)==request.POST['wezipe'] and id_ishgar.is_bashlayar==request.POST['wagt1'] and id_ishgar.is_gutaryar==request.POST['wagt2'] and id_ishgar.obed_bashlayar==request.POST['wagt3'] and id_ishgar.obed_gutaryar==request.POST['wagt4']: return HttpResponse()
                else:
                    T_A=id_ishgar.at; id_ishgar.at = request.POST['at']
                    if not (id_ishgar.is_bashlayar==request.POST['wagt1'] and id_ishgar.is_gutaryar==request.POST['wagt2'] and id_ishgar.obed_bashlayar==request.POST['wagt3'] and id_ishgar.obed_gutaryar==request.POST['wagt4']): id_ishgar.is_bashlayar= request.POST['wagt1']; id_ishgar.is_gutaryar = request.POST['wagt2']; id_ishgar.obed_bashlayar = request.POST['wagt3']; id_ishgar.obed_gutaryar = request.POST['wagt4']; id_ishgar.save()
                    else:
                        if str(id_ishgar.wezipe)!=request.POST['wezipe']: pol=Wezipeler.objects.get(Wezipe_at=request.POST['wezipe']); id_ishgar.is_bashlayar=pol.is_bashlayar; id_ishgar.is_gutaryar = pol.is_gutaryar; id_ishgar.obed_bashlayar = pol.obed_bashlayar; id_ishgar.obed_gutaryar = pol.obed_gutaryar
                    id_ishgar.wezipe=Wezipeler.objects.get(Wezipe_at=request.POST['wezipe']); id_ishgar.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{T_A} maglumaty üýtgedildi."})})
            elif which==4:
                q=Dinleyjiler.objects.get(id=id)
                if q.at==request.POST['at'] and str(q.kurs)==request.POST['wezipe'] and q.okuw_bashlayar==request.POST['wagt1'] and q.okuw_gutaryar==request.POST['wagt2']: return HttpResponse(status=204)
                else:T_A=q.at; q.at = request.POST['at']; q.kurs=Kurslar.objects.get(Kurs_at=request.POST['wezipe']); q.okuw_bashlayar = request.POST['wagt1']; q.okuw_gutaryar = request.POST['wagt2']; q.save();return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{T_A} maglumaty üýtgedildi."})})
            elif which==2:
                q=Wezipeler.objects.get(id=id); o1=q.Wezipe_at
                if q.Wezipe_at==request.POST['at'] and q.is_bashlayar==request.POST['wagt1'] and q.is_gutaryar==request.POST['wagt2'] and q.obed_bashlayar==request.POST['wagt3'] and q.obed_gutaryar==request.POST['wagt4']: return HttpResponse(status=204)
                else:
                    q.Wezipe_at=request.POST['at']; q.is_bashlayar=request.POST['wagt1']; q.is_gutaryar=request.POST['wagt2']; q.obed_bashlayar=request.POST['wagt3']; q.obed_gutaryar=request.POST['wagt4']; q.save(); rt=Ishgarler.objects.select_related('wezipe').filter(wezipe=q.id)
                    for n in rt: n.is_bashlayar=request.POST['wagt1']; n.is_gutaryar=request.POST['wagt2']; n.obed_bashlayar=request.POST['wagt3']; n.obed_gutaryar=request.POST['wagt4']; n.save()
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
        elif which==0: return render(request,'ishgarler_form.html',{'movie':Ishgarler.objects.get(id=id),'a6':Wezipeler.objects.all()})
        elif which==4: return render(request,'all_modal.html',{'movie':Dinleyjiler.objects.get(id=id),'a11':Kurslar.objects.all()})
        elif which==2: return render(request,'all_modal.html',{'a7':Wezipeler.objects.get(id=id)})
        elif which==3: return render(request,'all_modal.html',{'a8':Rugsatlar.objects.get(id=id)})
        elif which==5: return render(request,'all_modal.html',{'a2':Kurslar.objects.get(id=id)})
        else: return HttpResponse()
    else: return redirect('/')

def creating(request,san):
    if request.user.is_authenticated:
        if request.method=='POST':
            if san==0: wzp=Wezipeler(Wezipe_at=request.POST['at'], is_bashlayar=request.POST['wagt1'], is_gutaryar=request.POST['wagt2'], obed_bashlayar=request.POST['wagt3'], obed_gutaryar=request.POST['wagt4']); wzp.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{wzp} wezipesi döredildi."})})
            elif san==2: wzp=Rugsatlar(Rugsat_at=request.POST['at']); wzp.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{wzp} rugsady döredildi."})})
            elif san==4: wzp=Kurslar(Kurs_at=request.POST['at'], okuw_bashlayar=request.POST['wagt1'], okuw_gutaryar=request.POST['wagt2']); wzp.save(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged": None,"showMessage": f"{wzp} Kursy döredildi."})})
            elif san==1:
                def salam():
                    sana=0; sen=randint(1000000000000,9999999999999)
                    for i in Ishgarler.objects.select_related('kurs'):
                        if i.barkod_san==sen: sana+=1
                    if sana>0: return salam()
                    elif sana==0: bold=Wezipeler.objects.get(Wezipe_at=request.POST['wezipe']); saving=Ishgarler(at=request.POST['at'], wezipe=bold, gelen_wagty={None:None}, giden_wagty={None:None}, is_bashlayar=bold.is_bashlayar, is_gutaryar=bold.is_gutaryar, obed_bashlayar=bold.obed_bashlayar, obed_gutaryar=bold.obed_gutaryar, barkod_san=sen); saving.save(); bold.san+=1; bold.save()
                salam(); return HttpResponse(status=204,headers={'HX-Trigger': json.dumps({"movieListChanged":True,"showMessage": f"{request.POST['at']} döredildi."})})
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
        elif san==1: return render(request,'all_modal.html',{'a4':Wezipeler.objects.all()})
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