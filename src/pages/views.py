from django.shortcuts import render, redirect
from files.forms import UploadForm
from files.models import Upload


# Create your views here.


def home_view(request):
    return render(request, "home.html", {})


def upload_view(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = UploadForm()
    return render(request, 'form_upload.html', {
        'form': form
    })


def file_list_view(request):
    file = Upload.objects.all()
    context = {
        'object': file
    }
    return render(request, "file/detail.html", context)

