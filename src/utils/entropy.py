from collections import Counter
from math import log2

def get_entropy(data: bytes) -> float:
    entropy = 0.0
    total_len = len(data)
    
    if total_len == 0:
        return 0.0
    
    for count in Counter(data).values():
        prob = count / total_len
        entropy -= prob * log2(prob)
        
    return entropy