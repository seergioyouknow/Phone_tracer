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
            print("[!] invalid Number. Make sure to enter the international prefix (+34, +1, etc.)")
            return

        
        pasos = [
            "[!] [!] Analyzing international prefix...",
            "[!] Identifying country and region...",
            "[!] Looking for a phone operator...",
            "[!] Checking time zone...",
            "[!] Generating report..."
        ]
        for paso in pasos:
            print("[...] " + paso)
            time.sleep(random.uniform(0.8, 1.5))

        # Información detallada
        ubicacion = geocoder.description_for_number(p, "es")
        compania = carrier.name_for_number(p, "es")
        zonas = timezone.time_zones_for_number(p)
        tipo = ph.number_type(p)

        print("\n[+] --- Trace Results ---")
        print(f"[+] Country / Region : {ubicacion if ubicacion else 'No disponible'}")
        print(f"[+] Company: {compania if compania else 'No disponible'}")
        print(f"[+]  Time Zone: {', '.join(zonas) if zonas else 'No disponible'}")
        print(f"[+] Number type: {tipo}")  # 1 = fijo, 2 = móvil, etc.
        print("[+] Trace complete... ✅")

    except Exception as e:
        print(f"[!] Error: {e}")


# Ejecución
number = input("Enter full number, example: +34 123456789 -> ")
start_trace(number)

