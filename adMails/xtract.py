# Credits
# https://gist.github.com/dhruvbaldawa/1476680/bc58a7bafbf9c4da9a9c03273c55045c4cb4bacd

import urllib,re

with open('links.txt', 'r') as f_l, open('mailIDs.txt', 'w') as f_m:
    for line in f_l:
        print line
        #f = urllib.urlopen("https://www.ee.iitb.ac.in/~viren/")
        f = urllib.urlopen(line)
        s = f.read()
        if re.findall(r"\+\d{2}\s?0?\d{10}",s):
            print re.findall(r"\+\d{2}\s?0?\d{10}",s)
            for item in re.findall(r"\+\d{2}\s?0?\d{10}",s):
                f_m.write(item + '\n')
        if re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s):
            print re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
            for item in re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s):
                f_m.write(item + '\n')
        if re.findall(r"[A-Za-z0-9._%+-]+\[AT\][A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s):
            print re.findall(r"[A-Za-z0-9._%+-]+\[AT\][A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
            for item in re.findall(r"[A-Za-z0-9._%+-]+\[AT\][A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s):
                f_m.write(item + '\n')
print "Done"
