c = open('game-blog-web/src/views/GameDetailView.vue', 'r', encoding='utf8').read()

# Better markdown typography
old_md = '''.markdown-body {
  line-height: 1.8;
  font-size: 15px;
}
.markdown-body h1,
.markdown-body h2,
.markdown-body h3 {
  margin: 1em 0 0.5em;
  color: #333;
}
.markdown-body h1 { font-size: 24px; }
.markdown-body h2 { font-size: 20px; }
.markdown-body h3 { font-size: 17px; }
.markdown-body p { margin: 0.5em 0; }
.markdown-body ul, .markdown-body ol { padding-left: 20px; }
.markdown-body li { margin: 0.3em 0; }
.markdown-body strong { font-weight: 600; }
.markdown-body code {
  background: #f5f5f5;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 14px;
}'''

new_md = '''.markdown-body {
  line-height: 1.9;
  font-size: 16px;
  color: var(--text-primary);
}
.markdown-body h1,
.markdown-body h2,
.markdown-body h3 {
  margin: 1.2em 0 0.6em;
  color: var(--text-primary);
  font-weight: 700;
  line-height: 1.3;
}
.markdown-body h1 { font-size: 26px; padding-bottom: 8px; border-bottom: 2px solid var(--border-color); }
.markdown-body h2 { font-size: 22px; padding-bottom: 6px; border-bottom: 1px solid var(--border-color); }
.markdown-body h3 { font-size: 18px; }
.markdown-body p { margin: 0.6em 0; }
.markdown-body ul, .markdown-body ol { padding-left: 24px; }
.markdown-body li { margin: 0.4em 0; }
.markdown-body strong { font-weight: 700; color: var(--text-primary); }
.markdown-body code {
  background: var(--glass-bg);
  padding: 3px 8px;
  border-radius: 6px;
  font-size: 14px;
  border: 1px solid var(--glass-border);
}
.markdown-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
}
.markdown-body th, .markdown-body td {
  padding: 10px 14px;
  border: 1px solid var(--border-color);
  text-align: left;
}
.markdown-body th {
  background: var(--glass-bg);
  font-weight: 600;
}'''

c = c.replace(old_md, new_md)

# Update related games section
c = c.replace(
    '.related-games { margin-bottom: 20px; }\n.related-games h2 { margin-bottom: 16px; }',
    '.related-games { margin-bottom: 28px; }\n.related-games h2 { margin-bottom: 20px; font-size: 20px; font-weight: 700; }'
)

c = c.replace(
    '.related-card { cursor: pointer; transition: transform 0.3s; margin-bottom: 16px; }\n.related-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); }',
    '.related-card { cursor: pointer; transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1); margin-bottom: 16px; border-radius: 14px !important; overflow: hidden; }\n.related-card:hover { transform: translateY(-6px); box-shadow: 0 12px 36px rgba(0,0,0,0.15) !important; }'
)

# Update detail card
c = c.replace(
    '.related-cover { width: 100%; height: 140px; object-fit: cover; }',
    '.related-cover { width: 100%; height: 140px; object-fit: cover; display: block; }'
)

open('game-blog-web/src/views/GameDetailView.vue', 'w', encoding='utf8').write(c)
print('GameDetailView updated')
