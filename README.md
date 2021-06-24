# Detection of Covid 19 on chest radiographs based on Computer Vision

[![No Maintenance](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![build passing](https://img.shields.io/static/v1?label=build&message=passing&color=green)](https://github.com/nuuday/covid19radiocv)

Data is found at [kaggle](https://www.kaggle.com/c/siim-covid19-detection/overview)

### Prerequisites

Dependencies are installed with poetry, which is installed using

``` bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Most likely you would also like your virtual environment to reside in the project folder, do once as

``` bash
poetry config virtualenvs.in-project true
```
### Installing

Link to your version of python using 

``` bash
poetry env use <python-version>
```

A python version could be installed using

``` bash
pyenv install 3.8.8
```
Currently there are some issues on some platforms with using pyenv to install python. If you experience problems with sqlite3 on amazon linux (redhat distribution) try 

``` bash
yum list | grep sqlite
sudo yum install sqlite-devel.x86_64
pyenv install 3.8.8
```

And you can install the dependencies using 
``` bash
poetry install (or update)
```

### Coding style tests

``` bash
poetry run black src
```
  
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/hojland/project/tags). 

## Authors

* **Martin Højland** - *Initial work* - [hojland](https://github.com/Hojland)

See also the list of [contributors](https://github.com/hojland/project/contributors) who participated in this project.

## License
[MIT](https://choosealicense.com/licenses/mit/)