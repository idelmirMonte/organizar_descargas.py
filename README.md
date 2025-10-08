Perfecto 👌 Aquí tienes un **README.md** completamente listo para subir a tu repositorio de GitHub, adaptado a tu caso (carpeta `D:\Descargas` y archivo `organizar_descargas.py`).
Puedes copiarlo tal cual o guardarlo directamente como `README.md` junto a tu script:

---

````markdown
# 🗂️ Organizador Automático de Descargas

Este script en Python organiza automáticamente los archivos que se descargan en tu carpeta **Descargas**, moviéndolos a subcarpetas según su tipo (PDF, imágenes, música, etc.).  
Por ejemplo, si descargas un archivo `.pdf`, se moverá automáticamente a `D:\Descargas\PDF`.

---

## 🚀 Características

- Organiza archivos por tipo: PDF, imágenes, música, vídeos, documentos, ZIP, etc.
- Crea las subcarpetas automáticamente si no existen.
- Puede ejecutarse manualmente o automáticamente cada vez que inicias tu computadora.
- Configurable y personalizable (puedes añadir tus propias extensiones o carpetas).

---

## ⚙️ Requisitos

- **Windows 10/11**
- **Python 3.8 o superior**  
  (descárgalo desde [python.org](https://www.python.org/downloads/) y marca la casilla **“Add Python to PATH”** durante la instalación)
- (Opcional) **PyInstaller** si deseas crear un `.exe` y no depender de Python.

---

## 📁 Configuración del Script

1. Abre el archivo `organizar_descargas.py`.
2. Verifica que la ruta de descargas esté configurada correctamente:
   ```python
   from pathlib import Path
   carpeta_descargas = Path("D:/Descargas")
   ```
````

3. Puedes personalizar el diccionario `destinos` dentro del código para agregar o quitar tipos de archivo según tus necesidades.

---

## ▶️ Ejecución manual

Desde la carpeta donde guardaste el script, abre **PowerShell** o **CMD** y ejecuta:

```powershell
python organizar_descargas.py
```

---

## 🧩 Crear un ejecutable (.exe)

Si prefieres que el programa funcione sin necesidad de abrir Python:

1. Instala PyInstaller:

   ```powershell
   python -m pip install pyinstaller
   ```

2. Abre una terminal en la carpeta donde está el script y ejecuta:

   ```powershell
   python -m PyInstaller --noconsole --onefile organizar_descargas.py
   ```

3. El archivo `.exe` se generará en la carpeta `dist`, dentro del proyecto:

   ```
   dist/organizar_descargas.exe
   ```

4. Puedes mover ese `.exe` a donde quieras, por ejemplo:

   ```
   D:\Scripts\organizador.exe
   ```

---

## 💡 Ejecutar el script al iniciar Windows

### 🔸 Opción 1 — Carpeta de inicio (más fácil)

1. Presiona **Win + R** y escribe:

   ```
   shell:startup
   ```

   Luego presiona **Enter**.

2. Copia el archivo `organizar_descargas.exe` (o un acceso directo a él) dentro de esa carpeta.

   > Así se ejecutará automáticamente cada vez que inicies sesión.

🕒 **Opcional:** si quieres retrasar su ejecución unos segundos (por ejemplo, 30 segundos), crea un archivo `.bat` con este contenido:

```bat
@echo off
timeout /t 30 /nobreak >nul
start "" "D:\Scripts\organizador.exe"
exit
```

Coloca ese `.bat` en la carpeta `shell:startup` en lugar del `.exe`.

---

### 🔸 Opción 2 — Programador de tareas (más avanzado)

1. Abre **Programador de tareas** (Task Scheduler).
2. Crea una nueva tarea:

   - Nombre: `OrganizadorDescargas`
   - Tipo de inicio: **Al iniciar sesión**
   - Acción: **Iniciar un programa**

     - Programa/script: `D:\Scripts\organizador.exe`

   - (Opcional) Configura un retraso de 30 segundos.

3. Guarda la tarea.
   El script se ejecutará automáticamente cada vez que enciendas el computador.

---

## 🧠 Personalización

Puedes editar el diccionario `destinos` para agregar nuevas categorías o extensiones.
Ejemplo:

```python
destinos = {
    "PDF": [".pdf"],
    "IMAGENES": [".jpg", ".png", ".jpeg", ".gif"],
    "MUSICA": [".mp3", ".wav", ".flac"],
    "VIDEOS": [".mp4", ".mkv", ".mov"],
    "DOCUMENTOS": [".docx", ".xlsx", ".txt"],
    "ZIP": [".zip", ".rar", ".7z"],
}
```

---

## 🧾 Registro (opcional)

Si quieres guardar un registro de los archivos movidos, puedes añadir al script:

```python
from datetime import datetime
log_path = carpeta_descargas / "organizador_log.txt"

def log(msg):
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()} - {msg}\n")
```

Y luego agregar dentro del bucle principal:

```python
log(f"Movido: {archivo} -> {destino}")
```

---

## 🧰 Solución de problemas

| Problema                      | Posible solución                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------------ |
| **No mueve los archivos**     | Verifica que la ruta `C:/Descargas` exista y esté correctamente escrita.                   |
| **El .exe no se ejecuta**     | Asegúrate de haber generado el archivo con PyInstaller correctamente.                      |
| **Ventana negra al ejecutar** | Usa `--noconsole` en PyInstaller o ejecuta con `pythonw.exe` para ocultarla.               |
| **No se ejecuta al inicio**   | Verifica que el `.exe` o `.bat` esté dentro de `shell:startup` o que la tarea esté activa. |

---

## 🪪 Licencia

Este proyecto está bajo la **licencia MIT**, lo que significa que puedes usarlo, modificarlo y distribuirlo libremente, siempre dando crédito al autor original.

---

## 💬 Contribuciones

¡Contribuciones son bienvenidas!
Puedes crear un _pull request_ o abrir un _issue_ si tienes ideas para mejorar el proyecto (por ejemplo, interfaz gráfica, categorías automáticas, integración con fechas, etc.).

---

Hecho con 💻 por [IdelmirMonte]

```


```
