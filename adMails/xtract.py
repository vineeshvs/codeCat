# Credits
# https://gist.github.com/dhruvbaldawa/1476680/bc58a7bafbf9c4da9a9c03273c55045c4cb4bacd

import urllib,re
f = urllib.urlopen("http://www.ee.iitb.ac.in/~viren/")
s = f.read()
print re.findall(r"\+\d{2}\s?0?\d{10}",s)
print re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
print "Done"
