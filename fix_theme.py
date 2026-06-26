c = open('game-blog-web/src/assets/theme.css', 'r', encoding='utf8').read()

# Add glass morphism and animation variables at the top
glass_add = '''
/* ===== Glass Morphism & Effects ===== */
:root {
  --glass-bg: rgba(255, 255, 255, 0.7);
  --glass-border: rgba(255, 255, 255, 0.3);
  --glass-shadow: 0 8px 32px rgba(0,0,0,0.08);
  --glass-blur: blur(16px);
  --nav-height: 64px;
  --card-radius: 16px;
  --transition-smooth: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.theme-dark {
  --glass-bg: rgba(15, 15, 35, 0.75);
  --glass-border: rgba(255, 255, 255, 0.06);
  --glass-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* ===== Smooth Scrollbar ===== */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(0,0,0,0.15); border-radius: 3px; }
.theme-dark ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.15); }

/* ===== Animated Gradient Background ===== */
@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* ===== Glass Card ===== */
.glass-card {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border);
  border-radius: var(--card-radius);
  box-shadow: var(--glass-shadow);
  transition: var(--transition-smooth);
}
.glass-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.12);
}

/* ===== Glow Effect ===== */
.glow {
  transition: var(--transition-smooth);
}
.glow:hover {
  filter: brightness(1.1);
  box-shadow: 0 0 20px rgba(100, 126, 234, 0.3);
}

/* ===== Floating Animation ===== */
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

/* ===== Fade In Up ===== */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
'''

c = c.replace('/* ===== Theme: CSS Variables ===== */', glass_add + '\n/* ===== Theme: CSS Variables ===== */')

# Add glass overrides for Element Plus
c = c.replace('}', '''
}

/* ===== Glass Nav Override ===== */
.el-menu--horizontal {
  background: var(--glass-bg) !important;
  backdrop-filter: var(--glass-blur) !important;
  -webkit-backdrop-filter: var(--glass-blur) !important;
  border-bottom: 1px solid var(--glass-border) !important;
  height: var(--nav-height) !important;
}

/* ===== Glass Card Override ===== */
.el-card {
  background: var(--glass-bg) !important;
  backdrop-filter: var(--glass-blur) !important;
  -webkit-backdrop-filter: var(--glass-blur) !important;
  border: 1px solid var(--glass-border) !important;
  border-radius: var(--card-radius) !important;
  box-shadow: var(--glass-shadow) !important;
  transition: var(--transition-smooth) !important;
}
.el-card:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 12px 40px rgba(0,0,0,0.12) !important;
}

/* ===== Input Override ===== */
.el-input__wrapper {
  background: var(--glass-bg) !important;
  backdrop-filter: var(--glass-blur) !important;
  border: 1px solid var(--glass-border) !important;
  border-radius: 12px !important;
  box-shadow: none !important;
}
.el-input__wrapper.is-focus {
  border-color: var(--el-menu-active) !important;
  box-shadow: 0 0 0 3px rgba(64,158,255,0.15) !important;
}

/* ===== Tag Override ===== */
.el-tag {
  border-radius: 8px !important;
  font-weight: 500 !important;
}

/* ===== Button Override ===== */
.el-button--primary {
  border-radius: 10px !important;
  font-weight: 600 !important;
}

/* ===== Avatar Override ===== */
.el-avatar {
  border: 2px solid var(--glass-border) !important;
}
''')

open('game-blog-web/src/assets/theme.css', 'w', encoding='utf8').write(c)
print('theme.css updated with glass morphism')
