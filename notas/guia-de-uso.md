# Guía de uso — Labo 6

Convenciones y flujo de trabajo para mantener el repositorio ordenado.

---

## Convenciones de nombres

- **Scripts en `scripts/`**: `nombre_descriptivo.py` (guiones bajos)
- **Datos crudos**: incluir fecha si es relevante → `medicion_2025-04-10.csv`
- **Figuras**: `fig_variable_vs_variable.pdf` (ej. `fig_posicion_vs_tiempo.pdf`)
- Usá minúsculas y guiones (`-`) para carpetas; guiones bajos (`_`) para archivos Python.

---

## Flujo de trabajo

1. Volcar los datos crudos en `datos/crudos/`.
2. Analizar en `analisis.ipynb` y guardar datos procesados en `datos/procesados/`.
3. Exportar figuras finales a `figuras/`.
4. Redactar el informe en LaTeX dentro de `informes/`.
5. Hacer commit con mensajes descriptivos:
   ```
   git add datos/crudos/medicion_2025-04-10.csv
   git commit -m "agrego datos crudos de la medición"
   ```

---

## Qué subir y qué no subir

**Subir:**
- Todo el código (`.py`, `.ipynb`)
- Datos crudos y procesados (si pesan menos de ~10 MB)
- Figuras finales (`.pdf`, `.png`)
- Fuentes LaTeX (`.tex`, `.bib`)

**No subir:**
- Entorno virtual (`.venv/`)
- Archivos auxiliares de LaTeX (`.aux`, `.log`, `.synctex.gz`, etc.)
- Checkpoints de Jupyter (`.ipynb_checkpoints/`)
- Archivos del sistema (`.DS_Store`, `Thumbs.db`)
- Datos muy grandes (> 10 MB)

---

## Notas de LaTeX

Compilar desde la carpeta del informe:

```bash
cd informes
pdflatex informe.tex
biber informe
pdflatex informe.tex
```

---

## Notas de Python / Jupyter

- Trabajar siempre con el entorno virtual activado.
- Limpiar salidas antes de commitear (opcional):
  ```bash
  jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace analisis.ipynb
  ```
- Si usás funciones en varios notebooks, movelas a `scripts/utils.py` e importalas.
