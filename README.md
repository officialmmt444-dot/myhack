git init
echo "# Spoof Hack (Educational Demo)" > README.md
git add README.md spoof_hack.py
git commit -m "Initial commit: harmless visual spoof tool"
# create GitHub repo via web UI or gh CLI, then push:
# example if you created repo 'spoof-hack' on GitHub:
git remote add origin git@github.com:<your-username>/spoof-hack.git
git branch -M main
git push -u origin main
