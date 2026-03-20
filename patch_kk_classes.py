import re

# Update index.html
with open('/app/public/index.html', 'r') as f:
    content = f.read()

content = content.replace(
    '<li><i class="fas fa-map-marker-alt mr-2 text-green-400"></i> Near By: KK Classes Dildarnagar, Union Bank ke samne wali gali mein</li>',
    '<li><i class="fas fa-map-marker-alt mr-2 text-green-400"></i> Near By: Union Bank ke samne wali gali mein, Dildarnagar</li>'
)

with open('/app/public/index.html', 'w') as f:
    f.write(content)


# Update contact.html
with open('/app/public/contact.html', 'r') as f:
    content = f.read()

content = content.replace(
    'Near By: KK Classes Dildarnagar,<br>',
    ''
)

# Remove the specific phone numbers
content = content.replace(
    '<p><a href="tel:+919336781250" class="hover:text-green-600 font-semibold"><i class="fas fa-phone mr-2 text-green-500"></i> +91 9336781250</a></p>\n',
    ''
)

content = content.replace(
    '<p><a href="tel:+916205153276" class="hover:text-green-600 font-semibold"><i class="fas fa-phone mr-2 text-green-500"></i> +91 6205153276</a></p>\n',
    ''
)


with open('/app/public/contact.html', 'w') as f:
    f.write(content)

print("Removed KK Classes and the phone numbers from index.html and contact.html.")
