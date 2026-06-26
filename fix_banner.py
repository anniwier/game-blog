c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()

# Replace banner template: remove img, simplify layout
old = '''        <div class=\"banner-bg\" :style=\"{ background: gradients[idx % gradients.length] }\">
          <img :src=\"game.coverImage\" class=\"banner-img\" :alt=\"game.title\" @error=\"handleImgError\" />
          <div class=\"banner-overlay\">'''

new = '''        <div class=\"banner-bg\" :style=\"{ background: gradients[idx % gradients.length] }">
          <div class=\"banner-overlay\">'''

c = c.replace(old, new)

# Replace handleImgError since we removed the banner img
old2 = '''function handleImgError(event: Event) {
  const img = event.target as HTMLImageElement
  img.style.display = 'none'
}'''

new2 = '''function handleImgError(_event: Event) {
  // Banner image removed, this is for card images
}'''

c = c.replace(old2, new2)

# Replace CSS: remove banner-img, simplify banner-bg
old3 = '''.banner-bg {
  width: 100%; height: 100%;
  position: relative;
  display: flex;
  align-items: flex-end;
}
.banner-img {
  position: absolute;
  right: 40px;
  top: 50%;
  transform: translateY(-50%);
  height: 260px;
  max-width: 40%;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.5);
}'''

new3 = '''.banner-bg {
  width: 100%; height: 100%;
  position: relative;
}'''

c = c.replace(old3, new3)

# Remove gradient computed since we don't need it anymore
# Actually keep it, it's used in banner

open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
print('Done')
