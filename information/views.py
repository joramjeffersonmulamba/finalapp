from django.shortcuts import render

def vip(request):
    # Add any data processing logic here if needed
    context = {}  # You can add data to the context dictionary if needed
    return render(request, 'information/vip.html', context)

def howtoplay(request):
    # Add any data processing logic here if needed
    context = {}  # You can add data to the context dictionary if needed
    return render(request, 'information/howtoplay.html', context)
