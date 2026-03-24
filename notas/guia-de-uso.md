# Guía de uso — Labo 6

Convenciones y flujo de trabajo para mantener el repositorio ordenado durante la cursada.

---

## Estructura de una práctica

Cada práctica vive en su propia carpeta dentro de `practicas/`.  
Copiá la plantilla con:

```bash
cp -r templates/practica practicas/p02-nombre-de-la-practica
```

Estructura interna de cada práctica:

```
practicas/pNN-nombre/
├── README.md           # Objetivo, setup, observaciones clave
├── analisis.ipynb      # Notebook principal de análisis
├── datos/
│   ├── crudos/         # Datos originales sin modificar
│   └── procesados/     # Datos derivados, limpios
├── figuras/            # Gráficos generados por el notebook
└── informe/
    ├── informe.tex     # Informe principal
    └── referencias.bib
```

---

## Convenciones de nombres

- **Carpetas de práctica**: `pNN-descripcion` (ej. `p01-pendulo-simple`)
- **Notebooks**: siempre `analisis.ipynb` dentro de la carpeta de la práctica
- **Scripts en `scripts/`**: `nombre_descriptivo.py` (guiones bajos)
- **Datos crudos**: incluir fecha si es relevante → `medicion_2025-04-10.csv`
- **Figuras**: `fig_variable_vs_variable.pdf` (ej. `fig_posicion_vs_tiempo.pdf`)

---

## Commits recomendados

Mensajes cortos y descriptivos:

```
p01: datos crudos del experimento
p01: notebook de análisis completado
p01: figuras exportadas
p01: borrador del informe
p01: informe final
```

---

## Qué subir y qué no subir

**Subir:**
- Todo el código (`.py`, `.ipynb`)
- Datos crudos y procesados (si pesan menos de ~10 MB)
- Figuras finales (`.pdf`, `.png`)
- Fuentes LaTeX (`.tex`, `.bib`)
- PDFs de informes compilados (opcional pero útil)

**No subir:**
- Entorno virtual (`.venv/`)
- Archivos auxiliares de LaTeX (`.aux`, `.log`, `.synctex.gz`, etc.)
- Checkpoints de Jupyter (`.ipynb_checkpoints/`)
- Archivos del sistema (`.DS_Store`, `Thumbs.db`)
- Datos muy grandes (> 10 MB) → guardá el enlace o usá Git LFS

---

## Notas de LaTeX

- Compilar desde la carpeta del informe:
  ```bash
  cd practicas/p01-pendulo-simple/informe
  pdflatex informe.tex
  biber informe       # o bibtex si usás bibtex
  pdflatex informe.tex
  ```
- No es necesario commitear los archivos auxiliares; el `.gitignore` los excluye.

---

## Notas de Python / Jupyter

- Siempre trabajar con el entorno virtual activado.
- Limpiar las salidas del notebook antes de commitear (opcional pero recomendado):
  ```bash
  jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace analisis.ipynb
  ```
- Si usás funciones en varios notebooks, movelas a `scripts/utils.py` e importalas.
