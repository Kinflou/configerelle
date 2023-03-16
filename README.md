# Configerelle
 
Configerelle is a configuration system that simplifies
configuration flows by letting you access and link variables
without needing much code, besides the configuration itself


For example, having a configuration like this:
```yaml
# Person configuration (person.yml)

items:
  - spoon
  - fork

hold: '{cfg::items::#1}' # expression to refer to 'fork' in 'items'
```

and making the configuration file and load like this:
```python
from pathlib import Path
from configerelle.configuration.base import ConfigBase

class Person(ConfigBase):
    items: list[str]
    hold: str

person = Person.from_path(Path('person.yml'))
```

which then you can know what the person should hold,
based on the 'hold' field, like this:
```python
# by using the expression we defined in 'person.hold'
person.expr_of(str, person.hold)
>>> fork

# or can also do with direct expressions!
person.expr_of(str, '{cfg::items::#1}')
>>> fork

# also directly of course
person.items[0]
>>> fork
```

