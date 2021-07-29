from django.shortcuts import render, redirect, HttpResponse
import random

# Create your views here.
def root(request):
    if 'count' not in request.session:
        request.session['count'] = '0'
    if int(request.session['count'])<=5:
        request.session['triesleft'] = 5 - (int(request.session['count']))
    else:
        request.session['reset'] = False
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
    print(f"===================The random number generated is: {request.session['number']}====================")
    if 'username' not in request.session:
        request.session['username'] = "Mr/Mrs. Doodle!"
    if 'guessnumber' not in request.session:
        request.session['guessnumber'] = ''
    if 'color' not in request.session:
        request.session['color'] = 'white'
    if 'replay' not in request.session:
        request.session['replay'] = False
    if 'result' not in request.session:
        request.session['result'] = ''
    context = {
        'result' : request.session['result'],
        'color' : request.session['color'],
        'replay' : request.session['replay'],
        'count' : request.session['count'],
        'username' : request.session['username'],
        'triesleft' : request.session['triesleft']
    }
    
    return render(request, 'index.html', context)

def process(request):
    request.session['guessnumber'] = request.POST['guessnumber']
    if request.session['guessnumber'] == '':
        request.session['result'] = "Please enter a valid number!"
        request.session['color'] = "red"
        request.session['replay'] = False
        print(request.session['result'])

    elif int(request.session['guessnumber']) > int(request.session['number']):
        request.session['result'] = "Too High!!"
        request.session['color'] = "red"
        request.session['replay'] = False
        print(request.session['result'])

    elif int(request.session['guessnumber']) < int(request.session['number']):
        request.session['result'] = "Too Low!!"
        request.session['color'] = "red"
        request.session['replay'] = False
        print(request.session['result'])

    else:
        request.session['result'] = f"{request.session['guessnumber']} was the number!"
        request.session['color'] = "green"
        request.session['replay'] = True
        print(request.session['result'])
    
    request.session['count'] = int(request.session['count'])+1

    return redirect('/')

def congrats_page(request):
    
    context2 ={
        'count' : request.session['count'],
        'username' : request.session['username']
    }
    return render (request, 'congrats.html', context2)
    
def success(request):
    request.session['username'] = request.POST['username']
    return redirect('/congrats')

def destroy_session(request):
    request.session.flush()
    return redirect('/')