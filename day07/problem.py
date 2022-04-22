import re



lc = "LCNO-MAH-30-2500-0001"


res = re.match(r'LCNO-(KAR|MAH|TAL|TND|APN|GOA)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-([0-9]{3}[1-9])$', lc)
if res and len(lc) <= 21:
    print("match found", "=", res.group(0))
else:
    print("no match found")