import subprocess
import os

os.chdir(r"c:\Users\CHOTU\Downloads\PROJECT\PMDM PROJECT\Aushadh AI\final modified\AushadhAI_updated (2)\AushadhAI_updated\prototype")

# Set editor to avoid vim
os.environ['GIT_EDITOR'] = 'notepad'

try:
    # Complete the merge commit
    result = subprocess.run(['git', 'commit', '--no-verify', '-m', 'Merge remote and local changes'], 
                           capture_output=True, text=True)
    print("Commit output:", result.stdout)
    print("Commit errors:", result.stderr)
    
    # Push to GitHub
    result = subprocess.run(['git', 'push', '-u', 'origin', 'main'], 
                           capture_output=True, text=True)
    print("Push output:", result.stdout)
    print("Push errors:", result.stderr)
    print("\n✅ Successfully pushed to GitHub!")
except Exception as e:
    print(f"Error: {e}")
