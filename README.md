# PyQuakeML

Lightweight QuakeML data parsing for Python

# Installation

```bash
cd ~/src/   # or wherever you keep your source packages
git clone https://gitext.gfz-potsdam.de/nooshiri/pyquakeml.git
cd pyquakeml
sudo python setup.py install
```

# Usage

To load data given in QuakeML format use keyword argument `stream=...` or
`filename=...` in loader function:

```python
from pyquakeml import QuakeML

data = QuakeML.load_xml(filename='your_event.xml')
```
