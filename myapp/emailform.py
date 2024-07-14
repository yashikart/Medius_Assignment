from django import forms

class EmailForm(forms.Form):
    from_email = forms.EmailField(label='From Email', required=True)
    to_email = forms.EmailField(label='To Email', required=True)
    subject = forms.CharField(label='Subject', required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
