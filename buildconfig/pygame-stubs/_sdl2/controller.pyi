from pygame.joystick import Joystick
from typing import Dict

def init() -> None: ...
def get_init() -> bool: ...
def quit() -> None: ...

def set_eventstate(state: bool) -> None: ...
def get_eventstate() -> bool: ...

def get_count() -> int: ...
def is_controller(index: int) -> bool: ...
def name_forindex(index: int) -> str | None: ...

class Controller:
    def __init__(self, index: int) -> None: ...
    def init(self) -> None: ...
    def get_init(self) -> bool: ...
    def quit(self) -> None: ...
    @staticmethod
    def from_joystick(joy: Joystick) -> Controller: ...

    def attached(self) -> bool: ...
    def as_joystick(self) -> Joystick: ...
    def get_axis(self, axis: int) -> int: ...
    def get_button(self, button: int) -> bool: ...
    def get_mapping(self) -> Dict: ...
    def set_mapping(self, mapping: Dict) -> int: ...