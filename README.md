# PyConfigurer

A GUI configuration library for python programs.

# Usage

```python
from PyConfigurer import Configurer, ConfigTemplate, Token, FieldType


default_config = {
    "user": "Arjix",
    "age": 18
}


config_template = ConfigTemplate([
    Token(FieldType.text_input, "user", "Enter your name:", default_config["user"]),
    Token(FieldType.int_input, "age", "Enter your age:", default_config["age"])
])
config = Configurer(config_template)
new_config = config.run()


print("Old config", default_config)
print("New config", new_config)
```
