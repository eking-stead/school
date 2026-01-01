pandoc plans-2026.md -s --highlight-style=tango -o temp.html
echo "<style>" > complete.html
cat style.css >> complete.html
echo "</style>" >> complete.html
cat temp.html >> complete.html
rm temp.html
