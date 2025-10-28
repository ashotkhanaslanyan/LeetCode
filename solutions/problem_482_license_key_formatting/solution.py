class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        newKey: str = f'{s[:len(s)%k]}'
        fullIndex: int = len(s)%k
        for i in range(fullIndex, len(s)-k+1, k):
            newKey += f'-{s[i:i+k]}' if len(newKey) > 0 else s[i:i+k]
        return newKey