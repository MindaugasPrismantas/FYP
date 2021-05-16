import json

from django.shortcuts import redirect
from .models import Upload

# Create your views here.


def delete_file(request, pk):
    if request.method == 'POST':
        file = Upload.objects.get(pk=pk)
        file.delete()
    return redirect('file_list')
