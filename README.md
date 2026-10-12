# Seminario de Integración

Repositorio académico para organizar los repasos, ejercicios, prácticas y proyectos de la asignatura **Seminario de Integración**. Durante la materia se reforzarán conocimientos de Python y se trabajará con herramientas para desarrollar servicios web y aplicaciones.

## Objetivo

Integrar conocimientos de programación y desarrollo de software mediante ejercicios y proyectos prácticos, utilizando herramientas actuales para construir, ejecutar y organizar aplicaciones.

## Semana del 12 al 18 de octubre de 2026

### Python Fundamentals

Repaso de los fundamentos necesarios para construir programas en Python:

- **Variables y tipos de datos:** almacenar y representar información con tipos como `int`, `float`, `str` y `bool`.
- **Operadores y expresiones:** realizar cálculos, comparaciones y operaciones lógicas.
- **Entrada y salida:** recibir datos con `input()` y presentar resultados con `print()`.
- **Condicionales y ciclos:** controlar decisiones con `if` y repetir instrucciones con `for` y `while`.
- **Funciones:** organizar código reutilizable con parámetros y valores de retorno.
- **Colecciones:** agrupar información usando listas, tuplas, conjuntos y diccionarios.

## Tecnologías y conceptos

- **Python:** lenguaje de programación de propósito general, conocido por su sintaxis legible. Se utilizará para repasar fundamentos y desarrollar la lógica de las aplicaciones.
- **uv:** herramienta para gestionar proyectos Python, dependencias y entornos virtuales. Puede crear un entorno con `uv venv` e instalar dependencias de un proyecto.
- **venv:** módulo de Python que permite crear entornos virtuales aislados. Así, cada proyecto puede mantener sus propias dependencias sin mezclarlas con las de otros proyectos.
- **FastAPI:** framework de Python para crear API web. Permite definir rutas, validar datos y generar documentación interactiva de los endpoints.
- **Node.js:** entorno de ejecución que permite ejecutar JavaScript fuera del navegador. Se utiliza, entre otros casos, para las herramientas de desarrollo del ecosistema web.
- **Angular:** framework de desarrollo web basado en TypeScript para crear aplicaciones de una sola página mediante componentes, servicios y herramientas de enrutamiento.

## Temas de trabajo

1. Repaso de fundamentos de Python: variables, tipos de datos, condicionales, ciclos, funciones y módulos.
2. Creación y administración de entornos virtuales con `venv` y `uv`.
3. Gestión de dependencias y organización de proyectos Python.
4. Desarrollo de API con FastAPI: rutas, métodos HTTP, validación y documentación.
5. Uso de Node.js y herramientas del ecosistema JavaScript.
6. Fundamentos de Angular: componentes, plantillas, servicios y comunicación con API.
7. Integración de los conocimientos en ejercicios y proyectos.

## Estructura sugerida

```text
.
├── python/
│   └── ejercicios/
├── fastapi/
│   └── proyecto_api/
├── angular/
│   └── aplicacion_web/
├── proyectos/
├── .gitignore
└── README.md
```

Cada carpeta de proyecto puede contener sus propios subproyectos. El archivo `.gitignore` se aplica también dentro de esas carpetas y evita incluir entornos virtuales, dependencias instaladas, archivos temporales y configuraciones locales.

## Herramientas

- Python y `venv`
- `uv`
- FastAPI
- Node.js y npm
- Angular CLI
- Git y GitHub

## Uso académico

Este repositorio se utilizará para mantener organizados los materiales y avances de la asignatura. Se recomienda guardar cada práctica en la carpeta correspondiente y no subir credenciales, archivos `.env` ni entornos virtuales.