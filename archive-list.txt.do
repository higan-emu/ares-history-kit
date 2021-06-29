redo-always

# Archives are all the tarballs, and all the source zips,
# except for the v115 source zip which is redundant with ares_v115.tar.xz
printf "%s\n" ./archives/*.tar.xz ./archives/*-source.zip |
    grep -v ares_v115-source.zip |
    LC_ALL=C sort > "$3"

redo-stamp < "$3"
