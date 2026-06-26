import re

c = open('game-blog-web/src/components/AppLayout.vue', 'r', encoding='utf8').read()

# Add imports
c = c.replace(
    \"import { useRoute } from 'vue-router'\",
    \"import { useRoute } from 'vue-router'\nimport { ref, onMounted, onUnmounted } from 'vue'\"
)

# Add reactive vars after useThemeStore
c = c.replace(
    'const themeStore = useThemeStore()',
    '''const themeStore = useThemeStore()
const showBackToTop = ref(false)

onMounted(() => {
  const onScroll = () => { showBackToTop.value = window.scrollY > 400 }
  window.addEventListener('scroll', onScroll)
})
onUnmounted(() => window.removeEventListener('scroll', onScroll))

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}'''
)

# Add back to top button in template (after router-view area)
c = c.replace(
    '</router-view>\n      </transition>\n    </div>',
    '</router-view>\n      </transition>\n      <el-button v-if=\"showBackToTop\" class=\"back-to-top\" circle type=\"primary\" @click=\"scrollToTop\">\n        <el-icon><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><path d=\"M18 15l-6-6-6 6\"/></svg></el-icon>\n      </el-button>\n    </div>'
)

# Add CSS
old_css_end = '''.main-content {\n  min-height: calc(100vh - 60px);\n}\n</style>'''
new_css_end = '''.main-content {\n  min-height: calc(100vh - 60px);\n}\n\n.back-to-top {\n  position: fixed !important;\n  bottom: 32px; right: 32px;\n  z-index: 999;\n  box-shadow: 0 4px 16px rgba(0,0,0,0.15);\n  transition: all 0.3s ease !important;\n}\n.back-to-top:hover {\n  transform: translateY(-3px);\n  box-shadow: 0 6px 24px rgba(0,0,0,0.2);\n}\n</style>'''
c = c.replace(old_css_end, new_css_end)

open('game-blog-web/src/components/AppLayout.vue', 'w', encoding='utf8').write(c)
print('Back to top button added')
