c = open('game-blog-web/src/App.vue', 'r', encoding='utf8').read()

# Add particles template
c = c.replace('<template>', '<template>\n  <div class=\"particles-container\">\n    <span class=\"particle\" v-for=\"n in 20\" :key=\"n\" :style=\"{ left: Math.random()*100+\'%\', top: Math.random()*100+\'%\', animationDelay: Math.random()*8+\'s\', animationDuration: (6+Math.random()*6)+\'s\', width: (3+Math.random()*4)+\'px\', height: (3+Math.random()*4)+\'px\' }\"></span>\n  </div>')

# Add particles CSS before the first style rule  
c = c.replace('.page-fade-enter-active,', '.particles-container { position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden; }\n.particle { position: absolute; border-radius: 50%; background: var(--el-menu-active); opacity: 0.1; animation: particleFloat 8s ease-in-out infinite; }\n@keyframes particleFloat { 0%, 100% { transform: translateY(0) scale(1); } 25% { transform: translateY(-30px) scale(1.2); } 50% { transform: translateY(-10px) scale(0.8); } 75% { transform: translateY(-40px) scale(1.1); } }\n\n.page-fade-enter-active,')

open('game-blog-web/src/App.vue', 'w', encoding='utf8').write(c)
print('Particles added')
