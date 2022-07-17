from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import City, DailyFeed,Clipping,DailySpecialAkola,DailySpecialBuldhana,PageOneClip,PageTwoClip,TopAdds,BottomAdds
from .forms import DailyFeedForm,SignUpForm,RetrieveForm,ClippingForm,DailySpecialFeedForm,DailySpecialBuldhanaForm,PageOneClipForm,PageTwoClipForm,TopAddsForm,BottomAddsForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
import datetime
from django.shortcuts import redirect
from pdf2image import convert_from_path
from cloudinary.forms import cl_init_js_callbacks
from django.views.decorators.csrf import csrf_exempt
from django_user_agents.utils import get_user_agent
from django.urls import reverse
import json
from datetime import datetime, timedelta
#ToDO
# Add convert to image
# Add Clipping and Share
# Add Date range
# Add Supplement option

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def city(request):
    # user_agent = get_user_agent(request)
    # if user_agent.is_mobile:
    #     return redirect('city')
    # else:
    city_list = City.objects.all()
    date = timezone.now().date()
    form = request.POST.get('retrive_date',default='{}'.format(timezone.now().date()))
    city = DailyFeed.objects.filter(date=form)
    daily = DailySpecialAkola.objects.filter(date=form).first()
    akola = DailyFeed.objects.filter(city__name = "Akola").filter(date=form).first()
    topadd = TopAdds.objects.filter(add_date=form).first()
    bottomadd = BottomAdds.objects.filter(bottom_add_date=form).first()
    buldhana = DailyFeed.objects.filter(city__name = "Buldhana").filter(date=form).first()
    buldhanaspecial = DailySpecialBuldhana.objects.filter(date=form).first()
    return render (request,'main.html',{'city_list':city_list,'city':city,'date':date,'topadd':topadd,'bottomadd':bottomadd,'akola':akola,'buldhana':buldhana,'daily':daily,'buldhanaspecial':buldhanaspecial,'retrive_date':form})

@csrf_exempt
def mobileview(request,cityid):
    # user_agent = get_user_agent(request)
    # if user_agent.is_mobile:
    #     return redirect('city')
    # else:
    topadd = TopAdds.objects.filter(add_date=timezone.now().date()).first()
    bottomadd = BottomAdds.objects.filter(bottom_add_date=timezone.now().date()).first()
    ab = City.objects.get(pk=cityid)
    abc = ab.dailyfeed_set.all().filter(date=timezone.now())
    city = DailyFeed.objects.filter(date=timezone.now().date())
    city_list = City.objects.all()
    # form = request.POST.get('retrive_date',default='{}'.format(timezone.now().date()))
    # print(form)
    daily = DailyFeed.objects.filter(date=timezone.now().date()).filter(city= cityid).first()

    abc = daily.page1.url[:-4] +".jpg"
    abc2 = daily.page2.url[:-4] +".jpg"
    abc3 = daily.page3.url[:-4] +".jpg"
    abc4 = daily.page4.url[:-4] +".jpg"
    abc5 = daily.page5.url[:-4] +".jpg"
    abc6 = daily.page6.url[:-4] +".jpg"
    abc7 = daily.page7.url[:-4] +".jpg"
    abc8 = daily.page8.url[:-4] +".jpg"
    abc9 = daily.page9.url[:-4] +".jpg"
    abc10 = daily.page10.url[:-4] +".jpg"
    abc11 = daily.page11.url[:-4] +".jpg"
    abc12 = daily.page12.url[:-4] +".jpg"
    abcsmall = daily.page1.url[:-4] +".jpg"
    abcsmall2 = daily.page2.url[:-4] +".jpg"
    abcsmall3 = daily.page3.url[:-4] +".jpg"
    abcsmall4 = daily.page4.url[:-4] +".jpg"
    abcsmall5 = daily.page5.url[:-4] +".jpg"
    abcsmall6 = daily.page6.url[:-4] +".jpg"
    abcsmall7 = daily.page7.url[:-4] +".jpg"
    abcsmall8 = daily.page8.url[:-4] +".jpg"
    abcsmall9 = daily.page9.url[:-4] +".jpg"
    abcsmall10 = daily.page10.url[:-4] +".jpg"
    abcsmall11 = daily.page11.url[:-4] +".jpg"
    abcsmall12 = daily.page12.url[:-4] +".jpg"
    if request.method == 'POST':
        backendform = ClippingForm(request.POST, request.FILES)
        # if form:
        #     daily = DailyFeed.objects.filter(date=form).filter(city= cityid).first()
        #     abc = daily.page1.url[:-4] +".jpg"
        #     abc2 = daily.page2.url[:-4] +".jpg"
        #     abc3 = daily.page3.url[:-4] +".jpg"
        #     abc4 = daily.page4.url[:-4] +".jpg"
        #     abc5 = daily.page5.url[:-4] +".jpg"
        #     abc6 = daily.page6.url[:-4] +".jpg"
        #     abc7 = daily.page7.url[:-4] +".jpg"
        #     abc8 = daily.page8.url[:-4] +".jpg"
        #     abcsmall = daily.page1.url[:-4] +".jpg"
        #     abcsmall2 = daily.page2.url[:-4] +".jpg"
        #     abcsmall3 = daily.page3.url[:-4] +".jpg"
        #     abcsmall4 = daily.page4.url[:-4] +".jpg"
        #     abcsmall5 = daily.page5.url[:-4] +".jpg"
        #     abcsmall6 = daily.page6.url[:-4] +".jpg"
        #     abcsmall7 = daily.page7.url[:-4] +".jpg"
        #     abcsmall8 = daily.page8.url[:-4] +".jpg"
        if backendform.is_valid():
            response_data = {}
            backendform.save()
            response_data['id'] = backendform.instance.id
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        else:
            return HttpResponse(backendform.errors)
    else:
        backendform = ClippingForm()


    return render(request,'mobile_view.html',{'backendform':backendform,
    'ab':ab,
    'topadd':topadd,
    'bottomadd':bottomadd,
    'daily':daily,
    'city_list':city_list,
    'page1':abc,
    'page2':abc2,
    'page3':abc3,
    'page4':abc4,
    'page5':abc5,
    'page6':abc6,
    'page7':abc7,
    'page8':abc8,
    'page9':abc9,
    'page10':abc10,
    'page11':abc11,
    'page12':abc12,
    'page1small': abcsmall,
    'page2small':abcsmall2 ,
    'page3small':abcsmall3 ,
    'page4small':abcsmall4 ,
    'page5small':abcsmall5 ,
    'page6small':abcsmall6 ,
    'page7small':abcsmall7 ,
    'page8small':abcsmall8  ,
     'page9small':abcsmall9  ,
      'page10small':abcsmall10  ,
       'page11small':abcsmall11  ,
        'page12small':abcsmall12  ,
    'city':city,})



@csrf_exempt
def mobileviewform(request,cityid):
    # user_agent = get_user_agent(request)
    # if user_agent.is_mobile:
    #     return redirect('city')
    # else:
        ab = City.objects.get(pk=cityid)
        abc = ab.dailyfeed_set.all().filter(date=timezone.now())
        city = DailyFeed.objects.filter(date=timezone.now().date())
        city_list = City.objects.all()
        yesterday = datetime.now() - timedelta(1)
        yesterdayform = datetime.strftime(yesterday, '%Y-%m-%d')
        form = request.POST.get('retrive_date',default='{}'.format(yesterdayform))
        print(form)
        daily = DailyFeed.objects.filter(date=form).filter(city= cityid).first()

        abc = daily.page1.url[:-4] +".jpg"
        abc2 = daily.page2.url[:-4] +".jpg"
        abc3 = daily.page3.url[:-4] +".jpg"
        abc4 = daily.page4.url[:-4] +".jpg"
        abc5 = daily.page5.url[:-4] +".jpg"
        abc6 = daily.page6.url[:-4] +".jpg"
        abc7 = daily.page7.url[:-4] +".jpg"
        abc8 = daily.page8.url[:-4] +".jpg"
        # abc9 = daily.page9.url[:-4] +".jpg"
        # abc10 = daily.page10.url[:-4] +".jpg"
        # abc11 = daily.page11.url[:-4] +".jpg"
        # abc12 = daily.page12.url[:-4] +".jpg"
        abcsmall = daily.page1.url[:-4] +".jpg"
        abcsmall2 = daily.page2.url[:-4] +".jpg"
        abcsmall3 = daily.page3.url[:-4] +".jpg"
        abcsmall4 = daily.page4.url[:-4] +".jpg"
        abcsmall5 = daily.page5.url[:-4] +".jpg"
        abcsmall6 = daily.page6.url[:-4] +".jpg"
        abcsmall7 = daily.page7.url[:-4] +".jpg"
        abcsmall8 = daily.page8.url[:-4] +".jpg"
        # abcsmall9 = daily.page9.url[:-4] +".jpg"
        # abcsmall10 = daily.page10.url[:-4] +".jpg"
        # abcsmall11 = daily.page11.url[:-4] +".jpg"
        # abcsmall12 = daily.page12.url[:-4] +".jpg"
        return render(request,'mobile_view_form.html',{'retrive_date':form,
        'ab':ab,
        'daily':daily,
        'city_list':city_list,
        'page1':abc,
        'page2':abc2,
        'page3':abc3,
        'page4':abc4,
        'page5':abc5,
        'page6':abc6,
        'page7':abc7,
        'page8':abc8,
        'page9':abc9,
        'page10':abc10,
        'page11':abc11,
        'page12':abc12,
        'page1small': abcsmall,
        'page2small':abcsmall2 ,
        'page3small':abcsmall3 ,
        'page4small':abcsmall4 ,
        'page5small':abcsmall5 ,
        'page6small':abcsmall6 ,
        'page7small':abcsmall7 ,
        'page8small':abcsmall8  ,
        #  'page9small':abcsmall9  ,
        #   'page10small':abcsmall10  ,
        #   'page11small':abcsmall11  ,
        #     'page12small':abcsmall12  ,
        'city':city,})


@login_required
def dashboard(request):
    daily = DailyFeed.objects.all()
    city = DailyFeed.objects.filter(date=timezone.now().date())
    return render (request,'dash.html',{'daily':daily,'city':city})


@login_required
def create_dailyfeed(request):

    if request.method == 'POST' :
        #Get All Files
        files = request.FILES.getlist('files')
        form = DailyFeedForm(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            for f in files:
                filename = inst.files.save(f.name, f)
            inst.save()
            # pages1 = convert_from_path('{}'.format(inst.page1.path), 50)
            # pages1large = convert_from_path('{}'.format(inst.page1.path), 115)
            # pages2 = convert_from_path('{}'.format(inst.page2.path), 50)
            # pages2large = convert_from_path('{}'.format(inst.page2.path), 115)
            # pages3 = convert_from_path('{}'.format(inst.page3.path), 50)
            # pages3large = convert_from_path('{}'.format(inst.page3.path), 115)
            # pages4 = convert_from_path('{}'.format(inst.page4.path), 50)
            # pages4large = convert_from_path('{}'.format(inst.page4.path), 115)
            # pages5 = convert_from_path('{}'.format(inst.page5.path), 50)
            # pages5large = convert_from_path('{}'.format(inst.page5.path), 115)
            # pagformes7large = convert_from_path('{}'.format(inst.page7.path), 115)
            # pages8 = convert_from_path('{}'.format(inst.page8.path), 50)
            # pages8large = convert_from_path('{}'.format(inst.page8.path), 115)

            # for page1,page2,page3,page4,page5,page6,page7,page8,page1large,page2large,page3large,page4large,page5large,page6large,page7large,page8large in zip(pages1,pages2,pages3,pages4,pages5,pages6,pages7,pages8,pages1large,pages2large,pages3large,pages4large,pages5large,pages6large,pages7large,pages8large):
            #     page1.save('{}'.format(inst.page1.path)[:-4] +".jpg", 'JPEG')
            #     page2.save('{}'.format(inst.page2.path)[:-4] +".jpg", 'JPEG')
            #     page3.save('{}'.format(inst.page3.path)[:-4] +".jpg", 'JPEG')
            #     page4.save('{}'.format(inst.page4.path)[:-4] +".jpg", 'JPEG')
            #     page5.save('{}'.format(inst.page5.path)[:-4] +".jpg", 'JPEG')
            #     page6.save('{}'.format(inst.page6.path)[:-4] +".jpg", 'JPEG')
            #     page7.save('{}'.format(inst.page7.path)[:-4] +".jpg", 'JPEG')
            #     page8.save('{}'.format(inst.page8.path)[:-4] +".jpg", 'JPEG')
            #     page1large.save('{}'.format(inst.page1.path)[:-4] +"large.jpg", 'JPEG')
            #     page2large.save('{}'.format(inst.page2.path)[:-4] +"large.jpg", 'JPEG')
            #     page3large.save('{}'.format(inst.page3.path)[:-4] +"large.jpg", 'JPEG')
            #     page4large.save('{}'.format(inst.page4.path)[:-4] +"large.jpg", 'JPEG')
            #     page5large.save('{}'.format(inst.page5.path)[:-4] +"large.jpg", 'JPEG')
            #     page6large.save('{}'.format(inst.page6.path)[:-4] +"large.jpg", 'JPEG')
            #     page7large.save('{}'.format(inst.page7.path)[:-4] +"large.jpg", 'JPEG')
            #     page8large.save('{}'.format(inst.page8.path)[:-4] +"large.jpg", 'JPEG')
            return redirect('/', messages.success(request, 'Paper is successfully created.', 'alert-success'))
        else:
            return HttpResponse(form.errors)
    else:
        form = DailyFeedForm()
        return render(request,'newspaper.htm',{'form' : form})

@login_required
def create_dailyspecialfeed(request):

    if request.method == 'POST' :
        #Get All Files
        files = request.FILES.getlist('files')
        form1 = DailySpecialFeedForm(request.POST, request.FILES)
        if form1.is_valid():
            inst = form1.save(commit=False)
            # for f in files:
            #     filename = inst.files.save(f.name, f)
            inst.save()
            # pages1 = convert_from_path('{}'.format(inst.specialpage1.path), 50)
            # pages1large = convert_from_path('{}'.format(inst.specialpage1.path), 115)
            # pages2 = convert_from_path('{}'.format(inst.specialpage2.path), 50)
            # pages2large = convert_from_path('{}'.format(inst.specialpage2.path), 115)
            # pages3 = convert_from_path('{}'.format(inst.specialpage3.path), 50)
            # pages3large = convert_from_path('{}'.format(inst.specialpage3.path), 115)
            # pages4 = convert_from_path('{}'.format(inst.specialpage4.path), 50)
            # pages4large = convert_from_path('{}'.format(inst.specialpage4.path), 115)
            # for page1,page2,page3,page4,page1large,page2large,page3large,page4large in zip(pages1,pages2,pages3,pages4,pages1large,pages2large,pages3large,pages4large):
            #     page1.save('{}'.format(inst.specialpage1.path)[:-4] +".jpg", 'JPEG')
            #     page2.save('{}'.format(inst.specialpage2.path)[:-4] +".jpg", 'JPEG')
            #     page3.save('{}'.format(inst.specialpage3.path)[:-4] +".jpg", 'JPEG')
            #     page4.save('{}'.format(inst.specialpage4.path)[:-4] +".jpg", 'JPEG')
            #     page1large.save('{}'.format(inst.specialpage1.path)[:-4] +"large.jpg", 'JPEG')
            #     page2large.save('{}'.format(inst.specialpage2.path)[:-4] +"large.jpg", 'JPEG')
            #     page3large.save('{}'.format(inst.specialpage3.path)[:-4] +"large.jpg", 'JPEG')
            #     page4large.save('{}'.format(inst.specialpage4.path)[:-4] +"large.jpg", 'JPEG')
            return redirect('/', messages.success(request, 'Paper is successfully created.', 'alert-success'))
        else:
            return HttpResponse(form1.errors)
    else:
        form1 = DailySpecialFeedForm()
        return render(request,'akolaspecial.htm',{'form1' : form1})


@login_required
def create_dailybuldhanafeed(request):

    if request.method == 'POST' :
        #Get All Files
        files = request.FILES.getlist('files')
        form1 = DailySpecialBuldhanaForm(request.POST, request.FILES)
        if form1.is_valid():
            inst = form1.save(commit=False)
            # for f in files:
            #     filename = inst.files.save(f.name, f)
            inst.save()
            # pages1 = convert_from_path('{}'.format(inst.specialpage1.path), 50)
            # pages1large = convert_from_path('{}'.format(inst.specialpage1.path), 115)
            # pages2 = convert_from_path('{}'.format(inst.specialpage2.path), 50)
            # pages2large = convert_from_path('{}'.format(inst.specialpage2.path), 115)
            # pages3 = convert_from_path('{}'.format(inst.specialpage3.path), 50)
            # pages3large = convert_from_path('{}'.format(inst.specialpage3.path), 115)
            # pages4 = convert_from_path('{}'.format(inst.specialpage4.path), 50)
            # pages4large = convert_from_path('{}'.format(inst.specialpage4.path), 115)
            # for page1,page2,page3,page4,page1large,page2large,page3large,page4large in zip(pages1,pages2,pages3,pages4,pages1large,pages2large,pages3large,pages4large):
            #     page1.save('{}'.format(inst.specialpage1.path)[:-4] +".jpg", 'JPEG')
            #     page2.save('{}'.format(inst.specialpage2.path)[:-4] +".jpg", 'JPEG')
            #     page3.save('{}'.format(inst.specialpage3.path)[:-4] +".jpg", 'JPEG')
            #     page4.save('{}'.format(inst.specialpage4.path)[:-4] +".jpg", 'JPEG')
            #     page1large.save('{}'.format(inst.specialpage1.path)[:-4] +"large.jpg", 'JPEG')
            #     page2large.save('{}'.format(inst.specialpage2.path)[:-4] +"large.jpg", 'JPEG')
            #     page3large.save('{}'.format(inst.specialpage3.path)[:-4] +"large.jpg", 'JPEG')
            #     page4large.save('{}'.format(inst.specialpage4.path)[:-4] +"large.jpg", 'JPEG')
            return redirect('maindashboard', messages.success(request, 'Paper is successfully created.', 'alert-success'))
        else:
            return HttpResponse(form1.errors)
    else:
        form1 = DailySpecialBuldhanaForm()
        return render(request,'buldhanaspecial.html',{'form1' : form1})


@login_required
def create_pageoneclip(request):

    if request.method == 'POST' :
        files = request.FILES.getlist('files')
        form1 = PageOneClipForm(request.POST, request.FILES)
        if form1.is_valid():
            inst = form1.save(commit=False)
            inst.save()

            return redirect('maindashboard', messages.success(request, 'Paper is successfully created.', 'alert-success'))
        else:
            return HttpResponse(form1.errors)
    else:
        form1 = PageOneClipForm()
        return render(request,'pageoneclip.html',{'form1' : form1})


@login_required
def create_pagetwoclip(request):

    if request.method == 'POST' :
        files = request.FILES.getlist('files')
        form1 = PageTwoClipForm(request.POST, request.FILES)
        if form1.is_valid():
            inst = form1.save(commit=False)
            inst.save()
            return redirect('maindashboard', messages.success(request, 'Paper is successfully created.', 'alert-success'))
        else:
            return HttpResponse(form1.errors)
    else:
        form1 = PageTwoClipForm()
        return render(request,'pagetwoclip.html',{'form1' : form1})



@csrf_exempt
def dateview(request,cityid):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return HttpResponseRedirect(reverse('mobileview', args=(cityid,)))
    else:
        topadd = TopAdds.objects.filter(add_date=timezone.now().date()).first()
        bottomadd = BottomAdds.objects.filter(bottom_add_date=timezone.now().date()).first()
        ab = City.objects.get(pk=cityid)
        abc = ab.dailyfeed_set.all().filter(date=timezone.now())
        city = DailyFeed.objects.filter(date=timezone.now().date())
        city_list = City.objects.all()
        form = request.POST.get('retrive_date',default='{}'.format(timezone.now().date()))
        print(form)
        daily = DailyFeed.objects.filter(date=form).filter(city= cityid).first()

        abc = daily.page1.url[:-4] +".jpg"
        abc2 = daily.page2.url[:-4] +".jpg"
        abc3 = daily.page3.url[:-4] +".jpg"
        abc4 = daily.page4.url[:-4] +".jpg"
        abc5 = daily.page5.url[:-4] +".jpg"
        abc6 = daily.page6.url[:-4] +".jpg"
        abc7 = daily.page7.url[:-4] +".jpg"
        abc8 = daily.page8.url[:-4] +".jpg"
        abc9 = daily.page9.url[:-4] +".jpg"
        abc10 = daily.page10.url[:-4] +".jpg"
        abc11 = daily.page11.url[:-4] +".jpg"
        abc12 = daily.page12.url[:-4] +".jpg"
        abcsmall = daily.page1.url[:-4] +".jpg"
        abcsmall2 = daily.page2.url[:-4] +".jpg"
        abcsmall3 = daily.page3.url[:-4] +".jpg"
        abcsmall4 = daily.page4.url[:-4] +".jpg"
        abcsmall5 = daily.page5.url[:-4] +".jpg"
        abcsmall6 = daily.page6.url[:-4] +".jpg"
        abcsmall7 = daily.page7.url[:-4] +".jpg"
        abcsmall8 = daily.page8.url[:-4] +".jpg"
        abcsmall9 = daily.page9.url[:-4] +".jpg"
        abcsmall10 = daily.page10.url[:-4] +".jpg"
        abcsmall11 = daily.page11.url[:-4] +".jpg"
        abcsmall12 = daily.page12.url[:-4] +".jpg"
        if request.method == 'POST':
            backendform = ClippingForm(request.POST, request.FILES)
            if backendform.is_valid():
                backendform.save()
                return redirect('/', messages.success(request, 'Clip is successfully created.', 'alert-success'))
            else:
                return HttpResponse(backendform.errors)
        else:
            backendform = ClippingForm()


        return render(request,'daily_view.html',{'backendform':backendform,
        'ab':ab,
        'topadd':topadd,
        'bottomadd':bottomadd,
        'daily':daily,
        'retrive_date':form,
        'city_list':city_list,
        'page1':abc,
        'page2':abc2,
        'page3':abc3,
        'page4':abc4,
        'page5':abc5,
        'page6':abc6,
        'page7':abc7,
        'page8':abc8,
         'page9':abc9,
          'page10':abc10,
           'page11':abc11,
            'page12':abc12,
        'page1small': abcsmall,
        'page2small':abcsmall2 ,
        'page3small':abcsmall3 ,
        'page4small':abcsmall4 ,
        'page5small':abcsmall5 ,
        'page6small':abcsmall6 ,
        'page7small':abcsmall7 ,
        'page8small':abcsmall8  ,
        'page9small':abcsmall9  ,
        'page10small':abcsmall10  ,
        'page11small':abcsmall11 ,
        'page12small':abcsmall12  ,
        'city':city,})

def datespecialview(request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return HttpResponseRedirect(reverse('datespecialmobileview'))
    else:
        city = DailySpecialAkola.objects.filter(date=timezone.now().date())
        city_list = City.objects.all()
        form = request.POST.get('retrive_date',default='{}'.format(timezone.now().date()))
        print(form)
        daily = DailySpecialAkola.objects.filter(date=form).first()
        abc = daily.specialakola1.url[:-4] +".jpg"
        abc2 = daily.specialakola2.url[:-4] +".jpg"
        abc3 = daily.specialakola3.url[:-4] +".jpg"
        abc4 = daily.specialakola4.url[:-4] +".jpg"
        abc5 = daily.specialakola5.url[:-4] +".jpg"
        abc6 = daily.specialakola6.url[:-4] +".jpg"
        abc7 = daily.specialakola7.url[:-4] +".jpg"
        abc8 = daily.specialakola8.url[:-4] +".jpg"


        return render(request,'daily_specialview.html',{'city':city,'daily':daily,'retrive_date':form,'city_list':city_list,'page1':abc,'page2':abc2,'page3':abc3,'page4':abc4,'page5': abc5,'page6':abc6 , 'page7':abc7 , 'page8':abc8 ,})

def datespecialmobileview(request):
    city = DailySpecialAkola.objects.filter(date=timezone.now().date())
    city_list = City.objects.all()
    form = request.POST.get('retrive_date',default='{}'.format(timezone.now().date()))
    print(form)
    daily = DailySpecialAkola.objects.filter(date=form).first()
    abc = daily.specialakola1.url[:-4] +".jpg"
    abc2 = daily.specialakola2.url[:-4] +".jpg"
    abc3 = daily.specialakola3.url[:-4] +".jpg"
    abc4 = daily.specialakola4.url[:-4] +".jpg"
    abc5 = daily.specialakola5.url[:-4] +".jpg"
    abc6 = daily.specialakola6.url[:-4] +".jpg"
    abc7 = daily.specialakola7.url[:-4] +".jpg"
    abc8 = daily.specialakola8.url[:-4] +".jpg"


    return render(request,'daily_specialmobileview.html',{'city':city,'daily':daily,'retrive_date':form,'city_list':city_list,'page1':abc,'page2':abc2,'page3':abc3,'page4':abc4,'page5': abc5,'page6':abc6 , 'page7':abc7 , 'page8':abc8 ,})


def datespecialbuldhanaview(request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return HttpResponseRedirect(reverse('datespecialbuldhanamobileview'))
    else:
        city = DailySpecialBuldhana.objects.filter(date=timezone.now().date())
        city_list = City.objects.all()
        form = request.POST.get('retrive_date',default='{}'.format(timezone.now().date()))
        print(form)
        daily = DailySpecialBuldhana.objects.filter(date=form).first()
        abc = daily.specialbuldhana1.url[:-4] +".jpg"
        abc2 = daily.specialbuldhana2.url[:-4] +".jpg"
        abc3 = daily.specialbuldhana3.url[:-4] +".jpg"
        abc4 = daily.specialbuldhana4.url[:-4] +".jpg"
        abc5 = daily.specialbuldhana5.url[:-4] +".jpg"
        abc6 = daily.specialbuldhana6.url[:-4] +".jpg"
        abc7 = daily.specialbuldhana7.url[:-4] +".jpg"
        abc8 = daily.specialbuldhana8.url[:-4] +".jpg"


        return render(request,'daily_buldhanaview.html',{'city':city,'daily':daily,'retrive_date':form,'city_list':city_list,'page1':abc,'page2':abc2,'page3':abc3,'page4':abc4,'page5': abc5,'page6':abc6 , 'page7':abc7 , 'page8':abc8 ,})


def datespecialbuldhanamobileview(request):
    city = DailySpecialBuldhana.objects.filter(date=timezone.now().date())
    city_list = City.objects.all()
    form = request.POST.get('retrive_date',default='{}'.format(timezone.now().date()))
    print(form)
    daily = DailySpecialBuldhana.objects.filter(date=form).first()
    abc = daily.specialbuldhana1.url[:-4] +".jpg"
    abc2 = daily.specialbuldhana2.url[:-4] +".jpg"
    abc3 = daily.specialbuldhana3.url[:-4] +".jpg"
    abc4 = daily.specialbuldhana4.url[:-4] +".jpg"
    abc5 = daily.specialbuldhana5.url[:-4] +".jpg"
    abc6 = daily.specialbuldhana6.url[:-4] +".jpg"
    abc7 = daily.specialbuldhana7.url[:-4] +".jpg"
    abc8 = daily.specialbuldhana8.url[:-4] +".jpg"

    return render(request,'daily_buldhanamobileview.html',{'city':city,'daily':daily,'retrive_date':form,'city_list':city_list,'page1':abc,'page2':abc2,'page3':abc3,'page4':abc4,'page5': abc5,'page6':abc6 , 'page7':abc7 , 'page8':abc8 ,})


def clipdata(request,id):
    clip = Clipping.objects.get(pk=id)
    return render(request,'clip.html',{'clip':clip})

@login_required
def top_add(request):

    if request.method == 'POST' :
        #Get All Files
        form = TopAddsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('maindashboard', messages.success(request, 'Add is successfully created.', 'alert-success'))
        else :
            return HttpResponse(form.errors)
    else:
        form = TopAddsForm()
    return render(request,'topaddform.html',{'form':form})

@login_required
def bottom_add(request):

    if request.method == 'POST' :
        #Get All Files
        form = BottomAddsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('maindashboard', messages.success(request, 'Add is successfully created.', 'alert-success'))
        else :
            return HttpResponse(form.errors)
    else:
        form = BottomAddsForm()
    return render(request,'bottomadd.html',{'form':form})

@login_required
def maindashboard(request):
    return render(request,'index.html',)
