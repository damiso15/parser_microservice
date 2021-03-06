import os
import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from core.settings import BASE_DIR
from .forms import ExcelUploadForm
from .models import ExcelUpload


# Create your views here.


def index(request):
    pass
    return render(request, 'index.html')


def home(request):
    excel_upload = ExcelUpload.objects.all()
    return render(request, 'excel.html', {'excel_upload': excel_upload})


def form_upload(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('parse:convert')
    else:
        form = ExcelUploadForm()
    return render(request, 'excel.html', {'form': form})


def excel_parse_to_json(request):
    directory = os.path.join(BASE_DIR, r'media\upload')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.xlsx'):
            file_name = os.path.join(directory, filename)
            df = pd.read_excel(file_name, encoding='utf-8')
            data = df.dropna(axis=0, how='any')
            data.columns = data.columns.map(lambda x: str(x))
            data.columns = data.columns.map(lambda x: x.replace('\n', ''))
            final_data = data.to_dict(orient='records')
            return render(request, 'result.html', {'final_data': final_data})
        else:
            return render(request, 'result.html', messages.error(request, 'Error! No excel file found.'))



# file = request.FILES.get('file')
# filename = file.name
# ExcelUpload.objects.create(document=file)
# file_path = request.data.get('file_path')
# print(file_path, request.data)
# file = request.FILES.get('file')
# filename = file.name
# pdf_file_name = filename[-4:]
# ExcelUpload.objects.create(document=file)
