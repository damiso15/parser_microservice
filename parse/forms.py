from django import forms
from .models import ExcelUpload


class ExcelUploadForm(forms.ModelForm):
    class Meta:
        model = ExcelUpload
        fields = ('document', )


# class EmailForm(forms.ModelForm):
#     class Meta:
#         model = Email
#         fields = ('upload',)
