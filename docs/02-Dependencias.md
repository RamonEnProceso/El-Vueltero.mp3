# Dependencias

Acá las dependencias que estoy empleando para el proyecto

**Para instalarlas, ejecutá el requeriments.txt en un entorno virtual Python, inferior o igual a la v3.11:**
```bash
pip install -r requirements.txt
```

---

## FoxDot

> Live Coding
> *Crear beats, melodías y secuencias en tiempo real*

Crear patrones rítmicos, melodías y secuencias en tiempo real.

Usos:
* Beats
* Melodías
* Arpegios
* Patrones
* Música generativa

---

## Pyo

> Síntesis y procesamiento de audio
> *Crear instrumentos, efectos y sonido en tiempo real*

Generar, modificar y procesar audio.

Incluye:
* Osciladores (seno, cuadrada, triangular y sierra)
* Filtros
* Reverb
* Delay
* Chorus
* Compresores
* Envolventes ADSR
* Samplers
* Mezcla de múltiples pistas

---

## SciPy y NumPy

> Procesamiento Digital de Señales (DSP)
> *Generar y manipular audio mediante matemáticas*

Trabajar con señales digitales y procesamiento de audio desde bajo nivel.

Permiten:
* Generar ondas matemáticamente
* Manipular muestras de audio
* Aplicar filtros
* Realizar transformadas de Fourier (FFT)
* Crear efectos personalizados
* Analizar señales

---

## Librosa

> Análisis musical
> *Extraer información de canciones y samples*

Análisis de audio y música.

Permite:
* Detectar BPM
* Detectar tono (Pitch)
* Detectar tempo
* Separar silencios
* Extraer características del audio
* Visualizar espectrogramas
* Cambiar velocidad y tono de un audio

---

## PyDub

> Edición de audio
> *Manipular archivos de audio de forma sencilla*

Editar y combinar archivos de audio mediante una API simple.

Permite:
* Cortar audio
* Unir varios audios
* Superponer sonidos
* Aplicar Fade In y Fade Out
* Normalizar volumen
* Exportar en WAV, MP3, OGG y FLAC

---

## SoundDevice

> Grabación y reproducción
> *Capturar y reproducir audio desde Python*

Interactuar con los dispositivos de audio del sistema en tiempo real.

Permite:
* Capturar audio del micrófono
* Reproducir audio
* Grabar samples propios
* Trabajar con audio en tiempo real
* Seleccionar dispositivos de entrada y salida

---

## SoundFile

> Lectura y escritura de audio
> *Guardar y cargar archivos de audio con alta calidad*

Leer y escribir archivos de audio de forma rápida y eficiente.

Permite:

* Leer archivos WAV, FLAC, OGG y otros formatos
* Guardar audio generado desde Python
* Trabajar directamente con arrays de NumPy
* Conservar audio sin pérdidas
* Manejar archivos de gran tamaño de forma eficiente
