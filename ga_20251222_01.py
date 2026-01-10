import asyncio
import edge_tts
import os


class GeneradorVocesNiña:
    def __init__(self):
        self.voces = {
            "1": {
                "nombre": "Elvira (España)",
                "voz": "es-ES-ElviraNeural",
                "pitch": "+30Hz",
                "rate": "+15%",
            },
            "2": {
                "nombre": "Elvira (España)",
                "voz": "es-ES-ElviraNeural",
                "pitch": "+50Hz",
                "rate": "+10%",
            },
            "3": {
                "nombre": "Elvira (España)",
                "voz": "es-ES-ElviraNeural",
                "pitch": "+35Hz",
                "rate": "+10%",
            },
            "4": {
                "nombre": "Elvira (España)",
                "voz": "es-ES-ElviraNeural",
                "pitch": "+35Hz",
                "rate": "+30%",
            },
            "5": {
                "nombre": "Ainhoa Neural",
                "voz": "eu-ES-AinhoaNeural",
                "pitch": "+0Hz",
                "rate": "+0%",
            },
            "6": {
                "nombre": "Ainhoa Neural",
                "voz": "eu-ES-AinhoaNeural",
                "pitch": "+35Hz",
                "rate": "+5%",
            },
            "7": {
                "nombre": "Elvira (España)",
                "voz": "es-ES-ElviraNeural",
                "pitch": "+0Hz",
                "rate": "+0%",
            },
            "8": {
                "nombre": "Ainhoa Neural",
                "voz": "eu-ES-AinhoaNeural",
                "pitch": "+60Hz",
                "rate": "+10%",
            },
            "9": {
                "nombre": "Ainhoa Neural",
                "voz": "eu-ES-AinhoaNeural",
                "pitch": "+50Hz",
                "rate": "+5%",
            },
        }

    async def generar_voz(self, texto, numero_archivo, titulo_archivo, numero_voz):
        # Obtener la configuración de la voz seleccionada
        config = self.voces[str(numero_voz)]

        # Crear nombre de carpeta
        nombre_carpeta = "ga_20251222_01"

        # Crear la carpeta si no existe
        if not os.path.exists(nombre_carpeta):
            os.makedirs(nombre_carpeta)

        # Crear nombre de archivo
        nombre_archivo = f"{titulo_archivo}.mp3"

        # Limpiar caracteres no válidos para nombres de archivo
        nombre_archivo = "".join(c for c in nombre_archivo if c not in '<>:"/\\|?*')

        communicate = edge_tts.Communicate(
            texto, config["voz"], pitch=config["pitch"], rate=config["rate"]
        )

        await communicate.save(os.path.join(nombre_carpeta, nombre_archivo))
        print(
            f"✅ '{titulo_archivo}' guardado como: {nombre_archivo} (Voz: {config['nombre']})"
        )
        return nombre_archivo


async def main():
    generador = GeneradorVocesNiña()

    # Lista de textos con sus títulos y voz seleccionada
    textos = [
        # {
        #     "titulo": "INVITACION_EU",
        #     "voz": 6,
        #     "contenido": "... Kaixo! Saaki naiz. Agian ikusi nauzu, baina aurrez aurre ezagutu nahi zaitut. Horregatik, bi mila eta hogeita bosteko abenduaren hogeita hirura, arratsaldeko hiruretan, Isabel Orberen egoitzara etortzera gonbidatu nahi zaitut. Zu ikusteko gogo handia dut!",
        # },
        # {
        #     "titulo": "INVITACION_ES",
        #     "voz": 2,
        #     "contenido": "... ¡Hola!. Soy Saaki. Igual ya me has visto por ahí, pero quiero conocerte en persona. Por eso, me gustaría invitarte a venir a nuestra sede de Isabel Orbe, el próximo veintitres de diciembre de dosmil veinticinco, a las tres de la tarde. ¡Tengo muchas ganas de verte!.",
        # },
        # {
        #     "titulo": "CHISTE_EBRO_PREG_ES",
        #     "voz": 2,
        #     "contenido": "¿Cuál es el río más moderno de España?",
        # },
        {
            "titulo": "CHISTE_EBRO_RESP_ES",
            "voz": 2,
            "contenido": "El río, E, Bro.",
        },
    ]
    # textos = [
    #     {
    #         "titulo": "01_Intro_EU",
    #         "voz": 6,
    #         "contenido": "... Kaixo!. SAAKI naiz. Gaur da jendearen aurrean aurkezten naizen lehen eguna, eta urduritasun pixka bat daukat, baina, aldi berean, oso pozik nago zuek hemen ikusteagatik. Ikusten duzuenez, humanoide pediatriko bat naiz. Bioaraba Osasun Ikerketa Institutura etorri naiz, ikerketa- eta berrikuntza-proiektuetan laguntzera, Fundación Vital Fundazioaren finantzaketari esker. Nire lehen helburua Arabako ESIko Txagorritxu ospitaleko Pediatria arloan dauden haurren egonaldia hobetzea da. Ospitale hori Osakidetza-Euskal Osasun Zerbitzuaren sarean dago. Hasteko gogo handia dut!!.",
    #     },
    #     {
    #         "titulo": "01_Intro_ES",
    #         "voz": 2,
    #         "contenido": "... ¡Hola!. Soy Saaki. Hoy es el primer día que me presento delante de la gente y tengo algunos nervios, pero a la vez, estoy muy alegre por veros aquí. Como veis, soy un humanoide pediátrico. He venido al Instituto de Investigación Sanitaria Bioaraba para ayudar en proyectos de investigación e innovación, gracias a la financiación de la Fundación Vital Fundazioa. Mi primer objetivo aquí es mejorar la estancia de los niños y las niñas ingresados en el área de Pediatría, del hospital Ua Txagorritxu de la Osi Araba, integrado en la red de Osakidetza-Servicio Vasco de Salud. ¡¡Tengo muchas ganas de empezar!!.",
    #     },
    #     {
    #         "titulo": "02_NINOS_EU",
    #         "voz": 6,
    #         "contenido": "... Kaixo! Gelan ume batzuk ikusi ditudala iruditu zait. Mesedez, igo zaitezkete nirekin?",
    #     },
    #     {
    #         "titulo": "02_NINOS_ES",
    #         "voz": 2,
    #         "contenido": "... ¡Hola!. Me ha parecido ver unos niños en la sala. Por favor, ¿podeis subir aquí conmigo?.",
    #     },
    #     {
    #         "titulo": "03_PREG_EU",
    #         "voz": 6,
    #         "contenido": "... Bi galdera egin nahi dizkizuet. Nola duzue izena?... Kirolik egiten al duzue? ",
    #     },
    #     {
    #         "titulo": "03_PREG_ES",
    #         "voz": 2,
    #         "contenido": "... Quiero haceros dos preguntas. ¿Cómo os llamáis? ...¿Practicáis algún deporte?",
    #     },
    #     {
    #         "titulo": "04_CELEB_EU",
    #         "voz": 6,
    #         "contenido": "... Oso ondo. Kirolari erraldoiak zarete!. Ongi baderitzozue, ospakizun bat erakutsiko dizuet gol bat sartzen duzuenerako edo azken segunduan hiruko bat sartzen duzuenerako. Gustatuko zaizue. Errepikatu nirekin nahi baduzue. Eman segundo bat nire oroimenean bilatzen dudana.",
    #     },
    #     {
    #         "titulo": "04_CELEB_ES",
    #         "voz": 2,
    #         "contenido": "... Muy bien. ¡Menudos deportistas sois!. Si os parece bien, os voy a enseñar una celebración para cuando metais un gol o para cuando encesteis un triple en el ultimo segunto. Seguro que os gusta. Repetidla conmigo si quereis. Dadme un segundo que la busco en mi memoria.",
    #     },
    #     {
    #         "titulo": "05_BAILE_EU",
    #         "voz": 6,
    #         "contenido": "... Eskerrik asko, Jon eta Ariane. Gaur egun berezia da eta denekin konpartitu nahi nuke dantza. Gustatuko litzaidake eszenatokian zaudeten guztiok nirekin dantzatzera animatzea.",
    #     },
    #     {
    #         "titulo": "05_BAILE_ES",
    #         "voz": 2,
    #         "contenido": "... Muchas gracias, Jon y Ariane. Hoy es un día especial y me gustaría compartir un baile con todos. Me gustaría que todos los que estais en el escenario os animeis a bailar conmigo.",
    #     },
    #     {
    #         "titulo": "07_MANO_EU",  # Interacción con consejero y directora de F.Vital
    #         "voz": 6,
    #         "contenido": "... Beno. Juanek esan dit ekitaldi honen amaierara hurbiltzen ari garela. Osasun sailburu jauna eta Vital Fundazioko zuzendari andrea, bihotzez eskertu nahi dizuet gaur hemen egotea eta jasotako babesa. Horretarako, uzten badidazue, bostekoa eman nahi dizuet, hain atseginak bazarete.",
    #     },
    #     {
    #         "titulo": "07_MANO_ES",  # Interacción con consejero y directora de F.Vital
    #         "voz": 2,
    #         "contenido": "... Bueno. Me dice Juan que nos acercamos al final de este acto. Señor Consejero de Salud y señora directora de Fundación Vital, quiero agradecerles de corazón su presencia hoy aquí y el apoyo recibido. Para ello, si me permiten, me gustaría estrecharles la mano si son tan amables de acercase a mí.",
    #     },
    #     {
    #         "titulo": "08_GRACIAS_EU",  # Interacción con consejero y directora de F.Vital
    #         "voz": 6,
    #         "contenido": ".Eskerrik asko guztioi!.",
    #     },
    #     {
    #         "titulo": "08_GRACIAS_ES",  # Interacción con consejero y directora de F.Vital
    #         "voz": 2,
    #         "contenido": ".¡Muchas gracias a todas y a todos!.",
    #     },
    # ]

    # Generar archivos para cada texto
    for i, texto_info in enumerate(textos, 1):
        await generador.generar_voz(
            texto=texto_info["contenido"],
            numero_archivo=i,
            titulo_archivo=texto_info["titulo"],
            numero_voz=texto_info["voz"],
        )

    print(f"\n🎉 Se generaron {len(textos)} archivos de audio correctamente!")


if __name__ == "__main__":
    asyncio.run(main())
