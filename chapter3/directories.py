from pathlib import Path

path = Path("chapter3")
for file in  (path.glob("*.py")):
    print(file)

#exist = path exist
#rmdir = remove directory
#mkdir = create directory