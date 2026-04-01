import os

with open('/app/public/index.html', 'r') as f:
    content = f.read()

# The popup modal HTML
popup_html = """
    <!-- Notification Popup -->
    <div id="notification-popup" class="fixed inset-0 z-[100] flex items-center justify-center bg-black bg-opacity-75 hidden">
        <div class="relative bg-white p-2 rounded-lg max-w-[90vw] md:max-w-[70vw] lg:max-w-4xl shadow-2xl transform scale-95 transition-transform duration-300">
            <button onclick="document.getElementById('notification-popup').style.display='none'" class="absolute -top-4 -right-4 bg-red-600 text-white hover:bg-red-700 rounded-full w-10 h-10 flex items-center justify-center font-bold text-xl shadow-lg border-2 border-white z-10 transition">
                &times;
            </button>
            <img src="assets/IMG-20260320-WA0001.jpg" alt="Anukul Academy Notification" class="w-full h-auto rounded-md">
        </div>
    </div>

    <script>
        // Show popup when page loads
        document.addEventListener('DOMContentLoaded', function() {
            const popup = document.getElementById('notification-popup');
            if (popup) {
                // Remove hidden class and set display
                popup.classList.remove('hidden');
                popup.style.display = 'flex';
                // Trigger animation
                setTimeout(() => {
                    popup.firstElementChild.classList.remove('scale-95');
                    popup.firstElementChild.classList.add('scale-100');
                }, 50);
            }
        });
    </script>
"""

# The new Hero Section HTML
new_hero = """
    <!-- Hero Section -->
    <div class="relative bg-gray-900 overflow-hidden h-[90vh] min-h-[600px] flex items-center justify-center">
        <!-- Background Image with Overlay -->
        <div class="absolute inset-0">
            <img class="w-full h-full object-cover" src="assets/IMG-20260320-WA0004.jpg" alt="Library Study Desks">
            <div class="absolute inset-0 bg-green-900 bg-opacity-70 mix-blend-multiply"></div>
            <div class="absolute inset-0 bg-gradient-to-t from-gray-900 via-transparent to-transparent opacity-80"></div>
        </div>

        <!-- Hero Content -->
        <div class="relative z-10 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center mt-10">
            <h1 class="text-4xl tracking-tight font-extrabold text-white sm:text-5xl md:text-6xl drop-shadow-lg">
                <span class="block mb-2">Welcome to</span>
                <span class="block text-green-300 drop-shadow-md">Anukul Library & Academy</span>
            </h1>
            <p class="mt-6 max-w-2xl mx-auto text-xl text-gray-200 drop-shadow sm:text-2xl">
                "स्वअध्ययन ही सफलता का मूल मंत्र है |"
            </p>
            <p class="mt-2 max-w-2xl mx-auto text-lg text-gray-300 drop-shadow">
                24x7 Open Library providing the best environment for students in Dildarnagar.
            </p>

            <div class="mt-10 sm:flex sm:justify-center gap-4">
                <div class="rounded-md shadow">
                    <a href="gallery.html" class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-bold rounded-full text-green-900 bg-green-300 hover:bg-white hover:text-green-800 md:py-4 md:text-lg transition duration-300 transform hover:-translate-y-1 hover:shadow-xl">
                        Explore Library
                        <i class="fas fa-arrow-right ml-2"></i>
                    </a>
                </div>
                <div class="mt-3 sm:mt-0 rounded-md shadow">
                    <a href="facilities.html" class="w-full flex items-center justify-center px-8 py-3 border-2 border-white text-base font-bold rounded-full text-white bg-transparent hover:bg-white hover:text-green-900 md:py-4 md:text-lg transition duration-300 transform hover:-translate-y-1 hover:shadow-xl">
                        Our Facilities
                    </a>
                </div>
            </div>
        </div>
    </div>
"""

# Find and replace the old hero section
start_hero = "    <!-- Hero Section -->"
end_hero = "    <!-- Highlights Section -->"

if start_hero in content and end_hero in content:
    start_index = content.find(start_hero)
    end_index = content.find(end_hero)

    # Insert new hero section and popup right after nav
    content = content[:start_index] + popup_html + new_hero + '\n' + content[end_index:]

    with open('/app/public/index.html', 'w') as f:
        f.write(content)
    print("Updated index.html with new hero section and popup")
else:
    print("Could not find hero section boundaries in index.html")
