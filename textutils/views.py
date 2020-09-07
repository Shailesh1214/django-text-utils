# I have created this files - shailesh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params= {'name':'shailesh','place':'Pune'}
    return render(request,'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
    #analyze the text
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")

