from django import forms
from django.contrib.auth.password_validation import validate_password

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)  # Valider le mot de passe avec les règles de Django

        # Calculer le score du mot de passe
        score = self.calculate_password_score(password)

        if score < 3:
            raise forms.ValidationError("Le mot de passe est trop faible. Veuillez en choisir un plus fort.")
        return password

    @staticmethod
    def calculate_password_score(password):
        # Implémentation du calcul du score du mot de passe
        score = 0
        if len(password) >= 8:
            score += 1
        if any(char.isdigit() for char in password):
            score += 1
        if any(char.isalpha() for char in password):
            score += 1
        if any(char.isupper() for char in password) and any(char.islower() for char in password):
            score += 1
        if any(char.isalnum() for char in password):
            score += 1
        return score
