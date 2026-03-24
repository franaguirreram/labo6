# Labo 6 — Laboratorio de Física Experimental

> Repositorio de trabajo para la materia **Laboratorio 6** de la carrera de Física.  
> Contiene código de análisis, datos, figuras, informes y notas de cada práctica experimental.

---

## Estructura del repositorio

```
labo6/
├── practicas/              # Una subcarpeta por práctica (ver plantilla en templates/)
│   ├── p01-nombre/
│   ├── p02-nombre/
│   └── ...
├── datos/
│   ├── crudos/             # Datos tal como salen del instrumento (nunca se modifican)
│   └── procesados/         # Datos limpios o derivados, listos para graficar/analizar
├── figuras/                # Gráficos finales exportados (PNG, PDF, SVG)
├── informes/               # PDFs compilados y/o fuentes LaTeX de los informes finales
├── scripts/                # Scripts Python reutilizables entre prácticas
│   └── utils.py
├── notas/                  # Apuntes, bibliografía, guía de uso
│   └── guia-de-uso.md
├── templates/              # Plantillas para nuevas prácticas
│   └── practica/
├── .gitignore
├── requirements.txt
└── README.md               # Este archivo
```

---

## Inicio rápido

```bash
# 1. Clonar el repositorio
git clone https://github.com/franaguirreram/labo6.git
cd labo6

# 2. Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# .venv\Scripts\activate         # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Abrir Jupyter
jupyter notebook
```

---

## Convenciones de nombres

| Tipo de archivo | Formato | Ejemplo |
|---|---|---|
| Carpeta de práctica | `pNN-descripcion-corta` | `p01-pendulo-simple` |
| Notebook de análisis | `analisis.ipynb` | — |
| Script de procesamiento | `procesar_datos.py` | — |
| Datos crudos | `datos_crudos_YYYY-MM-DD.csv` | `datos_crudos_2025-04-10.csv` |
| Datos procesados | `datos_procesados.csv` | — |
| Figura exportada | `fig_descripcion.pdf` | `fig_fuerza_vs_tiempo.pdf` |
| Informe LaTeX | `informe.tex` (dentro de la carpeta de la práctica) | — |

- Usá minúsculas y guiones (`-`) para nombres de carpetas.  
- Usá guiones bajos (`_`) para nombres de archivos Python.  
- Evitá espacios, tildes y caracteres especiales en rutas.

---

## Flujo de trabajo recomendado

1. **Crear carpeta de práctica** copiando `templates/practica/` → `practicas/pNN-nombre/`
2. **Volcar los datos crudos** en `practicas/pNN-nombre/datos/crudos/` (o en `datos/crudos/` si son compartidos).
3. **Análisis en el notebook** `analisis.ipynb` dentro de la carpeta de la práctica.
4. **Exportar figuras finales** a `figuras/` o a `practicas/pNN-nombre/figuras/`.
5. **Redactar el informe** en LaTeX dentro de `practicas/pNN-nombre/informe/`.
6. **Hacer commit** con un mensaje descriptivo:  
   ```
   git add practicas/p01-pendulo-simple/
   git commit -m "p01: agrego análisis y primeras figuras"
   ```

---

## Qué subir y qué no subir

| ✅ Subir | ❌ No subir |
|---|---|
| Código Python / notebooks | Entorno virtual (`.venv/`) |
| Datos crudos (si son pequeños, < 10 MB) | Archivos compilados de LaTeX (`.aux`, `.log`, etc.) |
| Figuras finales (PDF/PNG) | Archivos de checkpoints de Jupyter |
| Fuentes LaTeX (`.tex`, `.bib`) | Archivos temporales del sistema (`.DS_Store`, `Thumbs.db`) |
| Informes compilados (`.pdf`) opcionales | Datos muy grandes → usar Git LFS o enlace externo |

> Ver `.gitignore` para la lista completa de exclusiones.

---

## Dependencias

Las dependencias de Python están listadas en [`requirements.txt`](requirements.txt).  
Para LaTeX se recomienda **TeX Live** (Linux/macOS) o **MiKTeX** (Windows), con los paquetes `siunitx`, `booktabs`, `pgfplots` y `biblatex`.

---

## Licencia

Repositorio de uso académico personal. Sin licencia de distribución.
