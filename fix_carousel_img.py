c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()
c = c.replace(
    '<div class=\"carousel-bg\" :style=\"{ background: gradients[idx % gradients.length] }\">\n          <div class=\"carousel-overlay\">',
    '<div class=\"carousel-bg\" :style=\"{ background: gradients[idx % gradients.length] }\">\n          <img :src=\"game.coverImage\" class=\"carousel-img\" :alt=\"game.title\" @error=\"handleImgError\" />\n          <div class=\"carousel-overlay\">'
)
c = c.replace(
    '.carousel-overlay {',
    '.carousel-img { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.35; }\n.carousel-overlay {'
)
open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
print('Done')
