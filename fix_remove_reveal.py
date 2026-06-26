# Remove all reveal classes from App.vue
c = open('game-blog-web/src/App.vue', 'r', encoding='utf8').read()
c = c.replace('.reveal { transition: opacity 0.6s ease, transform 0.6s ease; }\n', '')
c = c.replace('\n.reveal-delay-1 { transition-delay: 0.1s; }\n.reveal-delay-2 { transition-delay: 0.2s; }\n.reveal-delay-3 { transition-delay: 0.3s; }', '')
c = c.replace('\n  setTimeout(() => { document.querySelectorAll(\'.reveal\').forEach(el => observer.observe(el)) }, 100)\n  const observer = new IntersectionObserver((entries) => {\n    entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add(\'visible\') })\n  }, { threshold: 0.1 })', '')
open('game-blog-web/src/App.vue', 'w', encoding='utf8').write(c)

# Remove reveal classes from HomeView template
c2 = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()
c2 = c2.replace(' class=\"reveal\" :class=\"\'reveal-delay-\' + Math.min(index, 4)\"', '')
open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c2)
print('Scroll reveal removed')
