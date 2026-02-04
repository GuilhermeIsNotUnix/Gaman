import random

class Trainer:
    '''
    This class is responsible for training modes with the ability to filter the types of symbols to be considered in training (for example: only Hiragana, only Katakana, or all symbols).
    
    Attributes:
        symbol_pool (dict): Represents the pool of symbols being considered in the instance (example: it could be only Hiragana symbols, only Katakana symbols, or all combined).
        current_symbol: Represents the current random symbol.
        
    '''
    
    def __init__(self, symbol_pool: dict):
        '''
        __init__() Initializes the Trainer object with symbol_pool.
        
        :param symbol_pool: Represents the pool of symbols being considered in the instance (example: it could be only Hiragana symbols, only Katakana symbols, or all combined).
        :param current_symbol: Represents the current random symbol.
        '''
        self.symbol_pool = symbol_pool
        self.current_symbol = None