c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()

# Add 3D tilt CSS
old_tilt_css = '''@keyframes cardFadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}'''
new_tilt_css = '''@keyframes cardFadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* 3D Card Tilt */
.game-card { transform-style: preserve-3d; perspective: 800px; }
.game-card .game-cover-wrap { transform-style: preserve-3d; }
.game-card .game-info { transform: translateZ(20px); }
.custom-carousel { perspective: 1000px; }'''
c = c.replace(old_tilt_css, new_tilt_css)

# Add reveal classes to card el-col
c = c.replace(
    '<el-col :xs=\"24\" :sm=\"12\" :md=\"8\" :lg=\"6\" v-for=\"(game, index) in games\" :key=\"game.id\">',
    '<el-col :xs=\"24\" :sm=\"12\" :md=\"8\" :lg=\"6\" v-for=\"(game, index) in games\" :key=\"game.id\" class=\"reveal\" :class=\"\'reveal-delay-\' + Math.min(index, 4)\">'
)

# Add mouse tilt events to game card
old_card = '<el-card class=\"game-card\" :style=\"{ \'--delay\': index * 0.08 + \'s\' }\" :body-style=\"{ padding: \'0px\' }\" @click=\"goToGame(game.id)\">'
new_card = '<el-card class=\"game-card\" :style=\"{ \'--delay\': index * 0.08 + \'s\' }\" :body-style=\"{ padding: \'0px\' }\" @click=\"goToGame(game.id)\" @mousemove=\"handleTilt()\" @mouseleave=\"handleTiltLeave()\">'
c = c.replace(old_card, new_card)

# Add tilt handler functions
c = c.replace(
    'function handleImgError(_event: Event) {',
    '''function handleTilt(e: MouseEvent) {
  const card = (e.currentTarget as HTMLElement)
  const rect = card.getBoundingClientRect()
  const x = e.clientX - rect.left
  const y = e.clientY - rect.top
  const centerX = rect.width / 2
  const centerY = rect.height / 2
  const rotateX = ((y - centerY) / centerY) * -8
  const rotateY = ((x - centerX) / centerX) * 8
  card.style.transform = 'perspective(800px) rotateX(' + rotateX + 'deg) rotateY(' + rotateY + 'deg) scale3d(1.02,1.02,1.02)'
}
function handleTiltLeave(e: Event) {
  (e.currentTarget as HTMLElement).style.transform = 'perspective(800px) rotateX(0deg) rotateY(0deg) scale3d(1,1,1)'
}

function handleImgError(_event: Event) {'''
)

open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
print('HomeView: 3D tilt + scroll reveal added')
