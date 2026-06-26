c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()

# Update carousel dots animation
c = c.replace(
    '.carousel-dots span {\n  width: 10px;\n  height: 10px;\n  border-radius: 50%;\n  background: rgba(255,255,255,0.4);\n  cursor: pointer;\n  transition: background 0.3s;\n}\n.carousel-dots span.active {\n  background: #fff;\n  width: 24px;\n  border-radius: 5px;\n}',
    '.carousel-dots span {\n  width: 10px;\n  height: 10px;\n  border-radius: 50%;\n  background: rgba(255,255,255,0.3);\n  cursor: pointer;\n  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);\n}\n.carousel-dots span:hover {\n  background: rgba(255,255,255,0.6);\n  transform: scale(1.2);\n}\n.carousel-dots span.active {\n  background: #fff;\n  width: 28px;\n  border-radius: 5px;\n  box-shadow: 0 0 12px rgba(255,255,255,0.4);\n}'
)

# Add animated gradient to custom carousel
c = c.replace(
    '.custom-carousel {\n  position: relative;\n  border-radius: 12px;\n  overflow: hidden;\n  margin-bottom: 24px;\n  box-shadow: var(--shadow-md);\n  height: 360px;\n}',
    '.custom-carousel {\n  position: relative;\n  border-radius: 16px;\n  overflow: hidden;\n  margin-bottom: 28px;\n  box-shadow: 0 8px 32px rgba(0,0,0,0.12);\n  height: 360px;\n}'
)

# Better category tags
c = c.replace(
    '.category-tag { cursor: pointer; transition: transform 0.15s; }\n.category-tag:hover { transform: scale(1.05); }',
    '.category-tag { cursor: pointer; transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1); padding: 4px 0 !important; }\n.category-tag:hover { transform: translateY(-2px); filter: brightness(1.1); }'
)

# Update search bar
c = c.replace(
    '.search-bar { margin-bottom: 12px; }\n.search-input { max-width: 500px; }',
    '.search-bar { margin-bottom: 16px; }\n.search-input { max-width: 480px; }'
)

# Update section header
c = c.replace(
    '.section-header h1 {\n  font-size: 28px; color: var(--text-primary); font-weight: 700;\n}',
    '.section-header h1 {\n  font-size: 28px; color: var(--text-primary); font-weight: 800;\n  background: linear-gradient(135deg, var(--text-primary), var(--el-menu-active));\n  -webkit-background-clip: text;\n  -webkit-text-fill-color: transparent;\n  background-clip: text;\n}'
)

# Add float animation to game cards
old_card_ani = '.game-card {\n  cursor: pointer;\n  transition: transform 0.3s ease, box-shadow 0.3s ease;\n  margin-bottom: 20px;\n  animation: cardFadeIn 0.5s ease both;\n  animation-delay: var(--delay, 0s);\n}\n.game-card:hover { transform: var(--card-hover); box-shadow: var(--shadow-md); }'
new_card_ani = '.game-card {\n  cursor: pointer;\n  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);\n  margin-bottom: 24px;\n  animation: cardFadeIn 0.5s ease both;\n  animation-delay: var(--delay, 0s);\n  overflow: hidden;\n}\n.game-card:hover { transform: translateY(-8px); box-shadow: 0 16px 48px rgba(0,0,0,0.15); }'
c = c.replace(old_card_ani, new_card_ani)

open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
print('HomeView updated')
