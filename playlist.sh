# makes M3U playlists for each folder in MyDocs/.sounds/
# and creates all.m3u
# enables you to easily play a folder of music

# TODO delete old playlists
# TODO search for Ogg etc

# (c) David Hulbert 2010 BSD/MIT license

cd ~/MyDocs/.sounds
find -type f -iname "*.mp3" > all.m3u

for i in *; do
  echo Processing $i
  if [ -d "$i" ]; then
    find "$i/" -type f -iname "*.mp3" > "$i.m3u"
  fi
done

echo Done
