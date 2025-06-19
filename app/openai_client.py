import httpx
from app.config import OPENAI_API_KEY, OPENAI_API_URL


async def get_openai_response(prompt: str, role: str) -> str:
    """
    Send message to openai

    :param prompt: Question.
    :param role: Role.
    :return: Response.
    """
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": f"Eres un {role}."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(OPENAI_API_URL, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
    except httpx.HTTPStatusError as e:
        print(f"Error en la respuesta de OpenAI: {e.response.status_code} - {e.response.text}")
        raise RuntimeError("Error al comunicarse con OpenAI.")
    except Exception as e:
        print(f"Error inesperado al conectar con OpenAI: {e}")
        raise RuntimeError("Error desconocido al obtener la respuesta del chatbot.")
