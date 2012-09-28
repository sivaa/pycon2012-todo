from django.forms import ModelForm, ValidationError
from tasks.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task

    def clean_name(self):
        print "============================="
        name = self.cleaned_data['name']
       
        if len(name) < 5:
            raise ValidationError("Task Name should be minimum of 5 chars")
        return name