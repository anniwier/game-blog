c = open('game-blog-web/src/App.vue', 'r', encoding='utf8').read()
# Remove opacity:0 from reveal to make cards always visible
c = c.replace('.reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.6s ease, transform 0.6s ease; }', '.reveal { transition: opacity 0.6s ease, transform 0.6s ease; }')
c = c.replace('.reveal.visible { opacity: 1; transform: translateY(0); }', '')
open('game-blog-web/src/App.vue', 'w', encoding='utf8').write(c)

# Also increase glass opacity in dark mode
c2 = open('game-blog-web/src/assets/theme.css', 'r', encoding='utf8').read()
c2 = c2.replace('--glass-bg: rgba(15, 15, 35, 0.75);', '--glass-bg: rgba(15, 15, 35, 0.9);')
open('game-blog-web/src/assets/theme.css', 'w', encoding='utf8').write(c2)
print('Fixed dark mode visibility')
