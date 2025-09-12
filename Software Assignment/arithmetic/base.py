class Arithmetic:
    DIGITS = "0123456789ABCDEF"

    @staticmethod
    def parse(num_str: str, radix: int) -> int:
        """Parse number string in given radix into Python int."""
        return int(num_str, radix)