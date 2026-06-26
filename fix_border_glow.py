c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()

# Add animated gradient border to game cards
old_css = '.game-card { transform-style: preserve-3d; perspective: 800px; }'
new_css = '''.game-card { position: relative; transform-style: preserve-3d; perspective: 800px; isolation: isolate; }
.game-card::before {
  content: ''; position: absolute; inset: -2px; border-radius: inherit;
  background: linear-gradient(60deg, #667eea, #764ba2, #3b82f6, #ec4899, #667eea);
  background-size: 300% 300%; z-index: -1;
  animation: borderGlow 4s ease infinite;
  pointer-events: none;
}
@keyframes borderGlow {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}'''

c = c.replace(old_css, new_css)

open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
print('Animated gradient border added')
