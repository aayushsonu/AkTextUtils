from django.http import HttpResponse
from django.shortcuts import render

# Basic understanding of Django
'''
def index(request):
    return HttpResponse("Hello Aayush, Here you can also inject JavaScript <script>('like this')</script><br><a href='https://www.facebook.com'>fb</a><br><a href='https://www.youtube.com'>YouTube</a><br><a href='https://www.google.com'>google</a><br><a href='https://www.codewitharry.com'>codewithharry</a><br><a href='https://www.facebook.com'>xyz</a>")

def contact(request):
    file=open("./textutils/abc.txt",'r+')
    text=HttpResponse(file.read())
    file.close()
    return text
'''

# Concept Of Templating

def index(request):
    return render(request,'index.html')

# Analyze function or main function for this TextUtils website.

def analyze(request):
    
    # Get the TEXT
    
    djText=request.POST.get('text','default')

    # check checkbox values
    removepunc=request.POST.get('removepunc','off')
    capitilize=request.POST.get('capitilize','off')
    newLineRemover=request.POST.get('newLineRemover','off')
    extraSpaceRemover=request.POST.get('extraSpaceRemover','off')
    charcount=request.POST.get('charcount','off')

    # Analyse the TEXT
    punc='''~`!@#$%^&*()_+-={[]}\|;:,></.'''
    params={"result":"","purpose":""}

    # Check which checkbox is ON
    # if removepunc=='on' and capitilize=='on':
    #     params["purpose"]="Capitilization and Punctuations Removal"
    #     for char in djText:
    #         if char not in punc:
    #             params["result"]=params["result"]+char
    #         params["result"]=params["result"].upper()

    if removepunc =='on':
        for char in djText:
            if char not in punc:
                params["result"]=params["result"]+char
                params["purpose"]="Remove Punctuations"
        djText=params["result"]        

    if capitilize=='on':
        params["result"]=djText.upper()
        params["purpose"]="Capitilization"
        djText=params["result"]  

    if newLineRemover=='on':
        params["result"]=""
        params["purpose"]="New Line Remover"
        for char in djText:
            if char != '\n' and char != '\r':
                params["result"]=params["result"]+char
        djText=params["result"]  

    if extraSpaceRemover=='on':
        params["result"]=""
        params["purpose"]="Extra Space Remover"
        for i, char in enumerate(djText):
            if not (djText[i]==' ' and (djText[i+1]==' ')):
                params["result"]=params["result"]+char

    if charcount == 'on':
        params["R1"]="Character Count is " + str(len(djText))
        params["purpose"]="Character Count"
    
    if charcount == 'off' and newLineRemover=='off' and removepunc =='off' and capitilize=='off' and extraSpaceRemover=='off':
        params["result"]="Check any option first"

    # return template
    return render(request,'analyze.html',params)


# Adding About and Contact Page

def about(request):
    return HttpResponse("<h1>This is About Page.</h1>")

def contact(request):
    return HttpResponse("<h1>This is Contact Page.</h1>")