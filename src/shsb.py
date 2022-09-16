import os.path

import pip

DEPENDENCIES = "beautifulsoup"


class SHSB:
    def _is_shsb(self):
        return os.path.exists("N:/.packages")  # TODO: Find a different way to check if SHSB machine. Env variable?

    def install_dependencies(self):
        if not self._is_shsb():
            return

        for dependency in DEPENDENCIES:
            pip.main(["install", dependency])
