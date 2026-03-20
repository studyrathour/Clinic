import os

files = ['/app/public/index.html', '/app/public/facilities.html', '/app/public/academy.html', '/app/public/contact.html']

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # Desktop nav
    content = content.replace(
        '<a href="academy.html" class="hover:bg-green-600 px-3 py-2 rounded-md text-sm font-medium transition duration-300">Academy</a>',
        '<a href="academy.html" class="hover:bg-green-600 px-3 py-2 rounded-md text-sm font-medium transition duration-300">Academy</a>\n                        <a href="gallery.html" class="hover:bg-green-600 px-3 py-2 rounded-md text-sm font-medium transition duration-300">Gallery</a>'
    )
    # Mobile nav
    content = content.replace(
        '<a href="academy.html" class="hover:bg-green-700 block px-3 py-2 rounded-md text-base font-medium text-white">Academy</a>',
        '<a href="academy.html" class="hover:bg-green-700 block px-3 py-2 rounded-md text-base font-medium text-white">Academy</a>\n                <a href="gallery.html" class="hover:bg-green-700 block px-3 py-2 rounded-md text-base font-medium text-white">Gallery</a>'
    )

    with open(file, 'w') as f:
        f.write(content)

print("Updated navigation in all files.")
