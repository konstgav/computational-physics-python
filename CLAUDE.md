# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Teaching material for an elective course, "Introduction to Computational Physics with Python 3" (in Russian). The content lives in standalone Jupyter notebooks in the repo root, one per topic. Notebook prose, comments and plot labels are written in Russian; keep them in Russian when editing or adding notebooks. There is no package, build system, test suite or linter.

## Running

```bash
pip install -r requirements.txt   # pins numpy 1.16, scipy 1.2, matplotlib 3 (also used by Binder)
jupyter notebook                  # run from the repo root so relative paths resolve
jupyter nbconvert --to notebook --execute --inplace <Notebook>.ipynb   # re-run a notebook headlessly
```

The repo is also launched on mybinder.org straight from `master` (badge in README.md), so `requirements.txt` sets the environment students get. Changing the pins affects Binder.

## Structure and conventions

- **Notebooks are self-contained lessons.** The ordered syllabus is the table of contents in `README.md`, which links to each notebook on GitHub. When you add a lesson notebook, add it to that list. Some notebooks (e.g. `Oscillations.ipynb`, `Maxwell_distrubution.ipynb`, `b-V diagram.ipynb`, `Capillar-dynamics.ipynb`) aren't in the list yet.
- **Shared helper modules** at the root, imported by notebooks (`from gaussxw import gaussxw`, etc.):
  - `gaussxw.py`: Gauss–Legendre quadrature points and weights (`gaussxw`, `gaussxwab`), used in `Integration.ipynb`.
  - `banded.py`: banded-matrix Gaussian elimination solver, used in `Systems-of-Linear-Equations.ipynb`.

  Both come from Newman's *Computational Physics*, as do most of the `data/*.txt` exercise datasets.
- **Data and images** are loaded by relative path (`data/stars.txt`, `img/...`), so notebooks must run with the repo root as the working directory.
- **`school/`** (branch `school`): a separate 4-lesson mini-course for grades 10–11, run in local JupyterLab with its own `school/requirements.txt` (modern versions). Lesson notebooks are generated: edit `school/lesson-NN/build_notebooks.py` and rerun it, which writes both the student `.ipynb` and the `-solutions.ipynb`. Don't hand-edit the `.ipynb` files. Slide figures come from `make_figures.py`; slides are Marp markdown.
- **PDF export:** `jupyter_notebook_config.py` sets nbconvert to export PDF through the LaTeX template `mytemplate.tplx`, which adds T2A/babel-russian so Cyrillic text renders. Exporting with `jupyter nbconvert --to pdf` from the repo root picks these up. It needs a TeX installation with Russian support and the older nbconvert (<6) `.tplx` template format.
