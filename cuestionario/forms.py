from django import forms

mood = (
    (1, "Bien"),
    (2, "Mas o menos"),
    (3, "Mal"),
)

class MoodForm(forms.Form):
    mood_field = forms.ChoiceField(choices= mood, label = "¿Como estas? ")
    mood1_field = forms.ChoiceField(choices= mood, label = "¿Como te encuentras? ")
