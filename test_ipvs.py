import ipvs
print ipvs.__doc__
print dir(ipvs)

print "nr services:", ipvs.nr_services()
print "nr services:", ipvs.nr_services.__doc__
