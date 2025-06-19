# 🛡️ Chatbot Evaluador de Riesgos Laborales - Backend con FastAPI

Este proyecto es una API RESTful desarrollada con **FastAPI** que simula un **chatbot configurable con roles**, utilizando la API de **OpenAI** y persistencia en **SQLite**.

---

## 🚀 Características Principales

- Registro de usuarios con rol (ej: "experto en riesgos laborales")
- Envío de preguntas a GPT y recepción de respuestas contextualizadas
- Persistencia de interacciones en SQLite
- Consulta de historial por usuario
- Endpoints documentados con Swagger
- Código modular, limpio y con pruebas unitarias
- Validado con **Pyright** para asegurar calidad estática

---

## 📦 Tecnologías Utilizadas

- Python 3.10+
- FastAPI
- SQLModel + SQLite
- OpenAI API (gratuita)
- httpx (cliente HTTP asíncrono)
- dotenv (variables de entorno)
- Pytest (pruebas unitarias)
- Pyright (análisis estático de tipos)

---

## ⚙️ Instalación y Ejecución

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/chatbot-backend.git
cd chatbot-backend
```

### 2. Crea y activa un entorno virtual

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura el archivo .env

```bash
OPENAI_API_KEY=sk-***************
OPENAI_API_URL=https://api.openai.com/v1/chat/completions
```

### 5. Ejecuta el servidor

```bash
uvicorn app.main:app --reload
```

### 6. Accede a la documentación interactiva

📘 Swagger UI: http://localhost:8000/docs

🔍 Endpoints disponibles

| Método | Ruta                  | Descripción                          |
| ------ | --------------------- | ------------------------------------ |
| POST   | `/init_user`          | Crear usuario con rol personalizado  |
| POST   | `/ask`                | Enviar pregunta al chatbot           |
| GET    | `/history/{username}` | Consultar historial de interacciones |
| GET    | `/health`             | Verificar salud de la API y DB       |


🧪 Pruebas
Ejecutar pruebas unitarias

pytest tests/

Incluye pruebas para:

    Creación de usuarios

    Consulta de historial

    Comunicación con el chatbot (mockeada)

🧰 Validación de tipos con Pyright

Este proyecto es compatible con Pyright para asegurar calidad de tipos estáticos.
Ejecutar Pyright

pyright

📸 Incluye una captura de pantalla mostrando que no hay errores de tipos.
📌 Decisiones Técnicas

    SQLModel: facilita el trabajo con SQLite y modelos Pydantic/ORM combinados.

    Modularización: rutas separadas por función (chat, user, health).

    Mocking en pruebas: evita gastar tokens de OpenAI en testing.

    dotenv: permite mantener seguras las claves API fuera del código.

    httpx.AsyncClient: para integrarse bien con FastAPI y aprovechar async/await.

📄 Diagrama de Secuencia (simplificado)

sequenceDiagram
    participant Usuario
    participant API
    participant OpenAI
    participant DB

    Usuario->>API: POST /ask (username, message)
    API->>DB: Buscar usuario
    API->>OpenAI: Enviar mensaje con rol
    OpenAI-->>API: Respuesta del modelo
    API->>DB: Guardar pregunta y respuesta
    API-->>Usuario: Devolver respuesta

✅ Estado del Proyecto

✔️ Funcional, probado y listo para evaluación.
👨‍💻 Autor

Desarrollado por [Tu Nombre]
[LinkedIn] - [GitHub]

📸 Ver captura de Pyright en /docs/pyright_ok.png