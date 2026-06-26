import re
c = open('game-blog-web/src/components/AppLayout.vue', 'r', encoding='utf8').read()
c = c.replace("import { useThemeStore } from \x27@/stores/theme\x27\n", "")
c = c.replace("\nconst themeStore = useThemeStore()", "")
c = c.replace(" :class=\x22{ \x27theme-dark\x27: themeStore.isDark }\x22", "")
c = c.replace("Moon, Sunny, ", "")
c = c.replace(", Moon, Sunny", "")
open('game-blog-web/src/components/AppLayout.vue', 'w', encoding='utf8').write(c)
print('AppLayout done')
