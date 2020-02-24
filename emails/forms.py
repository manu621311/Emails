from django import forms
from .models import Email

class EmailsForm(forms.Form):
    object_list=Email.objects.all()
    choice_list=()
    for x in object_list:
        tux=((x.email,x.email),)
        #tux=((x.email),)
        choice_list+=tux
    email_field=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=choice_list)#doesnot update the form dynamically on updating the model
    '''email_field=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Email.objects.all()['email'])'''#better method.but dont know the usage
    
class EmailContentForm(forms.Form):
    email_subject=forms.CharField(max_length=250,empty_value='Subject')
    email_content=forms.CharField(empty_value='Write your content here...')