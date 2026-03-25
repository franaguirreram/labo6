# Labo 6 — Laboratorio de Física Experimental

Repositorio de trabajo para la materia **Laboratorio 6** de la carrera de Física.  
Contiene el análisis, datos, figuras e informe del proyecto experimental.

---

## Estructura

```
labo6/
├── datos/
│   ├── crudos/         # Datos originales del instrumento (nunca se modifican)
│   └── procesados/     # Datos limpios o derivados
├── figuras/            # Gráficos finales exportados (PDF, PNG)
├── informes/           # Fuentes LaTeX e informe compilado
├── scripts/            # Scripts Python de análisis
│   └── utils.py
├── notas/              # Apuntes y guía de uso
│   └── guia-de-uso.md
├── analisis.ipynb      # Notebook principal
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Inicio rápido

```bash
git clone https://github.com/franaguirreram/labo6.git
cd labo6
python -m venv .venv
source .venv/bin/activate    # Linux / macOS
pip install -r requirements.txt
jupyter notebook
```

---

## Qué subir y qué no subir

| ✅ Subir | ❌ No subir |
|---|---|
| Código Python / notebooks | Entorno virtual (`.venv/`) |
| Datos crudos (< 10 MB) | Archivos compilados de LaTeX (`.aux`, `.log`, etc.) |
| Figuras finales (PDF/PNG) | Checkpoints de Jupyter |
| Fuentes LaTeX (`.tex`, `.bib`) | Archivos del sistema (`.DS_Store`, `Thumbs.db`) |

> Ver `.gitignore` para la lista completa de exclusiones.

---

## Dependencias

Listadas en [`requirements.txt`](requirements.txt).  
Para LaTeX se recomienda **TeX Live** (Linux/macOS) o **MiKTeX** (Windows).

---

## Licencia

Repositorio de uso académico personal. Sin licencia de distribución.
