# I have created this File - Niranj
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #params = {'name':'Harry', 'place':'earth'}
    return render(request, 'index.html')


# return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    removepunc =request.POST.get('removepunc','off')
    capitalize =request.POST.get('capitalize','off')
    newlineremover =request.POST.get('newlineremover','off')
    spaceremover =request.POST.get('spaceremover','off')
    charcount =request.POST.get('charcount','off')
    #analyzed = djtext
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                    analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation','analyzed_text': analyzed}
        djtext = analyzed
        #return render( request ,'analyze.html',params)


    if capitalize == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if spaceremover == "on":
        analyzed = ""
        for index,char in  enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if charcount == "on":
        analyzed = ""
        analyzed = analyzed + str(len(djtext))


        params = {'purpose': 'Characters are Counted', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    if(removepunc != "on" and newlineremover != "on" and capitalize != "on" and spaceremover != "on" and charcount != "on" ):
        return HttpResponse("Error! No Methods Selected")





    return render(request, 'analyze.html', params)