from typing import Dict

NO_OF_CHARS = 256

def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    size= len(pattern)
    table = [-1]*NO_OF_CHARS
    for i in range(size):
        table[ord(pattern[i])] = i
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        raise Exception("TODO")
        return -1

    def search(self) -> int:
        m = len(self.pattern)
        n = len(self.text)
        s = 0
        while(s <= n-m):
            j = m-1
            while j>=0 and self.pattern[j] == self.text[s+j]:
                j -= 1
            if j<0:
                return s
                s += (m-self.table[ord(self.text[s+m])] if s+m<n else 1)
            else:
                s += max(1, j-self.table[ord(self.text[s+j])])
        return -1