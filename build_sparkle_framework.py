# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from os import chdir, getcwd
from os.path import dirname, realpath
from subprocess import check_call


def main():
    out_dir = getcwd()
    sparkle_dir = dirname(realpath(__file__))
    chdir(sparkle_dir)

    # Run `git submodule update --init` to update Vendor libs (i.e. ed25519)
    check_call(['git', 'submodule', 'update', '--init'])

    out_dir_config = 'CONFIGURATION_BUILD_DIR=' + out_dir

    for target in ('Sparkle', 'BinaryDelta', 'generate_keys', 'sign_update'):
        check_call(['xcodebuild', '-target', target, '-configuration', 'Release', out_dir_config, 'build'])


if __name__ == '__main__':
    main()
