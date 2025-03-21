# sh1106_i2c

`sh1106_i2c` es una biblioteca para MicroPython que permite controlar pantallas OLED basadas en el controlador SH1106 a través de la interfaz I2C. Esta implementación optimizada proporciona funciones esenciales para dibujar texto, imágenes y gráficos en la pantalla.

## Características
- **Soporte para I2C**: Facilita la comunicación con pantallas OLED basadas en SH1106.
- **Funciones de dibujo**: Permite mostrar texto, imágenes y formas básicas.
- **Compatibilidad con MicroPython**: Diseñado para funcionar en microcontroladores compatibles con MicroPython.
- **Bajo consumo de memoria**: Optimizado para entornos con recursos limitados.

## Requisitos
- Microcontrolador compatible con MicroPython (ESP8266, ESP32, Raspberry Pi Pico, etc.).
- Pantalla OLED con controlador SH1106 y comunicación I2C.
- Firmware de MicroPython instalado en el microcontrolador.

## Instalación
1. Sube el archivo `sh1106_i2c.py` a tu microcontrolador mediante `mpy-cross`, `ampy` o cualquier otro método de transferencia.
2. Importa la biblioteca en tu código:
   ```python
   from sh1106_i2c import SH1106_I2C
   ```

## Uso
### Inicializar la pantalla
```python
from machine import Pin, I2C
from sh1106_i2c import SH1106_I2C

# Configuración de I2C (ajusta los pines según tu microcontrolador)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Inicializa la pantalla OLED
oled = SH1106_I2C(128, 64, i2c)
```

### Mostrar texto
```python
oled.fill(0)  # Limpia la pantalla
oled.text("Hola, mundo!", 0, 0)
oled.show()
```

### Dibujar un rectángulo
```python
oled.rect(10, 10, 50, 30, 1)
oled.show()
```

## Contribución
Si deseas mejorar la biblioteca, puedes hacer un fork del repositorio y enviar un pull request con tus mejoras.

## Licencia
Este proyecto está bajo la licencia MIT.

---
Desarrollado por joelwast.

