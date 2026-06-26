import re
c = open("game-blog-web/src/App.vue", "r", encoding="utf8").read()
c = c.replace(
    "import { onMounted } from \x27vue\x27\nimport AppLayout from \x27@/components/AppLayout.vue\x27\nimport { useThemeStore } from \x27@/stores/theme\x27\n\nconst themeStore = useThemeStore()\nonMounted(() => {\n  themeStore.init()\n  const observer = new IntersectionObserver((entries) => {\n    entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add(\x27visible\x27) })\n  }, { threshold: 0.1 })\n  setTimeout(() => { document.querySelectorAll(\x27.reveal\x27).forEach(el => observer.observe(el)) }, 100)\n})",
    "import AppLayout from \x27@/components/AppLayout.vue\x27"
)
open("game-blog-web/src/App.vue", "w", encoding="utf8").write(c)
print("App.vue fixed")
