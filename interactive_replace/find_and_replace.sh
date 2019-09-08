# Method 1 
#-----------------------------------------------------------------
#for filename in *.txt; do vim -c '%s/omg/excellent/gc' -c 'wq' "$filename"; done
#for i in *.v ; do vim -c '%s/omg/hello/gc' -c 'wq' $i; done; 
#-----------------------------------------------------------------

for FILENAME in `find DIRECTORYPATH -type f -name \*.v`
do 
    vim -c '%s/PATTERN/REPLACEMENT/gc' -c 'wq' $FILENAME
done
