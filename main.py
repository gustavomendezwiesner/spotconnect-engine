import os
from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = FastAPI(
    title="SpotConnect Engine Core",
    description="Backend de integración con WhatsApp Business API para recintos de gran escala."
)

VERIFY_TOKEN = os.getenv("WEBHOOK_VERIFY_TOKEN", "spotconnect_secret_token_2026")

@app.get("/")
def root():
    return {"status": "online", "system": "SpotConnect Engine v1.0"}

# 1. Verificación del Webhook enviada por Meta/WhatsApp
@app.get("/webhook", response_class=PlainTextResponse)
def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_verify_token: str = Query(None, alias="hub.verify_token"),
    hub_challenge: str = Query(None, alias="hub.challenge")
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        print("✅ Webhook verificado correctamente con Meta.")
        return hub_challenge
    
    raise HTTPException(status_code=403, detail="Token de verificación inválido")

# 2. Recepción de eventos y mensajes de usuarios en tiempo real
@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    
    try:
        entry = data.get("entry", [])[0]
        changes = entry.get("changes", [])[0]
        value = changes.get("value", {})
        messages = value.get("messages", [])
        
        if messages:
            msg = messages[0]
            from_number = msg.get("from")  # Teléfono del usuario
            text_body = msg.get("text", {}).get("body", "")  # Mensaje recibido
            
            print(f"📩 [SpotConnect Engine] Mensaje de {from_number}: '{text_body}'")
            
            # Aquí se conectarán las respuestas automatizadas / IA
            
    except Exception as e:
        print(f"⚠️ Error procesando mensaje: {e}")
        
    return {"status": "EVENT_RECEIVED"}