# Make tags clickable in HomeView
h = open("game-blog-web/src/views/HomeView.vue", "r", encoding="utf8").read()
# The tag line in home
h = h.replace(
    "style=\"color:#fff; margin-right:4px;\">",
    "style=\"color:#fff; margin-right:4px;cursor:pointer;\" @click.stop=\"goToTag(tag.id)\">"
)
# Add goToTag function
if "function goToTag" not in h:
    h = h.replace(
        "function goToGame(id: number) {",
        "function goToTag(tagId: number) { router.push(\"/tags/\" + tagId) }\n\nfunction goToGame(id: number) {"
    )
open("game-blog-web/src/views/HomeView.vue", "w", encoding="utf8").write(h)

# Make tags clickable in GameDetailView
d = open("game-blog-web/src/views/GameDetailView.vue", "r", encoding="utf8").read()
d = d.replace(
    "style=\"color:#fff; margin-right:8px;\">",
    "style=\"color:#fff; margin-right:8px;cursor:pointer;\" @click=\"goToTag(tag.id)\">"
)
if "function goToTag" not in d:
    d = d.replace(
        "function goToGame(id: number) {",
        "function goToTag(tagId: number) { router.push(\"/tags/\" + tagId) }\n\nfunction goToGame(id: number) {"
    )
open("game-blog-web/src/views/GameDetailView.vue", "w", encoding="utf8").write(d)
print("Done")
