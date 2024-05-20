from pathlib import Path
numbers = Path(input())
with open(numbers, 'r', encoding='utf-8') as file:
    sk = [int(cyc) for cyc in file]
mid = round(sum(sk) / len(sk))
print(sum(map(lambda x: abs(x - mid), sk)))
