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
        lengths = s[0:divider]
        lengths = lengths.split(',')
        strings = []
        start = divider + 1
        for l in lengths:
            end = start + int(l)
            substring = s[start:end]
            strings.append(substring)
            start += int(l)
        return strings