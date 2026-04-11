import os
import re

ruta_base = '.' # Analiza la carpeta actual y subcarpetas

print("🚀 Iniciando el renombrado rápido e inteligente...")

# Diccionario para evitar que mapas de la misma sección se sobreescriban
contador_secciones = {}

for carpeta_actual, subcarpetas, archivos in os.walk(ruta_base):
    for archivo in archivos:
        if archivo.endswith('.pdf'):
            
            # Buscamos el patrón oculto en el nombre: L19 seguido de 4 números
            coincidencia = re.search(r'L19(\d{4})', archivo)
            
            if coincidencia:
                seccion = coincidencia.group(1)
                
                # Controlamos si hay más de un mapa para esta misma sección
                if seccion not in contador_secciones:
                    contador_secciones[seccion] = 0
                    sufijo = ""
                else:
                    contador_secciones[seccion] += 1
                    sufijo = f"_{contador_secciones[seccion]}"
                    
                nuevo_nombre = f"{seccion}{sufijo}.pdf"
                
                ruta_completa = os.path.join(carpeta_actual, archivo)
                nuevo_nombre_completo = os.path.join(carpeta_actual, nuevo_nombre)
                
                try:
                    os.rename(ruta_completa, nuevo_nombre_completo)
                    print(f"✅ {archivo} -> {nuevo_nombre}")
                except Exception as e:
                    pass
            else:
                # Los archivos que no tienen sección (ej. CEMDF15054...) son mapas generales del municipio
                print(f"ℹ️ Mapa general omitido (sin sección local): {archivo}")

print("🎉 ¡Proceso terminado! Todos los mapas están renombrados y a salvo.")