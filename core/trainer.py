import random
from typing import Dict, Tuple, Optional

class Trainer:
    '''
    This class is responsible for the logic of training modes with filtered or unfiltered symbols to be considered in training (for example: only Hiragana, only Katakana, or all symbols).
    
    Attributes:
        symbol_pool (dict): Represents the pool of symbols being considered in the instance (example: it could be only Hiragana symbols, only Katakana symbols, or all combined).
        current_symbol: Represents the current random symbol.
        
    '''
    
    def __init__(self, symbol_pool: Dict[str, str]):
        '''
        __init__() Initializes the Trainer object with symbol_pool and initializes self.current_symbol.
        
        :param symbol_pool: Represents the pool of symbols being considered in the instance (example: it could be only Hiragana symbols, only Katakana symbols, or all combined).
        '''
        self.symbol_pool = symbol_pool
        self.current_symbol: Optional[Tuple[str, str]] = None
    
    def get_random_symbol(self) -> Tuple[str, str]:
        '''
        Randomly generates a symbol (more technically, generates a tuple with the symbol and its respective romaji) updating the state of self.current_symbol for consistency.
        
        :return: Returns the current_symbol (a tuple of the randomly generated symbol and romaji).
        :rtype: tuple
        '''
        if not self.symbol_pool:
            raise ValueError("symbol_pool is empty")
        
        self.current_symbol = random.choice(list(self.symbol_pool.items()))
        return self.current_symbol