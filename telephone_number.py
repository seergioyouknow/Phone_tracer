import phonenumbers as ph
from phonenumbers import geocoder, carrier, timezone
import time, random

def start_trace(number):
    numero = number.strip()
    print(f"[+] Phone Tracer By Sergio González")
    print(f"[+] Number: {numero}")
    print(f"[+] Initializing trace...\n")

    try:
        p = ph.parse(numero, None)

        if not ph.is_valid_number(p):
            print("[!] Número no válido. Asegúrate de incluir el prefijo internacional (+34, +1, etc.)")
            return

        # Simulación de "traceo paso a paso"
        pasos = [
            "Analizando prefijo internacional...",
            "Identificando país y región...",
            "Buscando operador telefónico...",
            "Consultando zona horaria...",
            "Generando informe..."
        ]
        for paso in pasos:
            print("[...] " + paso)
            time.sleep(random.uniform(0.8, 1.5))

        # Información detallada
        ubicacion = geocoder.description_for_number(p, "es")
        compania = carrier.name_for_number(p, "es")
        zonas = timezone.time_zones_for_number(p)
        tipo = ph.number_type(p)

        print("\n[+] --- Resultados del Traceo ---")
        print(f"[+] País / Región : {ubicacion if ubicacion else 'No disponible'}")
        print(f"[+] Operador      : {compania if compania else 'No disponible'}")
        print(f"[+] Zona horaria  : {', '.join(zonas) if zonas else 'No disponible'}")
        print(f"[+] Tipo de número: {tipo}")  # 1 = fijo, 2 = móvil, etc.
        print("[+] Trace complete... ✅")

    except Exception as e:
        print(f"[!] Error: {e}")


# Ejecución
number = input("Introduce el número completo -> ")  # Ejemplo: +34 612345678
start_trace(number)
