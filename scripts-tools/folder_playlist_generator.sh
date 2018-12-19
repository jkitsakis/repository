#!/bin/bash


DIR=./'Favorite Tracks 3'


#cd $DIR
#BASEDIR=`pwd`

# Remove existing playlists
#find . -name '*.m3u'|sed -e "s/^/\"/"|sed -e "s/$/\"/"|xargs rm -f

find . -type d |sort| while read -r DIR; do
      find . -type f |grep -v m3u | grep -i mp3 |sort> '00-FavoriteTracks3-Playlist.m3u'
done