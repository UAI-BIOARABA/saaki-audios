# Generador de Voces para Saaki - Unitree G1

Este repositorio contiene varios scripts que nos permitirán crear audios compatibles con el robot humanoide Unitree G1.

## 🛠️ Requisitos Previos

1.  **Python Instalado**: Asegúrate de tener Python 3.10 o superior instalado.
2.  **Librerías necesarias**:
    Abre una terminal (CMD o PowerShell) y ejecuta:
    ```bash
    pip install pywin32
    ```
3. **Sistema operativo Windows**

---

## 🚀 Generador Local

Usa las voces instaladas en tu PC y las modifica para ajustarlas al tono y velocidad deseados.

### Requisitos Extra

**Voces Instaladas**: Debes tener voces de Text-To-Speech instaladas en tu ordeador. 

- Hay servicios que ofrecen voces para uso persnoal o uso libre. Aségurate de conocer la licencia de uso de la voz que quieras utilizar dependiendo de tus objetivos. 
- Puedes comprobar las voces instaladas en tu sistema mediante el script [listar_voces_instaladas.py](listar_voces_instaladas.py), el script usará la voz por defecto de Windows (David o Zira) si no encuentra la especificada.

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

### Uso

1.  Abre el archivo `generador.py`.
2.  Modifica la lista `bloques`. Asegúrate de poner el **nombre interno** de la voz instalada en tu PC ([listar_voces_instaladas.py](listar_voces_instaladas.py)).
3.  Ejecuta el script:
    ```bash
    python generador.py
    ```
4.  Los audios aparecerán en la carpeta `audios`.

---

## 🧑‍💻 Autores

- **Project Manager:** [Juan Fernández](https://github.com/jfbioaraba)
- **Lead Developer:** [Andoni González](https://github.com/andoni92)


---
## Disclaimer

Este software y los materiales asociados se proporcionan “tal cual”, sin garantías de ningún tipo, ni expresas ni implícitas, incluyendo —pero no limitándose a— garantías de comercialización, idoneidad para un propósito particular o ausencia de errores.

Los/as autores/as y Bioaraba – Instituto de Investigación Sanitaria no asumen responsabilidad alguna por el uso, la redistribución o la modificación de este repositorio ni por los posibles daños directos o indirectos derivados de su utilización.

Este proyecto tiene fines exclusivos de investigación y/o docencia.

No está destinado a su uso clínico, diagnóstico, terapéutico ni asistencial,
ni sustituye herramientas certificadas ni la evaluación profesional en entornos sanitarios.
