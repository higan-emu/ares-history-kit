redo-ifchange archive-list.txt
redo-ifchange $(sed -e 's/.tar.xz$/.metadata/' archive-list.txt)

cat archive-list.txt | while read archive; do
    read release version < ${archive%.tar.xz}.metadata
    printf "%s\t%s\t%s\n" "$release" "$version" "$archive"
done | LC_ALL=C sort
