import re

with open('/app/public/facilities.html', 'r') as f:
    content = f.read()

gallery_html = """
    <!-- Photo Gallery -->
    <div class="py-16 bg-green-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl font-extrabold text-green-900 mb-8">Library Gallery</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                <img src="assets/IMG-20260320-WA0003.jpg" alt="Library Interior" class="rounded-lg shadow-md hover:shadow-xl transition transform hover:scale-105 w-full h-48 object-cover">
                <img src="assets/IMG-20260320-WA0004.jpg" alt="Library Interior" class="rounded-lg shadow-md hover:shadow-xl transition transform hover:scale-105 w-full h-48 object-cover">
                <img src="assets/IMG-20260320-WA0005.jpg" alt="Library Interior" class="rounded-lg shadow-md hover:shadow-xl transition transform hover:scale-105 w-full h-48 object-cover">
                <img src="assets/IMG-20260320-WA0006.jpg" alt="Library Interior" class="rounded-lg shadow-md hover:shadow-xl transition transform hover:scale-105 w-full h-48 object-cover">
                <img src="assets/IMG-20260320-WA0007.jpg" alt="Library Interior" class="rounded-lg shadow-md hover:shadow-xl transition transform hover:scale-105 w-full h-48 object-cover">
                <img src="assets/IMG-20260320-WA0008.jpg" alt="Library Interior" class="rounded-lg shadow-md hover:shadow-xl transition transform hover:scale-105 w-full h-48 object-cover">
                <img src="assets/IMG-20260320-WA0009.jpg" alt="Library Interior" class="rounded-lg shadow-md hover:shadow-xl transition transform hover:scale-105 w-full h-48 object-cover">
                <img src="assets/IMG-20260320-WA0010.jpg" alt="Library Interior" class="rounded-lg shadow-md hover:shadow-xl transition transform hover:scale-105 w-full h-48 object-cover">
                <img src="assets/IMG-20260320-WA0011.jpg" alt="Library Interior" class="rounded-lg shadow-md hover:shadow-xl transition transform hover:scale-105 w-full h-48 object-cover">
                <img src="assets/IMG-20260320-WA0012.jpg" alt="Library Interior" class="rounded-lg shadow-md hover:shadow-xl transition transform hover:scale-105 w-full h-48 object-cover">
                <img src="assets/IMG-20260320-WA0013.jpg" alt="Library Interior" class="rounded-lg shadow-md hover:shadow-xl transition transform hover:scale-105 w-full h-48 object-cover">
            </div>
        </div>
    </div>
"""

# Insert gallery right before the floating buttons
content = content.replace('<!-- Floating Action Buttons -->', gallery_html + '\n    <!-- Floating Action Buttons -->')

with open('/app/public/facilities.html', 'w') as f:
    f.write(content)

print("Gallery added to facilities.html")
