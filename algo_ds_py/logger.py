"""logger

# How to use
logger = Logger(print=True)
logger.print_global_vars(header='input')
logger.print_vars(locals())
"""
from typing import Any, Optional


class Logger:

    def __init__(
        self,
        print: bool=False,
        pprint: bool=False,
    ) -> None:
        self.print = print
        self.pprint = pprint

    def print_header(
        self,
        title: str
    ) -> None:
        if self.print:
            print(f'---- {title} ----')

    def print_subheader(
        self,
        title: str
    ) -> None:
        if print:
            print(f'-- {title} --')

    def _print_single_var_info(
        self,
        symbol: str,
        value: Any,
    ):
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
    ):
        if not self.print:
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
                self._print_single_var_info(symbol, value)

    def print_global_vars(
        self,
        header: Optional[str] = None,
    ) -> None:
        if not self.print:
            return

        if header:
            self.print_header(header)

        self.print_vars(globals())

    def __repr__(self) -> str:
        return f'Logger (print={self.print})'

    def __str__(self) -> str:
        return self.__repr__()
