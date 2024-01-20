import requests
from django.shortcuts import render
from .forms import GenerateImageForm
from .models import GeneratedImage
import os


def generate_image(request):
    result_url = None

    if request.method == 'POST':
        form = GenerateImageForm(request.POST)
        if form.is_valid():
            api_url = "https://stablediffusionapi.com/api/v3/text2img"
            model_key = os.environ.get('MODEL_KEY')

            prompt = form.cleaned_data['prompt']
            negative_prompt = form.cleaned_data['negative_prompt']
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']
            samples = 1
            num_inference_steps = 20
            guidance_scale = 7.5

            payload = {
                "key": model_key,
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "width": width,
                "height": height,
                "samples": samples,
                "num_inference_steps": num_inference_steps,
                "guidance_scale": guidance_scale,
            }

            headers = {'Content-Type': 'application/json'}

            try:
                response = requests.post(
                    api_url,
                    json=payload,
                    headers=headers
                )
                response_data = response.json()

                if response_data.get("status") == "success":
                    result_url = response_data.get("output")[0]

                    # Сохраняем результат в базе данных
                    generated_image = GeneratedImage.objects.create(
                        model=model_key,
                        prompt=prompt,
                        negative_prompt=negative_prompt,
                        width=width,
                        height=height,
                        result=result_url,
                    )
                    generated_image.save()

            except Exception as e:
                # Обработка ошибок при вызове генерации
                return render(
                    request,
                    'error_template.html',
                    {"error_message": str(e)}
                )

    else:
        form = GenerateImageForm()

    return render(
        request,
        'generate_image.html',
        {'form': form,
         'result_url': result_url}
    )
