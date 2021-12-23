from typing import Any, Dict, List, NamedTuple
from enum import Enum, auto
import PySimpleGUI as sg


class FieldType(Enum):
    dropdown = auto()
    text_input = auto()
    int_input = auto()
    float_input = auto()
    path_input = auto()
    filepath_input = auto()


class Token(NamedTuple):
    field_type: FieldType
    key: str
    name: str
    default_value: Any = None
    options: list = []


class ConfigTemplate(NamedTuple):
    tokens: List[Token]


class Configurer:
    def __init__(self, template: ConfigTemplate):
        self.template = template

        self.layout = []
        for token in config_template.tokens:
            row = []
            if token.field_type in (FieldType.text_input, FieldType.int_input):
                row.append(sg.Text(token.name))
                row.append(sg.InputText(key=token.key,
                           default_text=token.default_value))
            elif token.field_type is FieldType.dropdown:
                row.append(sg.Text(token.name))
                row.append(sg.Listbox(
                    token.options,
                    key=token.key,
                    default_values=token.default_value,
                    size=[len(token.options)*10, len(token.options)*2],
                    expand_x=True
                ))
            elif token.field_type is FieldType.filepath_input:
                self.layout.append([sg.Text(token.name)])
                self.layout.append(
                    [sg.Input(key=token.key), sg.FileBrowse(initial_folder=token.default_value, key=token.key, )])

            elif token.field_type is FieldType.path_input:
                self.layout.append([sg.Text(token.name)])
                self.layout.append(
                    [sg.Input(key=token.key), sg.FolderBrowse(initial_folder=token.default_value, key=token.key, )])

            if row:
                self.layout.append(row)

        self.layout.append([sg.Button("Ok", key="ok-btn"),
                            sg.Button("Cancel", key="cancel-btn")])

    def validate_input(self, values: Dict[str, str]):
        isvalid = True

        for token in self.template.tokens:
            if token.field_type == FieldType.int_input:
                if not values.get(token.key, "").isdigit():
                    isvalid = False

        return isvalid

    def to_json(self, values: Dict[str, str]) -> dict:
        root = {}

        for token in self.template.tokens:
            if token.field_type == FieldType.int_input:
                root[token.key] = int(values[token.key])
            else:
                root[token.key] = values[token.key]
        return root

    def run(self):
        # Create the window
        window = sg.Window("Configurer", self.layout)

        # Create an event loop
        while True:
            event, values = window.read()
            if event == "cancel-btn" or event == sg.WIN_CLOSED:
                break
            elif event == "ok-btn":
                isvalid = self.validate_input(values)
                if isvalid:
                    return self.to_json(values)
                else:
                    print("invalid input")

        window.close()


if __name__ == "__main__":
    config_template = ConfigTemplate([
        Token(FieldType.text_input, "username", "Enter your name:", ""),
        Token(FieldType.int_input, "age", "Enter your age:", 18),
        Token(FieldType.path_input, "folder", "Enter a folder", "..")
    ])
    config = Configurer(config_template)
    print(config.run())
