archive="$2"

redo-ifchange "$archive"

version=$(printf "%s" "$archive" | grep -Eo 'ares_[vr0-9a]+')

case "$archive" in
    *.tar.xz)
        release=$(
            tar tvf "$archive" |
                awk '{ print $4 "T" $5 }' |
                LC_ALL=C sort |
                tail -1
        )
        ;;
    *.zip)
        release=$(
            unzip -l "$archive" |
                awk '{ print $2 "T" $3 }' |
                grep : |
                LC_ALL=C sort |
                tail -1
        )
        ;;
    *)
        echo "unknown archive type $archive" >&2
        exit 1
        ;;
esac

printf "%s\t%s\n" "$release" "$version"
