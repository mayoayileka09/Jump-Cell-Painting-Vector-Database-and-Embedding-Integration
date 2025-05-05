import os
import pooch

# This script clears the local pooch cache by deleting any cached Babel database files (e.g., babel.db)
# to ensure a clean state before re-fetching or reprocessing.


babel_cache = pooch.os_cache("pooch")
for file in os.listdir(babel_cache):
    if "babel.db" in file:
        os.remove(os.path.join(babel_cache, file))
        print(f"Deleted: {file}")
