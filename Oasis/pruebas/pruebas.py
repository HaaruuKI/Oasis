import requests

def simulate_paypal_payment(amount, currency, description):
  """Simula un pago con PayPal.

  Args:
    amount: El monto del pago.
    currency: La moneda del pago.
    description: La descripción del pago.

  Returns:
    Un objeto JSON con la información del pago simulado.
  """

  # Genera un ID de transacción aleatorio.
  transaction_id = "1234567890"

  # Crea los datos de la solicitud.
  data = {
    "intent": "sale",
    "payer": {
      "payment_method": "paypal"
    },
    "transactions": [
      {
        "amount": {
          "total": amount,
          "currency": currency
        },
        "description": description
      }
    ]
  }

  # Realiza la solicitud a la API de PayPal.
  response = requests.post(
    "https://api.sandbox.paypal.com/v2/payments",
    data=data,
    headers={"Authorization": "Bearer YOUR_PAYPAL_ACCESS_TOKEN"}
  )

  # Verifica el estado de la respuesta.
  if response.status_code == 201:
    return response.json()
  else:
    raise Exception(f"Error al procesar el pago: {response.status_code}")


if __name__ == "__main__":
  # Simula un pago de $100 USD.
  payment = simulate_paypal_payment(100, "USD", "Pago simulado")

  # Imprime la información del pago.
  print(payment)
