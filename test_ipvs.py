import ipvs
print ipvs.__doc__
print dir(ipvs)

print "nr services:", ipvs.nr_services()
print "nr services:", ipvs.nr_services.__doc__

print "hash table size:", ipvs.hashtable_size()
print "hash table size:", ipvs.hashtable_size.__doc__
