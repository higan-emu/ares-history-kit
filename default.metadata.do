archive="$2".tar.xz

redo-ifchange "$archive"

version=$(basename "$archive" .tar.xz)
release=$(tar tvf "$archive" | awk '{ print $4 }' | LC_ALL=C sort | tail -1)

printf "%s\t%s\n" "$release" "$version"
