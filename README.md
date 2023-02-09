# EcoleDirectPy

EcoleDirectPy is a API Wrapper for [EcoleDircte](https://www.ecoledirecte.com/).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install EcoLeDirectePy.

```bash
pip install EcoleDirectePy
```

## Usage

```python
import EcoleDirectePy

# Login to EcoleDirecte with your username and password
EcoleDirectePy.login("username", "password")


# returns yours scedules
EcoleDirectePy.emploidutemps('date1,date2')

# returns yours homeworks
emploidutemps.cahierdetexte('date1,date2')

# returns yours marks
EcoleDirectePy.notes()

# returns yours absences
EcoleDirectePy.absences()

# returns yours messages
EcoleDirectePy.messages()
```



## License

[MIT](https://choosealicense.com/licenses/mit/)