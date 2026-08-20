# Gendiff

[![Actions Status](https://github.com/gempro760-eng/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/gempro760-eng/python-project-174/actions)
[![Python CI](https://github.com/gempro760-eng/python-project-174/actions/workflows/ci.yml/badge.svg)](https://github.com/gempro760-eng/python-project-174/actions/workflows/ci.yml)

Gendiff compara dos archivos de configuración JSON o YAML como estructuras de
datos y muestra las propiedades agregadas, eliminadas, modificadas y sin cambios.

## Requisitos

- Python 3.14 o posterior.
- [uv](https://docs.astral.sh/uv/) para instalar dependencias y ejecutar el proyecto.

## Instalación

```bash
git clone https://github.com/gempro760-eng/python-project-174.git
cd python-project-174
uv sync
```

## Uso desde la terminal

La ayuda muestra todos los argumentos disponibles:

```bash
uv run gendiff --help
```

La forma predeterminada es `stylish`:

```bash
uv run gendiff file1.json file2.json
uv run gendiff file1.yml file2.yml
```

También se puede seleccionar explícitamente el formato con `-f` o `--format`:

```bash
uv run gendiff --format stylish file1.json file2.json
uv run gendiff -f plain file1.json file2.json
uv run gendiff --format json file1.json file2.json
```

La CLI recibe exactamente dos archivos: primero el archivo original y después
el archivo nuevo. Se admiten las extensiones `.json`, `.yml` y `.yaml`.

La herramienta también puede ejecutarse como módulo:

```bash
uv run python -m gendiff.scripts.gendiff --help
```

## Uso como biblioteca

```python
from gendiff import generate_diff

result = generate_diff("file1.json", "file2.json")
plain_result = generate_diff("file1.json", "file2.json", "plain")
json_result = generate_diff("file1.json", "file2.json", "json")
print(result)
```

## Desarrollo

Ejecutar las pruebas:

```bash
uv run pytest
```

Medir la cobertura:

```bash
uv run pytest --cov=gendiff --cov-report=term-missing
```

Ejecutar el linter configurado:

```bash
uv run ruff check .
```

El workflow `Python CI` ejecuta automáticamente la instalación bloqueada de
dependencias, las pruebas con cobertura mínima del 90% y Ruff en cada push y
pull request.

## Arquitectura

- `gendiff/parser.py` carga JSON y YAML.
- `gendiff/diff_builder.py` construye el árbol de diferencias recursivo.
- `gendiff/generate_diff.py` coordina la carga, comparación y presentación.
- `gendiff/formatters/` contiene los formatos `stylish`, `plain` y `json`.
- `gendiff/scripts/gendiff.py` define el punto de entrada de la CLI.
- `tests/` contiene las pruebas y sus fixtures.

## Demostraciones

### Stylish

[![asciicast](https://asciinema.org/a/ZQVCKWaH7FB6Q4Ez.png)](https://asciinema.org/a/ZQVCKWaH7FB6Q4Ez)

### Plain

[![asciicast](https://asciinema.org/a/tMCF3pC3mmU9Gujf.png)](https://asciinema.org/a/tMCF3pC3mmU9Gujf)

### JSON

Esta grabación utiliza los fixtures anidados y muestra la estructura completa
del árbol JSON, incluyendo `children`, `old_value` y `new_value`:

[![asciicast](https://asciinema.org/a/Gd50MP7AD4Jd4xzM.png)](https://asciinema.org/a/Gd50MP7AD4Jd4xzM)

Esta segunda grabación utiliza los archivos JSON simples de la raíz. Su salida
es más corta y permite leer con mayor facilidad los estados `added`, `removed`
y `changed`:

[![asciicast](https://asciinema.org/a/GKfV1SBxzR2OUjDn.png)](https://asciinema.org/a/GKfV1SBxzR2OUjDn)

### YAML

Esta grabación muestra la comparación de dos archivos YAML usando el formato
`stylish` predeterminado:

[![asciicast](https://asciinema.org/a/MrfEa4UCQN72EKsx.png)](https://asciinema.org/a/MrfEa4UCQN72EKsx)