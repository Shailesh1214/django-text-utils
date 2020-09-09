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
    # check checkbox value
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    spaceremover = request.GET.get('spaceremover','off')
    charcount = request.GET.get('charcount','off')

    # check which check box is on
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
    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
    #analyze the text
        return render(request,'analyze.html',params)
    elif(newlineremover == "on"):
         analyzed = ""
         for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
         params={'purpose':'Removed NewLines','analyzed_text':analyzed}
    #analyze the text
         return render(request,'analyze.html',params)
    elif(spaceremover == "on"):
         analyzed = ""
         for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index +1] == " "):
                analyzed = analyzed + char
         params={'purpose':'Extra Space Remover','analyzed_text':analyzed}
    #analyze the text
         return render(request,'analyze.html',params)
    elif(charcount == "on"):
         analyzed = ""
         count = 0
         for  char in enumerate(djtext):
                count = count + 1
                analyzed = count
         params={'purpose':'The Number of character in your string','analyzed_text':analyzed}
    #analyze the text
         return render(request,'analyze.html',params)     
    else:
        return HttpResponse("Error")

