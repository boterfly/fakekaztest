from django.shortcuts import render
from .models import *
import zipfile
import os
from io import BytesIO
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        action = 'email link'
        # print (email)
        if (email):
            obj = IndexModel(email=email, action=action)
            obj.save()
    return render(
        request,
        'index.html',
        context={'email':email},
    )

def archive(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        action = request.GET.get('action')
        # print (email)
        if (email):
            if(action):
                obj = IndexModel(email=email, action=action)
                obj.save()
                filelist = ["catalog/static/files/file1.txt", "catalog/static/files/file2.txt", "catalog/static/files/file3.txt"]
                byte_data = BytesIO()
                zipFile = zipfile.ZipFile(byte_data, "w")

                for file in filelist:
                    filename = os.path.basename(os.path.normpath(file))
                    zipFile.write(file, filename)
                zipFile.close()

                response = HttpResponse(byte_data.getvalue(), content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename=files.zip'

                return response