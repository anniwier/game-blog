import re
c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()
# Remove the ::before animated border and borderGlow keyframes
old_border = ".game-card::before {\n  content: ''; position: absolute; inset: -2px; border-radius: inherit;\n  background: linear-gradient(60deg, #667eea, #764ba2, #3b82f6, #ec4899, #667eea);\n  background-size: 300% 300%; z-index: -1;\n  animation: borderGlow 4s ease infinite;\n  pointer-events: none;\n}"
c = c.replace(old_border, '')
c = c.replace('@keyframes borderGlow {\n  0%, 100% { background-position: 0% 50%; }\n  50% { background-position: 100% 50%; }\n}', '')
open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
print('Removed border glow')
