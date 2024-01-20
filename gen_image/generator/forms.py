from django import forms


class GenerateImageForm(forms.Form):
    model_choices = [
        ('StableDiffusion1.0', 'StableDiffusion 1.0'),
        ('StableDiffusion1.4', 'StableDiffusion 1.4'),
        ('StableDiffusion1.5', 'StableDiffusion 1.5'),
        ('StableDiffusion2.0', 'StableDiffusion 2.0'),
        ('StableDiffusion2.1', 'StableDiffusion 2.1'),
    ]

    model = forms.ChoiceField(
        choices=model_choices,
        label='Выберите модель'
    )
    prompt = forms.CharField(
        max_length=255,
        label='Какое изображение нужно сгенерировать'
    )
    negative_prompt = forms.CharField(
        max_length=255,
        label='Чего не должно быть в изображении'
    )
    width = forms.IntegerField(
        initial=512,
        label='Ширина изображения'
    )
    height = forms.IntegerField(
        initial=512,
        label='Высота изображения'
    )
