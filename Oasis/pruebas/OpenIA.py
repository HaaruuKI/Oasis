import requests

# Configura la API de OpenAI
API_KEY = "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"
MODEL = "text-davinci-003"  # modelo

# Define la función de respuesta
def responder(texto):
    try:
        # Realiza la solicitud a la API de OpenAI
        respuesta = requests.post(
            f"https://api.openai.com/v1/engines/{MODEL}/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"prompt": texto, "max_tokens": 150},  # Adjust max_tokens as needed
        )

        # Verifica el código de respuesta HTTP
        respuesta.raise_for_status()

        # Devuelve la respuesta de la API
        return respuesta.json()["choices"][0]["text"]

    except requests.exceptions.RequestException as e:
        # Maneja cualquier error de solicitud
        print(f"Error en la solicitud a la API: {e}")
        return "Lo siento, no pude procesar tu solicitud en este momento."

# Inicia la conversación
while True:
    t = "actuamo como consejero de steam y "
    # Solicita una entrada del usuario
    texto = input("¿Qué deseas preguntar o solicitar? ")+t

    # Genera una respuesta
    respuesta = responder(texto)

    # Imprime la respuesta
    print(respuesta)
