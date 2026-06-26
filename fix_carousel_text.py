c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()

# Ensure carousel overlay has white text and dark gradient
old_overlay = '''.carousel-overlay {
  position: absolute; bottom: 0; left: 0; right: 0;
  padding: 40px;
  background: linear-gradient(transparent, rgba(0,0,0,0.75));
  color: #fff;
}'''

new_overlay = '''.carousel-overlay {
  position: absolute; bottom: 0; left: 0; right: 0;
  padding: 40px 40px 32px;
  background: linear-gradient(rgba(0,0,0,0.05) 0%, rgba(0,0,0,0.85) 100%);
  color: #fff !important;
}'''

c = c.replace(old_overlay, new_overlay)

# Also ensure all carousel text elements are white
c = c.replace(
    '.carousel-title {\n  font-size: 28px; margin-bottom: 8px;\n  text-shadow: 0 2px 8px rgba(0,0,0,0.5);\n}',
    '.carousel-title {\n  font-size: 28px; margin-bottom: 8px;\n  text-shadow: 0 2px 12px rgba(0,0,0,0.6);\n  color: #fff !important;\n}'
)

c = c.replace(
    '.carousel-summary {\n  font-size: 14px; opacity: 0.9;\n  margin-bottom: 12px; max-width: 500px;\n}',
    '.carousel-summary {\n  font-size: 14px;\n  margin-bottom: 12px; max-width: 500px;\n  color: rgba(255,255,255,0.85) !important;\n}'
)

c = c.replace(
    '.carousel-rating { display: flex; align-items: center; gap: 4px; color: #fbbf24; font-size: 14px; margin-left: 8px; }',
    '.carousel-rating { display: flex; align-items: center; gap: 4px; color: #fbbf24 !important; font-size: 14px; margin-left: 8px; }'
)

# Ensure carousel button is visible
c = c.replace(
    '.banner-btn {\n  border-radius: 20px;\n  padding: 8px 28px;\n}',
    '.banner-btn {\n  border-radius: 20px;\n  padding: 8px 28px;\n}'
)

open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
print('Carousel text color fixed')
