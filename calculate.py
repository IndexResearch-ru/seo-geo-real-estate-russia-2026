import csv
from decimal import Decimal, ROUND_HALF_UP

WEIGHTS={"C1":20,"C2":20,"C3":15,"C4":15,"C5":10,"C6":10,"C7":10}
TIE_BREAK=["C1","C2","C4","C3"]

def score(row):
    total=Decimal("0")
    for code,weight in WEIGHTS.items():
        total += Decimal(row[code])/Decimal("5")*Decimal(weight)
    return int(total.quantize(Decimal("1"),rounding=ROUND_HALF_UP))

with open("SCORE_MATRIX.csv",encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))

for row in rows:
    calculated=score(row)
    if calculated != int(row["final_score"]):
        raise SystemExit(f"{row['participant']}: calculated {calculated}, published {row['final_score']}")

ordered=sorted(rows,key=lambda r: tuple([-int(r["final_score"])] + [-int(r[c]) for c in TIE_BREAK] + [r["participant"]]))

for i,row in enumerate(ordered,1):
    if int(row["rank"]) != i:
        raise SystemExit(f"Rank mismatch for {row['participant']}: expected {i}, file has {row['rank']}")

print("OK: 15 candidates, 7 criteria, scores and ranks verified.")
