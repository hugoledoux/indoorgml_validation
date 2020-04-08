import json
import sys

filename = sys.argv[1]
fin = open(filename)
j = json.loads(fin.read())

n701 = 0
n702 = 0
n703 = 0
n704 = 0

f = j['features'][0]
for e in f['errors_feature']:
    if e['code'] == 701:
        n701 += 1
    if e['code'] == 702:
        n702 += 1
    if e['code'] == 703:
        n703 += 1
    if e['code'] == 704:
        n704 += 1



print("701:\t%d" % (n701))
print("702:\t%d" % (n702))
print("703:\t%d" % (n703))
print("704:\t%d" % (n704))