from django.shortcuts import render

def test(request):
    form = 3
    return render(request, 'home.html', {'form': form})