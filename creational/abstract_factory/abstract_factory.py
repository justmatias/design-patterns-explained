from abc import ABC, abstractmethod
from dataclasses import dataclass


class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...

    @abstractmethod
    def on_click(self) -> str: ...


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str: ...

    @abstractmethod
    def on_toggle(self) -> str: ...


@dataclass
class WindowsButton(Button):
    label: str

    def render(self) -> str:
        return f"[Windows Button: {self.label}]"

    def on_click(self) -> str:
        return f"Windows button '{self.label}' clicked"


@dataclass
class MacOSButton(Button):
    label: str

    def render(self) -> str:
        return f"(macOS Button: {self.label})"

    def on_click(self) -> str:
        return f"macOS button '{self.label}' clicked"


@dataclass
class WindowsCheckbox(Checkbox):
    label: str

    def render(self) -> str:
        return f"[Windows Checkbox: {self.label}]"

    def on_toggle(self) -> str:
        return f"Windows checkbox '{self.label}' toggled"


@dataclass
class MacOSCheckbox(Checkbox):
    label: str

    def render(self) -> str:
        return f"(macOS Checkbox: {self.label})"

    def on_toggle(self) -> str:
        return f"macOS checkbox '{self.label}' toggled"


class UIFactory(ABC):
    @abstractmethod
    def create_button(self, label: str) -> Button: ...

    @abstractmethod
    def create_checkbox(self, label: str) -> Checkbox: ...


class WindowsUIFactory(UIFactory):
    def create_button(self, label: str) -> Button:
        return WindowsButton(label)

    def create_checkbox(self, label: str) -> Checkbox:
        return WindowsCheckbox(label)


class MacOSUIFactory(UIFactory):
    def create_button(self, label: str) -> Button:
        return MacOSButton(label)

    def create_checkbox(self, label: str) -> Checkbox:
        return MacOSCheckbox(label)


class Application:
    def __init__(self, factory: UIFactory) -> None:
        self._factory = factory
        self._button = factory.create_button("OK")
        self._checkbox = factory.create_checkbox("Accept terms")

    def render(self) -> None:
        print(self._button.render())
        print(self._checkbox.render())

    def interact(self) -> None:
        print(self._button.on_click())
        print(self._checkbox.on_toggle())


if __name__ == "__main__":
    import sys

    os_name = sys.argv[1] if len(sys.argv) > 1 else "windows"

    factory: UIFactory
    if os_name == "macos":
        factory = MacOSUIFactory()
    else:
        factory = WindowsUIFactory()

    app = Application(factory)
    app.render()
    app.interact()
