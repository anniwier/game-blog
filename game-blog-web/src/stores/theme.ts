import { defineStore } from 'pinia'
import { ref, watch } from 'vue'

export const useThemeStore = defineStore('theme', () => {
  const isDark = ref(localStorage.getItem('theme') === 'dark')

  function toggle() {
    isDark.value = !isDark.value
  }

  function init() {
    applyTheme()
  }

  function applyTheme() {
    const root = document.documentElement
    if (isDark.value) {
      root.classList.remove('theme-light')
      root.classList.add('theme-dark')
    } else {
      root.classList.remove('theme-dark')
      root.classList.add('theme-light')
    }
    localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
  }

  // Auto-apply when isDark changes
  watch(isDark, applyTheme, { immediate: false })

  return { isDark, toggle, init }
})
