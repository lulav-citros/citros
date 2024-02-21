from rich_argparse import RichHelpFormatter


class RichHelpFormatterCitros(RichHelpFormatter):
    def __init__(
        self,
        prog: str,
        indent_increment: int = 2,
        max_help_position: int = 24,
        width=None,
    ) -> None:
        super().__init__(prog, indent_increment=4, max_help_position=40, width=width)
