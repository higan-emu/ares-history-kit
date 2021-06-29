version=$(basename "$2")

# Strip the "ares_" prefix from the version string.
bare_version=${version#ares_}

major_version=${bare_version%r*}
source="changes/changes_$major_version.html"

if [ -f "$source" ]; then
    redo-ifchange "$source" ./extract-changelog.py
    ./extract-changelog.py "$bare_version" "$source"
else
    echo "[No official changelog available for this version. -Ed.]"
fi
