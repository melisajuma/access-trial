from django.shortcuts import render, redirect
from .models import *
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import viewsets
from .sheet2 import interest_responses, firstapplication_response
# from .sheet3 import assesment_responses, score_response
# from django.contrib.auth.models import User
# from django.shortcuts import render
# from .filters import UserFilter

# Create your views here.
#class Profileview(viewsets.ModelViewSet):
    #queryset= Profile.objects.all()
    #serializer_class = ProfileSerializer


def homepage(request):
    '''
    assuming we make the api call
    
    '''
    
    form_data=interest_responses()
    response = firstapplication_response()

    for email in  interestModel.objects.values_list('email', flat=True).distinct():
        interestModel.objects.filter(pk__in= interestModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()

    res= interestModel.objects.all()
    return render(request,'interest.html',{'data':res})

# def scorecard(request):
#     '''
#     Assuming we make the api call
        
#     '''
#     # form_data=assesment_responses()
#     form_data=assesment_responses()
#     response = score_response()

#     for email in  scoreModel.objects.values_list('email', flat=True).distinct():
#         scoreModel.objects.filter(pk__in= scoreModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()

#     res= scoreModel.objects.all()
#     return render(request,'scores.html',{'data':res})
    

# def search(request):
#     user_list = User.objects.all()
#     user_filter = UserFilter(request.GET, queryset=user_list)
#     return render(request, 'search/user_list.html', {'filter': user_filter})