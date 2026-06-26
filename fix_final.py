# Fix AppLayout background
c = open('game-blog-web/src/components/AppLayout.vue', 'r', encoding='utf8').read()
c = c.replace('background: #f5f5f5;', 'background: transparent;')
open('game-blog-web/src/components/AppLayout.vue', 'w', encoding='utf8').write(c)

# Add scroll reveal to App.vue
c2 = open('game-blog-web/src/App.vue', 'r', encoding='utf8').read()
old = ".page-fade-leave-to {\n  opacity: 0;\n  transform: translateY(-10px);\n}"
new = ".page-fade-leave-to {\n  opacity: 0;\n  transform: translateY(-10px);\n}\n\n.reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.6s ease, transform 0.6s ease; }\n.reveal.visible { opacity: 1; transform: translateY(0); }\n.reveal-delay-1 { transition-delay: 0.1s; }\n.reveal-delay-2 { transition-delay: 0.2s; }\n.reveal-delay-3 { transition-delay: 0.3s; }"
c2 = c2.replace(old, new)

# Add scroll observer to script
old2 = "onMounted(() => themeStore.init())"
new2 = "onMounted(() => {\n  themeStore.init()\n  const observer = new IntersectionObserver((entries) => {\n    entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('visible') })\n  }, { threshold: 0.1 })\n  setTimeout(() => { document.querySelectorAll('.reveal').forEach(el => observer.observe(el)) }, 100)\n})"
c2 = c2.replace(old2, new2)

open('game-blog-web/src/App.vue', 'w', encoding='utf8').write(c2)
print('AppLayout + App.vue updated')
