from django import forms

mood = (
    (1, "Casi nunca"),
    (2, "Pocas veces"),
    (3, "Unas veces sí, otras veces no"),
    (4, "Muchas veces"),
    (5, "Casi siempre"),
)

class MoodForm(forms.Form):
    mood_field = forms.ChoiceField(choices= mood, label = "¿Como estas? ")
    mood1_field = forms.ChoiceField(choices= mood, widget=forms.RadioSelect())
