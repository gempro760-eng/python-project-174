# Gendiff (Proyecto Hexlet)

[![Actions Status](../../workflows/hexlet-check/badge.svg)](../../actions)

## Descripción
Gendiff es una herramienta de línea de comandos y biblioteca de Python que compara dos archivos de configuración (JSON y YAML) y muestra las diferencias en un formato limpio y ordenado.

## Características
- Compara archivos de configuración en formato **JSON** y **YAML** (`.yaml`, `.yml`).
- Muestra las claves ordenadas alfabéticamente.
- Resalta claramente configuraciones agregadas (`+`), eliminadas (`-`) y sin cambios.
- Ofrece varios formatos de salida: **stylish** (por defecto), **plain** y **json**.

## Instalación

Clona el repositorio e instala las dependencias usando `uv`:

```bash
git clone [https://github.com/gempro760-eng/python-project-174.git](https://github.com/gempro760-eng/python-project-174.git)
cd python-project-174
uv sync