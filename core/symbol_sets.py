from data.hiragana import HIRAGANA
from data.katakana import KATAKANA
import typing

def get_hiragana_only() -> dict:
    '''
    get_hiragana_only() get and return the Hiragana symbols dict modeled on data/.
    
    :return: Hiragana dictionary with its symbols and its romaji meaning
    :rtype: dict
    '''
    return HIRAGANA

def get_katakana_only() -> dict:
    '''
    get_katakana_only() get and return the Katakana symbols dict modeled on data/.
    
    :return: Katakana dictionary with its symbols and its romaji meaning
    :rtype: dict
    '''
    return KATAKANA

def get_all_symbols_mixed() -> dict:
    '''
    get_all_symbols_mixed() get and return a dict that combines all the combined dicts of symbols (currently a combination of Hiragana and Katakana).
    
    :return: Katakana dictionary with its symbols and its romaji meaning
    :rtype: dict
    '''
    return HIRAGANA | KATAKANA