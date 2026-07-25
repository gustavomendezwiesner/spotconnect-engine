# 🚀 SpotConnect Engine

**SpotConnect Engine** es el motor conversacional y de mensajería masiva diseñado para la gestión en tiempo real de eventos, congresos y recintos de gran escala[cite: 4].

Sustituye o complementa los sistemas de perifoneo tradicional mediante comunicación silenciosa, inteligente y segmentada por WhatsApp API[cite: 2, 4].

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Frontend / Torre de Control:** React + Tailwind CSS (v0.dev / Next.js)
- **API Integration:** WhatsApp Business API (Meta Cloud API)[cite: 1]

---

## 🖥️ Prototipo de Interfaz: Torre de Control (React)

El sistema cuenta con una plataforma web administrativa (Dashboard Operativo) diseñada para el staff y operadores del recinto[cite: 1, 4]:

- **Multi-Chat Inbox:** Atención y monitoreo de chats en vivo etiquetados por rol (*Asistente*, *Expositor*, *Staff*, *VIP*)[cite: 3, 4].
- **Centro de Broadcast Masivo:** Emisión de alertas de agenda, reubicación de salas y patrocinios mediante plantillas HSM[cite: 3, 4].
- **Analítica Operativa & ROI:** Visualización de tráfico de mensajes por hora, tasa de lectura (>98%) y gestión de tickets de soporte en tiempo real[cite: 1, 3, 4].

---

## 📌 Caso de Estudio Activo (Mock Data)

Para las simulaciones y pruebas de rendimiento, el proyecto utiliza configuraciones de prueba inspiradas en **Colombia Tech Week & Colombia Tech Fest**[cite: 1]:
- **Entorno Centralizado:** Gestión de flujo masivo y logística interna sin perifoneo ruidoso[cite: 1, 2].
- **Entorno Descentralizado:** Avisos de agenda en tiempo real para múltiples *side events* en simultáneo[cite: 1, 4].

> *Nota: SpotConnect Engine es una plataforma SaaS Marca Blanca. El nombre del evento, la agenda y las reglas de IA se adaptan dinámicamente según el cliente o centro de convenciones[cite: 1, 4].*

---

## 📂 Arquitectura del Proyecto

```text
spotconnect-engine/
├── .gitignore
├── README.md        # Documentación ejecutiva y técnica
├── main.py          # Core del Webhook y servidor FastAPI
└── venv/            # Entorno virtual (no versionado)