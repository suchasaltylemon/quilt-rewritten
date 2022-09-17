from os.path import exists

import pip

DEPENDENCIES = []


class SHSB:
    def _is_shsb(self):
        return exists("N:/.packages")  # TODO: Find a different way to check if SHSB machine. Env variable?

    def install_dependencies(self):
        if not self._is_shsb():
            return

        for dependency in DEPENDENCIES:
            pip.main(["install", dependency])
