from stix2patterns.pattern import Pattern

p = Pattern("[ipv4-addr:value = '10.0.0.1']")

print p.inspect()
