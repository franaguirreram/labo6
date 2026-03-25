# Labo 6 — Implementación de una platina piezoeléctrica para corrección activa de deriva en MINFLUX

Repositorio de trabajo para la materia **Laboratorio 6** de la carrera de Física. Contiene el análisis, datos, figuras e informe del proyecto experimental.

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

## Licencia

Repositorio de uso académico personal. Sin licencia de distribución.
