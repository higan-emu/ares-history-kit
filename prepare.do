redo-ifchange ./releases.txt
redo-ifchange $(cut -f2 ./releases.txt | sed -e 's#.*#changes/&.changelog#')
