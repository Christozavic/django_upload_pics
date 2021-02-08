from django.shortcuts import render
from django.http import HttpResponse
from .models import UploadPics
from .forms import PicsForm
from django.conf import settings


# Create your views here.
def upload(request, template_name='upload.html'):
    if request.method == 'POST':
        form = PicsForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.get('pic', None)
            with open('test.jpg', 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
    else:
        form = PicsForm()
    return render(request, template_name, {
        'form': form,
    })
