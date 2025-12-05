from pathlib import Path
import re

class AoC:
    """
    A base class for Advent of Code puzzle solutions.
    This class handles loading puzzle input data, either from a file or from
    example data provided during initialization.
    Attributes:
        DAY (int): The day number of the Advent of Code puzzle.
        DATA (str): The loaded puzzle input data.
    Args:
        day (int): The day number of the puzzle.
        example_data (str, optional): Example data to use instead of file data. Defaults to "".
        use_example (bool, optional): Whether to use example data instead of loading from file. Defaults to False.
    """

    def __init__(self, day, year, use_example=False, use_example_nr=0) -> None:  
        """Initialize AoC object with day, example data, and usage flag."""      
        self.DAY = day
        self.YEAR = year
        self._USE_EXAMPLE = use_example
        self._USE_EXAMPLE_NR = use_example_nr
        self.DATA = self._load_data()
    
    def _load_data(self) -> str:   
        """Private method to load puzzle data based on configuration."""
        if not self._USE_EXAMPLE: 
            with open(f"{self.YEAR}/Day{self.DAY}/data.txt") as f:
                return f.read().strip()
        else:
            file_path = Path(f"ADVENTOFCODE_DATA/{self.YEAR}/Day{self.DAY}/example.txt").resolve()
            with open(file_path) as f:
                content = f.read().strip()
                pattern = r"#Example\s+Part\d+(.*?)(?=#Example\s+Part\d+|$)"

                matches = re.findall(pattern, content, re.DOTALL)
                if  not self._USE_EXAMPLE_NR or not matches: 
                    return content
                else:
                    if self._USE_EXAMPLE_NR <= len(matches):
                        return matches[self._USE_EXAMPLE_NR - 1].strip()
                    else:
                        raise ValueError(f"Example number {self._USE_EXAMPLE_NR} not found in example.txt")





