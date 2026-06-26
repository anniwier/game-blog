c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()

# Replace carousel slide: remove img tag, use stacked background
old = '<img :src=\"game.coverImage\" class=\"carousel-img\" :alt=\"game.title\" @error=\"handleImgError\" />\n          <div class=\"carousel-overlay\">'
new = '<div class=\"carousel-overlay\">'
c = c.replace(old, new)

# Update the carousel-bg to use stacked background with gradient + image URL
old2 = '<div class=\"carousel-bg\" :style=\"{ background: gradients[idx % gradients.length] }\">'
new2 = '<div class=\"carousel-bg\" :style=\"{ background: \'url(\' + game.coverImage + \') center/cover no-repeat, \' + gradients[idx % gradients.length] }\">'
c = c.replace(old2, new2)

# Remove carousel-img CSS  
c = c.replace('.carousel-img { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.35; }\n', '')
c = c.replace('  object-fit: cover; opacity: 0.35; width: 100%; height: 100%;\n', '')

# Add overflow hidden to carousel-bg
c = c.replace('border-radius: 12px;\n}', 'border-radius: 12px;\n  overflow: hidden;\n}')

open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
print('Done')
