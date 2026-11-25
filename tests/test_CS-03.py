"""Executable success criteria for spec clause CS-03. Case IDs match tests/CS-03.md."""
import sys, pathlib
from datetime import date, datetime, timezone
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from streaks import streak, local_day

TODAY = date(2026, 11, 24)
d = lambda m, day: date(2026, m, day)

CASES = {
    "CS-03-a": ([d(11, 22), d(11, 23), d(11, 24)], 3),
    "CS-03-b": ([d(11, 21), d(11, 22), d(11, 23)], 3),
    "CS-03-c": ([d(11, 20), d(11, 21), d(11, 22)], 0),
    "CS-03-d": ([d(11, 24), d(11, 24), d(11, 23)], 2),
    "CS-03-f": ([], 0),
}

failed = 0
for cid, (days, expected) in CASES.items():
    got = streak(days, TODAY)
    ok = got == expected
    failed += not ok
    print(f"{'PASS' if ok else 'FAIL'} {cid}: expected {expected}, got {got}")

# CS-03-e: 11:30 PM Miami on 11-24 is 04:30 UTC on 11-25
ts = datetime(2026, 11, 25, 4, 30, tzinfo=timezone.utc)
day = local_day(ts, "America/New_York")
ok = day == d(11, 24) and streak([day], TODAY) == 1
failed += not ok
print(f"{'PASS' if ok else 'FAIL'} CS-03-e: local day {day}")

sys.exit(1 if failed else 0)
