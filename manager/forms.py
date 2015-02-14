from django import forms
from manager.models import ParserTask, SiteUrl


class ParserTaskForm(forms.ModelForm):
        tasks = forms.ModelMultipleChoiceField(queryset=SiteUrl.objects, widget=forms.CheckboxSelectMultiple(),
                                               required=True)

        class Meta: 
                model = ParserTask
                fields = ('tasks',)