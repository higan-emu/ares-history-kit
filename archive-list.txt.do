redo-always

printf "%s\n" ./archives/*.tar.xz | LC_ALL=C sort > "$3"

redo-stamp < "$3"
