import asyncio
import edge_tts
import os

# CONFIGURACIÓN DE LAS VOCES (Para que suenen como niño/a)
VOCES_CONFIG = {
    "ES_NINA": {
        "nombre": "Elvira (Modo Niña)",
        "voz": "es-ES-ElviraNeural",
        "pitch": "+35Hz",  # Sube el tono para agudizar
        "rate": "+10%",    # Aumenta un poco la velocidad
    },
    "EU_NINA": {
        "nombre": "Ainhoa (Modo Niña)",
        "voz": "eu-ES-AinhoaNeural",
        "pitch": "+50Hz",
        "rate": "+5%",
    }
}

# CARPETA DE SALIDA
CARPETA_SALIDA = "audios_online"

async def generar_voz(texto, nombre_archivo, clave_voz):
    if clave_voz not in VOCES_CONFIG:
        print(f"❌ Error: La voz '{clave_voz}' no existe en la configuración.")
        return

    config = VOCES_CONFIG[clave_voz]
    
    # Crear carpeta si no existe
    if not os.path.exists(CARPETA_SALIDA):
        os.makedirs(CARPETA_SALIDA)

    ruta_completa = os.path.join(CARPETA_SALIDA, f"{nombre_archivo}.mp3")

    print(f"🔄 Generando: {nombre_archivo}...")
    
    communicate = edge_tts.Communicate(
        texto, 
        config["voz"], 
        pitch=config["pitch"], 
        rate=config["rate"]
    )

    await communicate.save(ruta_completa)
    print(f"✅ Guardado: {ruta_completa} (Voz: {config['nombre']})")


async def main():
    # ==========================================
    # 📝 LISTA DE FRASES A GENERAR
    # ==========================================
    lista_audios = [
        # Ejemplo Español
        {
            "archivo": "Saludo_ES",
            "voz": "ES_NINA",
            "texto": "¡Hola! Soy Saaki. Me alegro mucho de veros a todos aquí."
        },
        # Ejemplo Euskera
        {
            "archivo": "Agurra_EU",
            "voz": "EU_NINA",
            "texto": "Kaixo! Saaki naiz. Oso pozik nago zuek hemen ikusteagatik."
        },
        # Agregar más frases aquí...
    ]

    for item in lista_audios:
        await generar_voz(item["texto"], item["archivo"], item["voz"])

    print(f"\n🎉 Proceso finalizado. {len(lista_audios)} archivos generados.")

if __name__ == "__main__":
    asyncio.run(main())