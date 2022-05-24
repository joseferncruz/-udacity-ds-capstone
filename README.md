5CA - Advanced Analytics Case Study
==============================
2022 - [Jose Oliveira da Cruz](https://www.linkedin.com/in/josecruz-phd/), candidate for the data analytics role.

This repository contains the materials (presentation + executable Jupyter notebooks) for the case study interview step at 5CA.



## Repository Contents




    ├── README.md          
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- Support documentation
    │
    ├── notebooks          <- Jupyter notebooks.
    ├── reports            <- PowerPoint Presentation
    │   └── figures        <- Generated graphics and figures
    │
    └── environment.yml    <- conda environment will required python packages



## Installation & Requirements

1. Install a python environment with jupyter notebooks (e.g., [anaconda distribution](https://www.anaconda.com/products/individual)).

2. Create an environment with the required packages by running on the anaconda shell:
```
conda env create -f environment.yml --name myenv
conda activate myenv
```

3. Run individual notebooks in the following order:

  1. `notebooks/nb01_data-exploration.ipynb`
  2. `notebooks/nb02_modeling-part1.ipynb`
  3. `notebooks/nb03_modeling-part2.ipynb`
