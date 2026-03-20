with open('/app/public/facilities.html', 'r') as f:
    content = f.read()

# We need to remove the whole gallery section we added previously.
import re

# Find the start of the Photo Gallery comment and the end of its div
start_str = "    <!-- Photo Gallery -->"
end_str = "    <!-- Floating Action Buttons -->"

if start_str in content and end_str in content:
    start_index = content.find(start_str)
    end_index = content.find(end_str)

    new_content = content[:start_index] + content[end_index:]

    with open('/app/public/facilities.html', 'w') as f:
        f.write(new_content)
    print("Removed gallery from facilities.html")
else:
    print("Could not find gallery bounds in facilities.html")
