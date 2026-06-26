c = open('game-blog-web/src/assets/theme.css', 'r', encoding='utf8').read()
c = c.replace(
    '--bg-primary: #f0f2f5;\n  --bg-secondary: #ffffff;',
    '--bg-primary: #f0f2f5;\n  --bg-gradient: linear-gradient(135deg, #f0f2f5 0%, #e2e8f0 50%, #edf2f7 100%);\n  --bg-secondary: #ffffff;'
)
c = c.replace(
    '--bg-primary: #0f0f23;\n  --bg-secondary: #1a1a3e;',
    '--bg-primary: #0f0f23;\n  --bg-gradient: linear-gradient(135deg, #0f0f23 0%, #12123a 50%, #0d0d1f 100%);\n  --bg-secondary: #1a1a3e;'
)
c = c.replace('background: var(--bg-primary);', 'background: var(--bg-gradient);')
open('game-blog-web/src/assets/theme.css', 'w', encoding='utf8').write(c)
print('Background gradient added')
