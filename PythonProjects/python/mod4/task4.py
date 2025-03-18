s = input().strip()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
odds = [ch for ch, cnt in freq.items() if cnt % 2]
if len(odds) > 1:
    print("Невозможно составить палиндром")
else:
    left, mid = "", ""
    for ch in sorted(freq.keys()):
        count = freq[ch]
        left += ch * (count // 2)
        if count % 2:
            mid = ch
    print(left + mid + left[::-1])