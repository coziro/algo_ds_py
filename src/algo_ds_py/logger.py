import inspect
import types
from typing import Any, Optional


class Logger:

    def __init__(
        self,
        enabled: bool=False,
        pprint: bool=False,
    ) -> None:
        self.enabled = enabled
        self.pprint = pprint

    def print_header(
        self,
        title: str
    ) -> None:
        if self.enabled:
            print(f'---- {title} ----')

    def print_subheader(
        self,
        title: str
    ) -> None:
        if self.enabled:
            print(f'-- {title} --')

    def print_text(
        self,
        text: str,
    ) -> None:
        if self.enabled:
            print(text)

    def _print_single_var_info(
        self,
        symbol: str,
        value: Any,
    ) -> None:
        if self.pprint and isinstance(value, list):
            print(f'{symbol} ({type(value).__name__}):')
            for i, elem in enumerate(value):
                print(f'  {i}: {elem}')
        else:
            print(f'{symbol}({type(value).__name__}): {value}')

    def print_vars(
        self,
        var_info: dict,
        var_names: Optional[list] = None,
    ) -> None:
        if not self.enabled:
            return

        if var_names:
            for symbol in var_names:
                value = var_info[symbol]
                self._print_single_var_info(symbol, value)

        else:
            for symbol, value in var_info.items():
                if symbol.startswith('_'):
                    continue
                if callable(value):
                    continue
                if isinstance(value, types.ModuleType):
                    continue
                self._print_single_var_info(symbol, value)

    def print_global_vars(
        self,
        header: Optional[str] = None,
        var_names: Optional[list] = None,
    ) -> None:
        if not self.enabled:
            return

        if header:
            self.print_header(header)

        frame = inspect.currentframe()
        caller_globals = {}
        if frame is not None and frame.f_back is not None:
            caller_globals = frame.f_back.f_globals

        self.print_vars(caller_globals, var_names)

    def __repr__(self) -> str:
        return f'Logger (enabled={self.enabled})'

    def __str__(self) -> str:
        return self.__repr__()
