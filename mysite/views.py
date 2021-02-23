# I created this file-Krupal.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render


def index(request):
    # parameter = {'name': 'krupal', 'place': 'mars'}
    return render(request,'index.html')
    # return HttpResponse("Home")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text',"default")
    #  check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        # analyze = djtext

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        # return  render(request, 'analyze.html' ,params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose':'Change to uppercase','analyzed_text':analyzed}
        djtext = analyzed

        # return render(request,'analyze.html',params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose':'Remove New line','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]== " " and djtext[index+1] == " ":
                pass
            else:

                analyzed = analyzed + char

        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(removepunc !="on" and fullcaps!="on" and newlineremover !="on" and extraspaceremover !="on"):
        return HttpResponse("please select any operations and try again..")

    return render(request, 'analyze.html', params)
