import re
c = open('game-blog-web/src/components/AppLayout.vue', 'r', encoding='utf8').read()
c = c.replace(
    "import { useRoute } from 'vue-router'",
    "import { useRoute, ref, onMounted, onUnmounted } from 'vue'"
)
c = c.replace(
    'const themeStore = useThemeStore()',
    'const themeStore = useThemeStore()\nconst showBackToTop = ref(false)\n\nonMounted(() => {\n  const onScroll = () => { showBackToTop.value = window.scrollY > 400 }\n  window.addEventListener(\'scroll\', onScroll)\n})\nonUnmounted(() => window.removeEventListener(\'scroll\', onScroll))\n\nfunction scrollToTop() {\n  window.scrollTo({ top: 0, behavior: \'smooth\' })\n}'
)
c = c.replace(
    '</router-view>\n      </transition>\n    </div>',
    '</router-view>\n      </transition>\n      <el-button v-if="showBackToTop" class="back-to-top" circle type="primary" @click="scrollToTop">\n        <el-icon><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 15l-6-6-6 6"/></svg></el-icon>\n      </el-button>\n    </div>'
)
c = c.replace(
    '.main-content {\n  min-height: calc(100vh - 60px);\n}',
    '.main-content {\n  min-height: calc(100vh - 60px);\n}\n\n.back-to-top {\n  position: fixed !important;\n  bottom: 32px; right: 32px;\n  z-index: 999;\n  box-shadow: 0 4px 16px rgba(0,0,0,0.15);\n  transition: all 0.3s ease !important;\n}\n.back-to-top:hover {\n  transform: translateY(-3px);\n  box-shadow: 0 6px 24px rgba(0,0,0,0.2);\n}'
)
open('game-blog-web/src/components/AppLayout.vue', 'w', encoding='utf8').write(c)
print('AppLayout updated')
