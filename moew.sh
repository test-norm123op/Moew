#!/bin/sh
python3 ~/moew/search.py "$(rofi -dmenu -l 0 -theme '/home/navbuggie/rfConfigs/config.rasi')"
val=$(cat ~/moew/data/appcode.txt)
if [ $val == "0" ]
then
    cat ~/moew/data/searchres.txt | python3 ~/moew/getstream.py "$(rofi -dmenu -sep '\x0f' -format i -theme '/home/navbuggie/rfConfigs/config.rasi')"
fi

