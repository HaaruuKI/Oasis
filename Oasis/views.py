from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from steam import Steam

def IA(request):
    API_KEY = "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"
    MODEL = "text-davinci-003"
    t = request.GET['texto']
    respuesta = requests.post(
    f"https://api.openai.com/v1/engines/{MODEL}/completions",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"prompt": t, "max_tokens": 150},
    )
    respuesta.raise_for_status()
    texto = respuesta.json()["choices"][0]["text"]
    
    respuesta = texto
    return render(request,"blog/chatIA.html",{"respuesta": respuesta})

@login_required
def Games(request):
    KEY = 'AD00A005102CE567F19D7148973DD9B9'
    steam = Steam(KEY)
    
    men = request.GET["buscar"]

    games = steam.apps.search_games(men)
    gamess = []
    for game in games["apps"]:
         gamess.append({
            'name': game['name'],
            'price': game['price'],
            'img': game['img']
        })
        
    

    API_KEY = "e96570333f471bc980102be2bfe80303"
    CITY = "Nogales, Sonora, Mexico"

    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    )

    data = response.json()

    weather_description = data["weather"][0]["description"]
    
    v = "https://www.youtube.com/embed/AlWgZhMtlWo"

    return render(request,"blog/games.html",{"games": gamess,"weather": weather_description, "video": v})


# def index(request):
#     texto = "Este es un mensaje de prueba"
#     return render(request, 'blog/chatIA.html',{"texto": texto})