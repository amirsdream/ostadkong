from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from poem.models import Poem
# Create your views here.

def main(request):
	poems = Poem.objects.all()
	return render(request, 'index.html',{'poems':poems})

def poet(request,pk):
	poem = get_object_or_404(Poem,pk=pk)
	return render(request, 'index2.html',{'poem':poem})