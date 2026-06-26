import re
c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()

# Replace banner section
old = '''<el-carousel-item v-for="game in featuredGames" :key="game.id" class="banner-slide">
        <div class="banner-bg" :style="{ backgroundImage: 'url(' + game.coverImage + ')' }">'''
new = '''<el-carousel-item v-for="(game, idx) in featuredGames" :key="game.id" class="banner-slide">
        <div class="banner-bg" :style="{ background: gradients[idx % gradients.length] }">
          <img :src="game.coverImage" class="banner-img" :alt="game.title" @error="handleImgError" />'''
c = c.replace(old, new)

# Update import
c = c.replace("import { ref, onMounted } from 'vue'", "import { ref, computed, onMounted } from 'vue'")

# Add gradients after featuredGames
old3 = 'const featuredGames = ref<GameItem[]>([])'
new3 = '''const featuredGames = ref<GameItem[]>([])
const gradients = computed(() => [
  'linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)',
  'linear-gradient(135deg, #0f3443 0%, #0d7377 50%, #34e89e 100%)',
  'linear-gradient(135deg, #2d1b69 0%, #6c3483 50%, #bb8fce 100%)',
  'linear-gradient(135deg, #7b241c 0%, #c0392b 50%, #f1948a 100%)',
])'''
c = c.replace(old3, new3)

# Add handleImgError
old4 = 'function goToGame(id: number) {\n  router.push("/games/" + id)\n}'
new4 = '''function goToGame(id: number) {
  router.push("/games/" + id)
}

function handleImgError(event: Event) {
  const img = event.target as HTMLImageElement
  img.style.display = 'none'
}'''
c = c.replace(old4, new4)

# Update CSS
old5 = '''.banner-bg {
  width: 100%; height: 100%;
  background-size: cover; background-position: center;
  position: relative;
}'''
new5 = '''.banner-bg {
  width: 100%; height: 100%;
  position: relative;
  display: flex;
  align-items: flex-end;
}
.banner-img {
  position: absolute;
  right: 40px;
  top: 50%;
  transform: translateY(-50%);
  height: 260px;
  max-width: 40%;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.5);
}'''
c = c.replace(old5, new5)

open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
print('Done')
