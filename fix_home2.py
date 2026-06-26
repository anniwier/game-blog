c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()

# 1. Add handleCardImgError after handleImgError
old = """function handleImgError(event: Event) {
  const img = event.target as HTMLImageElement
  img.style.display = 'none'
}"""

new = """function handleImgError(event: Event) {
  const img = event.target as HTMLImageElement
  img.style.display = 'none'
}

function handleCardImgError(event: Event) {
  const img = event.target as HTMLImageElement
  const alt = img.alt || ''
  img.style.display = 'none'
  const wrap = img.parentElement
  if (wrap) {
    wrap.style.background = 'linear-gradient(135deg, #667eea, #764ba2)'
    wrap.style.display = 'flex'
    wrap.style.alignItems = 'center'
    wrap.style.justifyContent = 'center'
    const text = document.createElement('span')
    text.style.cssText = 'color:white;font-size:22px;font-weight:bold;text-align:center;padding:20px;'
    text.textContent = alt
    wrap.appendChild(text)
  }
}"""

c = c.replace(old, new)

# 2. Wrap card image in div with error handler  
old2 = '<img :src=\"game.coverImage\" class=\"game-cover\" :alt=\"game.title\" />'
new2 = '<div class=\"game-cover-wrap\">\n            <img :src=\"game.coverImage\" class=\"game-cover\" :alt=\"game.title\" @error=\"handleCardImgError\" />\n          </div>'
c = c.replace(old2, new2)

# 3. Update CSS
old3 = '.game-cover { width: 100%; height: 200px; object-fit: cover; }'
new3 = '.game-cover { width: 100%; height: 100%; object-fit: cover; }\n.game-cover-wrap { width: 100%; height: 200px; overflow: hidden; background: var(--bg-secondary); }'
c = c.replace(old3, new3)

open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
print('Done')
