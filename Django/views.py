# Creates By Me  --> Swastik Dolas

from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'index2.html')

def analyze(request):

    #Getting Text
    temp = request.GET.get('text', 'Default')
    remc = request.GET.get('removepunc', 'off')
    Uppercase = request.GET.get('Uppercase','off')
    Newlineremover =  request.GET.get('Newlineremover','off')
    print(temp)
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
    #Punctuation Remover
    if remc == "on":
        Analyzed = ""
        for char in temp:
            if char not in punc:
                Analyzed = Analyzed + char
                stri = {'purpose':'analyzing word','analyzedtext':Analyzed}
        return render(request,'analyze.html', stri)

    #UPPERCASE Maker
    elif(Uppercase == "on"):
        Analyzed = ""
        for char in temp:
            Analyzed = Analyzed + char.upper()
            stri = {'purpose': 'Changing To UPPERCASE', 'analyzedtext': Analyzed}
        return render(request, 'analyze.html', stri)

    #Newline Remover
    elif(Newlineremover == "on"):
        Analyzed = ""
        for char in temp:
            if char !='\n' and char!='\r':
                Analyzed = Analyzed +  char
                stri = {'purpose': 'Removing New Line', 'analyzedtext': Analyzed}
        return render(request, 'analyze.html', stri)

    else:
        return HttpResponse("Something Went Wrong !!")
    #Removing All Punctuation Marks From temp
