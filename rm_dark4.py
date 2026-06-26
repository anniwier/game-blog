import re
c = open('game-blog-web/src/App.vue', 'r', encoding='utf8').read()
c = c.replace("import { useThemeStore } from \x27@/stores/theme\x27\n", "")
c = c.replace("\nconst themeStore = useThemeStore()\nonMounted(() => themeStore.init())", "")
open('game-blog-web/src/App.vue', 'w', encoding='utf8').write(c)
print('App.vue done')
