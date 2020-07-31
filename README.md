## pyins 

![](https://github.com/Zhang-Haipeng/pyins/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/Zhang-Haipeng/pyins/branch/main/graph/badge.svg)](https://codecov.io/gh/Zhang-Haipeng/pyins) ![Release](https://github.com/Zhang-Haipeng/pyins/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pyins/badge/?version=latest)](https://pyins_rz.readthedocs.io/en/latest/?badge=latest)

Python package that helps process pictures for Instagram posts.

### Installation:

```
pip install -i https://test.pypi.org/simple/ pyins
```

### Features
- TODO

### Dependencies

python = "^3.7"  
matplotlib = "^3.3.0"  
numpy = "^1.19.0"  

### Usage

```
from pyins import pyins
pyins.split_black_all()
# all pics ending with `.jpg`/`.JPG` will be black-split into two and saved into the `/output` folder. 

pyins.land_split("my_pic.jpg", color='w')
# `my_pic.jpg` will be white-split and saved to `/output` folder. 
```

### Documentation
The official documentation is hosted on Read the Docs: <https://pyins_rz.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
