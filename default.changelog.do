version=$(basename "$2")

# Strip the "ares_" prefix from the version string.
bare_version=${version#ares_}

major_version=${bare_version%r*}
source="changes/changes_$major_version.html"
redo-ifchange "$source" ./extract-changelog.py

echo "Update to ares ${bare_version} release."
echo
./extract-changelog.py "$bare_version" "$source"
