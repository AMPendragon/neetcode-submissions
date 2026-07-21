class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ''

        lengths = []
        text = ''
        for s in strs:
            lengths.append(str(len(s)))
            text += s
        encoded = ','.join(lengths) + ' ' + text
        return encoded
        
    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
            
        divider = s.find(' ')
        indexes = s[0:divider]
        indexes = indexes.split(',')
        strings = []
        start = divider + 1
        for index in indexes:
            end = start + int(index)
            substring = s[start:end]
            strings.append(substring)
            start += int(index)
        return strings