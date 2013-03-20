import json
import random as rand

f = open('input.log','w')

for i in xrange(0,990):
    instance = {}
    instance["att1"] = rand.random()
    instance["att2"] = rand.random()
    instance["class"] = 0
    f.write(json.dumps(instance) + "\n")

for i in xrange(0,10):
    instance = {}
    instance["att1"] = rand.random()
    instance["att2"] = rand.random()
    instance["class"] = 1
    f.write(json.dumps(instance) + "\n")

f.close()