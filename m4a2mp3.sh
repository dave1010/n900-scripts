# attempt to convert m4a files to mp3
# mencoder on the n900 wasn't compiled with lame codec support 
so this doesn't work yet


for i in *.m4*; do
   mencoder "$i" -o "${i/m4a/mp3}" -oac mp3lame
done
