from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
	return HttpResponse('<h1>Olá {}</h1><h2>{} anos</h2>'.format(nome,idade))
