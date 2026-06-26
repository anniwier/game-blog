c = open('game-blog-web/src/views/HomeView.vue', 'r', encoding='utf8').read()

# 1. Replace el-carousel with custom carousel
oldCarousel = '''    <!-- Banner Carousel -->
    <el-carousel class=\"banner-carousel\" height=\"360px\" indicator-position=\"\" :interval=\"5000\">
      <el-carousel-item v-for=\"(game, idx) in featuredGames\" :key=\"game.id\" class=\"banner-slide\">
        <div class=\"banner-bg\" :style=\"{ background: gradients[idx % gradients.length] }\">
          <div class=\"banner-overlay\">
            <h2 class=\"banner-title\">{{ game.title }}</h2>
            <p class=\"banner-summary\">{{ game.summary }}</p>
            <div class=\"banner-meta\">
              <el-tag v-for=\"tag in game.tags\" :key=\"tag.id\" :color=\"tag.color || '#409eff'\" size=\"small\" style=\"color:#fff;margin-right:6px;\">{{ tag.tagName }}</el-tag>
              <span class=\"banner-rating\"><el-icon><StarFilled /></el-icon> {{ game.rating }}</span>
            </div>
            <el-button type=\"primary\" size=\"large\" round @click=\"goToGame(game.id)\">查看详情</el-button>
          </div>
        </div>
      </el-carousel-item>
    </el-carousel>'''

newCarousel = '''    <!-- Custom Carousel -->
    <div class=\"custom-carousel\">
      <div class=\"carousel-slide\" v-for=\"(game, idx) in featuredGames\" :key=\"game.id\" v-show=\"currentSlide === idx\">
        <div class=\"carousel-bg\" :style=\"{ background: gradients[idx % gradients.length] }\">
          <div class=\"carousel-overlay\">
            <h2 class=\"carousel-title\">{{ game.title }}</h2>
            <p class=\"carousel-summary\">{{ game.summary }}</p>
            <div class=\"carousel-meta\">
              <el-tag v-for=\"tag in game.tags\" :key=\"tag.id\" :color=\"tag.color || '#409eff'\" size=\"small\" style=\"color:#fff;margin-right:6px;\">{{ tag.tagName }}</el-tag>
              <span class=\"carousel-rating\"><el-icon><StarFilled /></el-icon> {{ game.rating }}</span>
            </div>
            <el-button type=\"primary\" size=\"large\" round @click=\"goToGame(game.id)\">查看详情</el-button>
          </div>
        </div>
      </div>
      <div class=\"carousel-dots\">
        <span v-for=\"(g, i) in featuredGames\" :key=\"g.id\" :class=\"{ active: currentSlide === i }\" @click=\"currentSlide = i\"></span>
      </div>
    </div>'''

c = c.replace(oldCarousel, newCarousel)

# 2. Add onUnmounted to import
c = c.replace('import { ref, computed, onMounted } from \'vue\'', 'import { ref, computed, onMounted, onUnmounted } from \'vue\'')

# 3. Add currentSlide ref and timer
oldRefs = 'const featuredGames = ref<GameItem[]>([])'
newRefs = 'const featuredGames = ref<GameItem[]>([])\nconst currentSlide = ref(0)\nlet slideTimer = 0'
c = c.replace(oldRefs, newRefs)

# 4. Add timer functions after featuredGames population
oldOnMount = '''    categories.value = catRes.data || []
  } catch (error) {
    console.error('获取游戏列表失败:', error)
  }
})'''

newOnMount = '''    categories.value = catRes.data || []
    startSlideTimer()
  } catch (error) {
    console.error('获取游戏列表失败:', error)
  }
})

function startSlideTimer() {
  if (slideTimer) clearInterval(slideTimer)
  slideTimer = window.setInterval(() => {
    if (featuredGames.value.length > 0) {
      currentSlide.value = (currentSlide.value + 1) % featuredGames.value.length
    }
  }, 5000)
}

onUnmounted(() => { if (slideTimer) clearInterval(slideTimer) })'''

c = c.replace(oldOnMount, newOnMount)

# 5. Replace banner CSS with custom carousel CSS
oldBannerCSS = '''.banner-carousel {
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 24px;
  box-shadow: var(--shadow-md);
  position: relative;
}
.banner-slide { position: relative; }
.banner-bg {
  width: 100%; height: 100%;
  position: relative;
}
.banner-overlay {
  position: absolute; bottom: 0; left: 0; right: 0;
  padding: 40px;
  background: linear-gradient(transparent, rgba(0,0,0,0.75));
  color: #fff;
}
.banner-title {
  font-size: 28px; margin-bottom: 8px;
  text-shadow: 0 2px 8px rgba(0,0,0,0.5);
}
.banner-summary {
  font-size: 14px; opacity: 0.9;
  margin-bottom: 12px; max-width: 500px;
}
.banner-meta { display: flex; align-items: center; margin-bottom: 16px; }
.banner-rating { display: flex; align-items: center; gap: 4px; color: #fbbf24; font-size: 14px; margin-left: 8px; }'''

newBannerCSS = '''.custom-carousel {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 24px;
  box-shadow: var(--shadow-md);
  height: 360px;
}
.carousel-slide {
  height: 100%;
  width: 100%;
}
.carousel-bg {
  width: 100%; height: 100%;
  position: relative;
  border-radius: 12px;
}
.carousel-overlay {
  position: absolute; bottom: 0; left: 0; right: 0;
  padding: 40px;
  background: linear-gradient(transparent, rgba(0,0,0,0.75));
  color: #fff;
}
.carousel-title {
  font-size: 28px; margin-bottom: 8px;
  text-shadow: 0 2px 8px rgba(0,0,0,0.5);
}
.carousel-summary {
  font-size: 14px; opacity: 0.9;
  margin-bottom: 12px; max-width: 500px;
}
.carousel-meta { display: flex; align-items: center; margin-bottom: 16px; }
.carousel-rating { display: flex; align-items: center; gap: 4px; color: #fbbf24; font-size: 14px; margin-left: 8px; }
.carousel-dots {
  position: absolute;
  bottom: 16px;
  right: 40px;
  display: flex;
  gap: 8px;
  z-index: 10;
}
.carousel-dots span {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255,255,255,0.4);
  cursor: pointer;
  transition: background 0.3s;
}
.carousel-dots span.active {
  background: #fff;
  width: 24px;
  border-radius: 5px;
}'''

c = c.replace(oldBannerCSS, newBannerCSS)

open('game-blog-web/src/views/HomeView.vue', 'w', encoding='utf8').write(c)
print('Done')
