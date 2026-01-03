pandoc class-notes-2026.md -s --highlight-style=tango -o temp.html
echo "<style>" > class-notes-2026.html
cat prog/style.css >> class-notes-2026.html
echo "</style>" >> class-notes-2026.html
cat temp.html >> class-notes-2026.html
rm temp.html

pandoc personal-notes-2026.md -s --highlight-style=tango -o temp.html
echo "<style>" > personal-notes-2026.html
cat prog/style.css >> personal-notes-2026.html
echo "</style>" >> personal-notes-2026.html
cat temp.html >> personal-notes-2026.html
rm temp.html
