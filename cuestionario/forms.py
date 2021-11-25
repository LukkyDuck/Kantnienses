from django import forms

mood = (
    (0, "Casi nunca"),
    (1, "Pocas veces"),
    (2, "Unas veces sí, otras veces no"),
    (3, "Muchas veces"),
    (4, "Casi siempre"),
)

class MoodForm(forms.Form):
    pregunta1 = forms.ChoiceField(choices= mood, widget=forms.RadioSelect(), required=True)
    pregunta2 = forms.ChoiceField(choices= mood, widget=forms.RadioSelect(), required=True)
    pregunta3 = forms.ChoiceField(choices= mood, widget=forms.RadioSelect(), required=True)
    pregunta4 = forms.ChoiceField(choices= mood, widget=forms.RadioSelect(), required=True)
    pregunta5 = forms.ChoiceField(choices= mood, widget=forms.RadioSelect(), required=True)
    pregunta6 = forms.ChoiceField(choices= mood, widget=forms.RadioSelect(), required=True)
    pregunta7 = forms.ChoiceField(choices= mood, widget=forms.RadioSelect(), required=True)
    pregunta8 = forms.ChoiceField(choices= mood, widget=forms.RadioSelect(), required=True)
    pregunta9 = forms.ChoiceField(choices= mood, widget=forms.RadioSelect(), required=True)
    pregunta10 = forms.ChoiceField(choices= mood, widget=forms.RadioSelect(), required=True)
    pregunta11 = forms.ChoiceField(choices= mood, widget=forms.RadioSelect(), required=True)
    pregunta12 = forms.ChoiceField(choices= mood, widget=forms.RadioSelect(), required=True)
