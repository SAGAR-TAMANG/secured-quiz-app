from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
# @xframe_options_exempt
def index(request):
    if request.method == 'POST':
        # Store the value in session
        request.session['url'] = request.POST.get("search_space")
        request.session['timer'] = request.POST.get("search_space")
        print("All options: ", request.POST)
        print("Inside index()")
        print("Context:", request.session['url'])
        return redirect('main')
    return render(request, 'index.html')

def main(request):
    if request.method == 'POST':
        print("Inside main()")
    # Retrieve the value from session
    url = request.session.get('url', None)  
    timer = request.session.get('timer', None)
    context = {
        'url': url,
        'timer': timer,
    }
    return render(request, 'main.html', context)
