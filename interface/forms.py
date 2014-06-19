import requests
from django import forms


class ProcedureCreateForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    id = forms.CharField(max_length=255)

    def clean(self):
        super(ProcedureCreateForm, self).clean()

        data = {}

        for key, value in self.cleaned_data.items():
            data[key] = value

        r = requests.post('http://127.0.0.1:8000/api/procedure/', data=data)

        raise forms.ValidationError(r.text)

        return self.cleaned_data


class ProcedureUpdateForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean(self):
        super(ProcedureUpdateForm, self).clean()

        data = {}

        for key, value in self.cleaned_data.items():
            data[key] = value

        print data

        print 'http://127.0.0.1:8000/api/procedure/'+str(data['id'])+'/'

        r = requests.put('http://127.0.0.1:8000/api/procedure/'+str(data['id'])+'/', data=data)

        raise forms.ValidationError(r.text)

        print self.cleaned_data


class ProcedureDeleteForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean(self):
        super(ProcedureDeleteForm, self).clean()

        data = {}

        for key, value in self.cleaned_data.items():
            data[key] = value

        r = requests.delete('http://127.0.0.1:8000/api/procedure/'+str(data['id'])+'/', data=data)

        raise forms.ValidationError(r.text)

        print self.cleaned_data


class StepCreateForm(forms.Form):
    order = forms.IntegerField(initial='0')
    description = forms.CharField(max_length=255)

    def clean(self):
        super(StepForm, self).clean()

        data = {}

        for key, value in self.cleaned_data.items():
            data[key] = value

        r = requests.post('http://127.0.0.1:8000/api/step/', data = data)

        print r.text

        return self.cleaned_data


# class StepCreateForm(StepForm):

#     def clean(self):
#         super(StepForm, self).clean()

#         data = {}

#         for key, value in self.cleaned_data:
#             data[key] = value

#         r = requests.post('http://127.0.0.1:8000/api/step/', data = data)

#         print r.text

#         return self.cleaned_data


# class PrecedenceForm(forms.Form):
#     name = forms.CharField(max_length=255)

#     def clean(self):
#         super(PrecedenceForm, self).clean()

#         data = {}

#         data['name'] = self.cleaned_data.get('name')

#         r = requests.post('http://127.0.0.1:8000/api/precedence/', data = data)

#         print r.text

#         return self.cleaned_data


# class PrecedenceCreateForm(StepForm):

#     def clean(self):
#         super(PrecedenceForm, self).clean()

#         data = {}

#         for key, value in self.cleaned_data:
#             data[key] = value

#         r = requests.post('http://127.0.0.1:8000/api/precedence/', data = data)

#         print r.text

#         return self.cleaned_data
