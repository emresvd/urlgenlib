import sys

if sys.argv[-1] == "main.py":
    import urlgenlib
    print(
        urlgenlib.urlgen("https://github.com/emresvd/")
    )

if sys.argv[-1] == "clean":
    import shutil
    for i in ["build", "dist", "urlgenlib.egg-info"]:
        shutil.rmtree(i)

if sys.argv[-1] == "build":
    import os
    os.system("python setup.py sdist bdist_wheel")

if sys.argv[-1] == "upload":
    import os
    os.system("twine upload dist/*")
