import os
import shutil
from pathlib import Path

# === CONFIGURACIÓN ===
carpeta_descargas = Path("D:/Descargas")  # ← Tu ruta personalizada

# Carpetas destino (se crearán automáticamente si no existen)
destinos = {
    "PDF": [".pdf"],
    "IMAGENES": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "MUSICA": [".mp3", ".wav", ".flac", ".m4a"],
    "VIDEOS": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "DOCUMENTOS": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    "COMPRIMIDOS": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "EJECUTABLES": [".exe", ".msi"],
    "OTROS": []  # Archivos que no encajen en ninguna categoría
}


def organizar_descargas():
    for archivo in carpeta_descargas.iterdir():
        if archivo.is_file():
            extension = archivo.suffix.lower()
            movido = False
            for carpeta, extensiones in destinos.items():
                if extension in extensiones:
                    destino = carpeta_descargas / carpeta
                    destino.mkdir(exist_ok=True)
                    shutil.move(str(archivo), destino / archivo.name)
                    movido = True
                    break
            if not movido:
                destino = carpeta_descargas / "OTROS"
                destino.mkdir(exist_ok=True)
                shutil.move(str(archivo), destino / archivo.name)


if __name__ == "__main__":
    organizar_descargas()
