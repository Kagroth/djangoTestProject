from django.shortcuts import render
from django.conf import settings

from .models import Directory
import os

# Create your views here.
def index(request):
    return render(request, 'testApp/index.html',  None)


def create_dir(request):
    path_to_create = settings.BASE_DIR + "/foldery/folder_utworzony_z_poziomu_aplikacji"

    message = createDirectory(path_to_create)

    return render(request, 'testApp/create_dir.html', {'message': message})


def createDirectory(pathToCreate):
    # funkcja tworzy folder w lokalizacji path/dirName
    try:
        directory = Directory.objects.create()
        directory.name = "/folder_utworzony_z_poziomu_aplikacji" + str(directory.pk)
        pathToCreate = pathToCreate + "-" + str(directory.pk)

        if os.path.exists(pathToCreate):
            os.rmdir(pathToCreate)
        
        os.mkdir(pathToCreate)

        directory.save()
        return True
    except Exception as e:
        print(str(e))
        return False
    