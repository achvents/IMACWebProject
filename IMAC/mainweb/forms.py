from django import forms
from .models import staff_imac

#ini buat backend formnya registrasinya 

class StaffForm(forms.ModelForm):

    class Meta:
        model = staff_imac
        db_table = staff_imac
        fields = ['nama','divisi','jurusan','nrp','idimac']
        labels = {
            'nama' : 'Nama Lengkap',
            'divisi' : 'Divisi',
            'jurusan' : 'Departemen Asal',
            'nrp' : 'NRP',
            'idimac' : 'ID IMAC',
            }
    #untuk validasi nih
    def __init__(self, *args, **kwargs):
        super(StaffForm,self).__init__(*args, **kwargs)
        