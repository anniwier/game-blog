# 1. Remove dark mode CSS from theme.css
c = open('game-blog-web/src/assets/theme.css', 'r', encoding='utf8').read()
c = c.replace('\n\n.theme-dark {\n  --bg-primary: #0f0f23;\n  --bg-gradient: linear-gradient(135deg, #0a0a1a 0%, #14143a 50%, #0f172a 100%);\n  --bg-secondary: #1a1a3e;\n  --bg-card: #1a1a3e;\n  --bg-nav: #141430;\n  --text-primary: #e0e0f0;\n  --text-secondary: #a0a0c0;\n  --text-muted: #6a6a8a;\n  --border-color: #2a2a50;\n  --shadow-sm: 0 2px 8px rgba(0,0,0,0.3);\n  --shadow-md: 0 4px 16px rgba(0,0,0,0.4);\n  --shadow-lg: 0 8px 32px rgba(0,0,0,0.5);\n  --hero-bg: linear-gradient(135deg, #1a1a3e 0%, #0f0f23 100%);\n  --card-hover: translateY(-6px);\n  --rating-color: #fbbf24;\n  --tag-bg: #4a6fa5;\n  --input-bg: #1e1e42;\n  --el-menu-bg: #141430;\n  --el-menu-text: #c0c0e0;\n  --el-menu-active: #667eea;\n  --glass-bg: rgba(15, 15, 35, 0.9);\n  --glass-border: rgba(255, 255, 255, 0.06);\n  --glass-shadow: 0 8px 32px rgba(0,0,0,0.3);\n}', '')
open('game-blog-web/src/assets/theme.css', 'w', encoding='utf8').write(c)

# 2. Remove dark scrollbar styles
c2 = open('game-blog-web/src/assets/theme.css', 'r', encoding='utf8').read()
c2 = c2.replace('\n.theme-dark ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.15); }', '')
open('game-blog-web/src/assets/theme.css', 'w', encoding='utf8').write(c2)
print('1. Dark mode CSS removed')
