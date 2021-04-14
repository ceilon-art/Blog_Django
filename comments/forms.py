from django.forms import ModelForm
from .models import Comments


class FormComment(ModelForm):
    def clean(self):
        data = self.cleaned_data
        name = data.get('comment_name')
        email = data.get('comment_email')
        comment = data.get('comment')

        if len(name) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais de 5 caracteres'
            )

    class Meta:
        model = Comments
        fields = ('comment_name', 'comment_email', 'comment')
