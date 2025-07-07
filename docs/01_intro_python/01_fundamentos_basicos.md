# Fundamentos Básicos

## **1.1 Introducción a Python**

### **Historia**

- Creado por **Guido van Rossum** en 1991.
- Su filosofía se basa en la legibilidad del código (Zen de Python).

#### **Características clave**

- **Lenguaje interpretado**: No requiere compilación (se ejecuta línea por línea).
- **Multiplataforma**: Funciona en Windows, Linux, macOS.
- **Tipado dinámico**: No es necesario declarar el tipo de variable, pero por favor haganlo!
- **Orientado a objetos**: Soporta POO, pero también programación funcional.

#### **Usos comunes**

- **Desarrollo web**: Frameworks como Django y Flask.
- **Ciencia de datos**: Librerías como Pandas, NumPy.
- **Inteligencia artificial**: TensorFlow, PyTorch.
- **Automatización (scripting)**: Tareas repetitivas, manipulación de archivos.

## **1.2 Instalación y Configuración**

### **Descargar Python**

- Sitio oficial: [python.org](https://www.python.org/downloads/).
- Versión recomendada: **Python 3.12** (Julio de 2025)
- Una vez descargado es recomendado utilizar ambientes(env).

- (Alternativa)**Usar un contenedor de docker**

### **Entornos de desarrollo (IDE/Editores)**

- **VS Code**: Ligero, con extensiones para Python (IntelliSense, debugging).
- **PyCharm**: IDE profesional (versión Community gratuita).
- **Jupyter Notebook**: Ideal para análisis de datos (entorno interactivo).
- **Alternativas simples**: Sublime Text, IDLE (incluido con Python).

#### **Verificar instalación**
  ```bash
  python --version  # En Windows/Linux/macOS (o `python3` en algunos sistemas).
  ```

## **1.3 Sintaxis Básica**

### **Indentación**

- Python usa espacios/tabulaciones para definir bloques (no llaves `{}` como otros lenguajes).
- Ejemplo:
```python
if 5 > 2:
    print("Cinco es mayor que dos")  # 4 espacios o 1 tabulación.
```

### **Comentarios**

- Línea única: `# Esto es un comentario`.
- Multilínea:
```python
"""
Esto es un comentario
de varias líneas.
"""
```

### **Estructura de un programa**

- Un script de Python es un archivo con extensión `.py`.
- Se ejecuta línea por línea desde arriba hacia abajo.



## **1.4 Variables y Tipos de Datos**

### **Variables**

- No requieren declaración de tipo.
- Ejemplo:
```python linenums="1" title="Ejemplo sin tipos"
nombre = "Pepe"        # str
edad = 40              # int
altura = 1.76          # float
es_programador = True  # bool
```

### **Tipos de datos principales**

- `int`: Números enteros (`-3`, `0`, `42`).
- `float`: Números decimales (`3.14`, `-0.001`).
- `str`: Cadenas de texto (`"Hola"`, `'Python'`).
- `bool`: Valores booleanos (`True`, `False`).
- `None`: Valor nulo (similar a `null` en otros lenguajes).
- Ejemplo:
```python linenums="1" title="Ejemplo con tipos"
nombre: str = "Pepe"         # str
edad: int = 40               # int
altura: float = 1.76         # float
es_programador: bool = True  # bool
```

### **Operadores**
  - **Aritméticos**: `+`, `-`, `*`, `/`, `**` (potencia), `//` (división entera), `%` (módulo).
  - **Comparación**: `==`, `!=`, `>`, `<`, `>=`, `<=`.
  - **Lógicos**: `and`, `or`, `not`.

### **Ejemplos**

```python linenums="1"
suma = 3 + 2       # 5
potencia = 2 ** 3  # 8 (2 elevado a 3)
es_mayor = 10 > 5  # True
```

## **1.5 Conversión de Tipos (Type Casting)**

### **Funciones útiles**

- `int()`: Convierte a entero.
- `float()`: Convierte a decimal.
- `str()`: Convierte a cadena.
- `bool()`: Convierte a booleano.

### **Ejemplos**

```python linenums="1" title="Ejemplo de cast"
numero = int("10")      # Convierte el string "10" a entero.
texto = str(3.14)       # Convierte 3.14 a string "3.14".
decimal = float("5.2")  # Convierte "5.2" a float 5.2.
```

### **Ejemplo de Errores de casteo**

```python
int("Hola")  # Error: No se puede convertir texto no numérico.
```

