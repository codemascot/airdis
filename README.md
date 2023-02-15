# AirDis
This airdis CLI calculates the great circle distance among the a sets of places which comes from a CSV file.


* Free software: MIT license
* Documentation: https://airdis.readthedocs.io.

## Installation & Run

1. First clone this repo in your machine
```
$ git clone git@github.com:codemascot/airdis.git <PROJECT_PATH>
```
2. Change directory (`cd`) to `<PROJECT_PATH>`
```
$ cd <PROJECT_PATH>
```
3. Then install it with below `pip` command
```
$ pip install -e .
```
4. And run it with `airdis` in your Terminal
```
$ airdis -n 5 -p "csv/path/places.csv"
```
Here both `-n` and `-p` arguments are optional.

## Example

```
airdis on  main via 🐍 v3.10.9
❯ airdis -n 5
Name                Latitude            Longitude

Vardø               Longyearbyen        982.1829382784964  km
Vardø               Oslo                1487.6187821688432 km
Oslo                Longyearbyen        2043.6189438484282 km
Anchorage           Longyearbyen        4479.3540555961035 km
Vardø               Anchorage           5382.894281380392  km
Oslo                Anchorage           6443.9413268596745 km
Vardø               Jakarta             10132.856896888705 km
Jakarta             Longyearbyen        10711.167389473869 km
Oslo                Jakarta             10945.026837151634 km
Anchorage           Jakarta             11320.469203385404 km

Average distance: 6392.91 km. Closest pair: Oslo - Anchorage 6443.94 km
```

## Credits

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
