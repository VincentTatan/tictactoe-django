from django.shortcuts import render

def welcome(request):
    return render(request, 'tictactoestart/welcome.html')