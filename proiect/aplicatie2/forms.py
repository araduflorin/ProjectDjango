from django import forms

from aplicatie2.models import Companies


class CompaniesClass(forms.ModelForm):

    class Meta:
        model = Companies
        fields = ['name','website','company_type','location']