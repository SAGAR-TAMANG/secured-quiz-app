from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt



# Create your views here.
# @xframe_options_exempt
def index(request):
  return render(request, 'index.html')

def main(request):
  return render(request, 'main.html')