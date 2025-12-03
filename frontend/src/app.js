# Ensure branch (use existing branch or switch to fix branch)
git checkout -b fix/frontend-app || git checkout fix/frontend-app

# Create App.js (minimal component)
mkdir -p frontend/src
cat > frontend/src/App.js <<'JS'
import React from "react";

export default function App() {
  return (
    <div style={{ fontFamily: "system-ui, sans-serif", padding: 24 }}>
      <h1>Final Portfolio</h1>
      <p>Your React app is mounted and ready.</p>
    </div>
  );
}
JS

# Ensure index.css exists (optional but recommended)
cat > frontend/src/index.css <<'CSS'
html, body, #root {
  height: 100%;
  margin: 0;
  padding: 0;
  background: #fff;
  color: #111;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
}
CSS

# Show small tree to confirm files exist
echo "Files created:"
ls -la frontend/src | sed -n '1,200p'

# Stage, commit, and push
git add frontend/src/App.js frontend/src/index.css
git commit -m "fix(frontend): add missing App.js and index.css for build"
git push --set-upstream origin fix/frontend-app
