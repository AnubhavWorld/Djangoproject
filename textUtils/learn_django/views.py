from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'home2.html',{})  
def analyze(request):
    text=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed_text=""
    if removepunc== 'on':
        for char in text:
            if char not in punctuations:
                analyzed_text+=char
    else:
        analyzed_text=text
    params={'purpose':'Removed Punctuations','analyzed_text':analyzed_text}
    return render(request,'analyze.html',params)




def capitalizefirst(request):
    return HttpResponse('capitalizefirst')
def newlineremove(request):
    return HttpResponse('newlineremove')
def spaceremove(request):
    return HttpResponse('spaceremove')
def charcount(request):
    return HttpResponse('charcount')
