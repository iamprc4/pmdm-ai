@echo off
set GIT_EDITOR=notepad
git config core.editor "notepad"
git commit --no-verify -m "Merge remote-tracking branch 'origin/main'"
git push -u origin main
pause
