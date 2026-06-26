c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()
old = 'featuredGames.value = res.data.slice(0, 4)'
new = '// Pick 4 random games for the carousel\n    const shuffled = [...res.data].sort(() => Math.random() - 0.5)\n    featuredGames.value = shuffled.slice(0, 4)'
c = c.replace(old, new)
open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
print('Done')
