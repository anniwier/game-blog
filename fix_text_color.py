c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()
old = '.carousel-overlay * {'
if old in c:
    print('Already fixed')
else:
    c = c.replace('color: #fff !important;\n}', 'color: #fff;\n}\n.carousel-overlay * { color: #fff !important; }')
    open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
    print('Fixed')
