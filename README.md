# Generador de Voces para SAAKI (Robot Humanoide)

Este paquete contiene dos herramientas para generar audios.

## 📋 Requisitos Previos

1.  **Python Instalado**: Asegúrate de tener Python 3.x instalado.
2.  **Librerías necesarias**:
    Abre una terminal (CMD o PowerShell) y ejecuta:
    ```bash
    pip install edge-tts pywin32
    ```
3. **Sistema operativo Windows para la versión local**



## 🛠️ OPCIÓN A: Generador Local (Recomendado)

Usa las voces instaladas en tu PC (como AhoTTS) y las modifica con un programa externo.

### Requisitos Extra

**FFmpeg**: Debes tener instalado `ffmpeg` y configurado en las variables de entorno de Windows.
1.  **Descarga**: Ve a la página oficial de FFmpeg y en la sección de Windows selecciona los ejecutables de gyan.dev o BtbN. Descarga el archivo .zip o .7z (generalmente llamado "release-essentials" o "full").
2.  **Extrae**: Descomprime el contenido. Verás una carpeta con subcarpetas como bin, doc y presets.
3.  **Ubica**: Mueve la carpeta extraída a la raíz de tu disco duro (ejemplo: C:\ffmpeg) para que sea fácil de encontrar.
4.  **Configura el PATH**:
        - Busca "Editar las variables de entorno del sistema" en el menú de Inicio y ábrelo.
        - Haz clic en el botón Variables de entorno.
        - En "Variables del sistema", selecciona la fila Path y haz clic en Editar.
        - Haz clic en Nuevo y pega la ruta a la carpeta bin de FFmpeg (ejemplo: C:\ffmpeg\bin).
        - Acepta todos los cuadros de diálogo.
5.  **Verificación**: Para confirmar que todo funciona correctamente, abre una nueva ventana de comandos (CMD) y escribe: 
        ```cmd
        ffmpeg -version
        ```

**Voces Instaladas**: Debes tener las voces instaladas de Aholab (ej. `AhoTTS_Ainara_eu`) instalando la aplicación [AhoSAPI](https://aholab.ehu.eus/aholab/es/ahosapi/). Es una Speech API (Microsoft) de Aholab. Si no las tienes, el script usará la voz por defecto de Windows (David o Zira).

### Uso

1.  Abre el archivo `generador_local.py`.
2.  Modifica la lista `bloques`. Asegúrate de poner el **nombre exacto** de la voz instalada en tu PC (puedes verlas ejecutando el archivo PowerShell `_get_pc_voices.ps1` si lo conservas).
3.  Ejecuta el script:
    ```bash
    python generador_local.py
    ```
4.  Los audios aparecerán en la carpeta `audios_locales`.

---

## 🚀 OPCIÓN B: Generador Online (No funciona en Euskera)

No recomendamos su uso, solo en caso de absoluta necesidad

Usa voces neuronales de internet.

1.  Abre el archivo `generador_moderno.py`.
2.  Ve a la sección `LISTA DE FRASES A GENERAR` (hacia el final del archivo).
3.  Añade o modifica los textos que quieras.
4.  Ejecuta el script:
    ```bash
    python generador_moderno.py
    ```
5.  Los audios aparecerán en la carpeta `audios_online`.

---