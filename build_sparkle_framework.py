# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import os.path
import shutil
import subprocess
import sys


def Main(args):
  out_dir = os.getcwd()
  sparkle_dir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(sparkle_dir)

  # Run `git submodule update --init` to update Vendor libs (i.e. ed25519)
  command = ['git', 'submodule', 'update', '--init']
  subprocess.run(command, check=True)

  command = ['xcodebuild', '-target', 'Sparkle', '-configuration', 'Release', 'build']
  subprocess.run(command, check=True)

  command = ['xcodebuild', '-target', 'BinaryDelta', '-configuration', 'Release', 'build']
  subprocess.run(command, check=True)

  command = ['xcodebuild', '-target', 'generate_keys', '-configuration', 'Release', 'build']
  subprocess.run(command, check=True)

  command = ['xcodebuild', '-target', 'sign_update', '-configuration', 'Release', 'build']
  subprocess.run(command, check=True)

  return 0


if __name__ == '__main__':
  sys.exit(Main(sys.argv))
