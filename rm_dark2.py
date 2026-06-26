# 3. Remove theme toggle from AppLayout
c = open('game-blog-web/src/components/AppLayout.vue', 'r', encoding='utf8').read()
c = c.replace('import { useThemeStore } from '@/stores/theme'\n, '')
c = c.replace('\nconst themeStore = useThemeStore()', '')
c = c.replace(' :class="{ \'theme-dark\': themeStore.isDark }"', '')
c = c.replace('\n      <el-menu-item index=\"theme\" @click=\"themeStore.toggle()\">\n        <el-icon><template v-if=\"themeStore.isDark\"><Moon /></template><template v-else><Sunny /></template></el-icon>\n      </el-menu-item>', '')
c = c.replace(', Moon, Sunny', '')
open('game-blog-web/src/components/AppLayout.vue', 'w', encoding='utf8').write(c)

# 4. Remove theme store from App.vue
c2 = open('game-blog-web/src/App.vue', 'r', encoding='utf8').read()
c2 = c2.replace("import { useThemeStore } from '@/stores/theme'\n", '')
c2 = c2.replace('\nconst themeStore = useThemeStore()\nonMounted(() => themeStore.init())', '')
open('game-blog-web/src/App.vue', 'w', encoding='utf8').write(c2)
print('2. Theme toggle removed')
