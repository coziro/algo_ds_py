"""logger

# How to use
logger = Logger(print=True)
logger.print_global_vars(header='input')
logger.print_vars(locals())
"""

class Logger:

    def __init__(self, print: bool=False) -> None:
        self.print = print

    def print_header(self, title: str) -> None:
        if not self.print:
            return
        print(f'---- {title} ----')

    def print_subheader(self, title: str) -> None:
        if not self.print: 
            return
        print(f'-- {title} --')

    def print_var(
        self,
        symbol,
        value,
        pprint:bool = False
    ):
        if pprint and isinstance(value, list):
            print(f'{symbol} ({type(value).__name__}):')
            for i, elem in enumerate(value):
                print(f'  {i}: {elem}')
        else:
            print(f'{symbol}({type(value).__name__}): {value}')

    def print_vars(
        self, 
        vars: dict,
        pprint: bool = False,
        var_names: list = None,
    ):
        if not self.print:
            return

        if var_names:
            for symbol in var_names:
                value = vars[symbol]
                self.print_var(symbol, value, pprint)

        else:
            for symbol, value in vars.items():
                if symbol.startswith('_'):
                    continue
                if callable(value):
                    continue
                else:
                    self.print_var(symbol, value, pprint)

    def print_global_vars(
        self, 
        header:str = None,
        pprint:bool = False,
    ) -> None:
        if not self.print:
            return

        if header:
            self.print_header(header)

        self.print_vars(globals(), pprint=pprint)

    def __repr__(self) -> str:
        return f'Logger (print={self.print})'

    def __str__(self) -> str:
        return self.__repr__()
