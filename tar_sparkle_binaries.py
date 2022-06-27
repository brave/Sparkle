import os
import os.path
import sys
import tarfile


def main():
    with tarfile.open('sparkle_binaries.tar.gz', 'w:gz') as tar:
        for f in sys.argv[1:]:
            tar.add(f)
        sparkle_src_dir = os.path.dirname(os.path.realpath(__file__))
        sign_update_dsa = os.path.join(sparkle_src_dir, 'bin',
                                       'old_dsa_scripts', 'sign_update')
        tar.add(sign_update_dsa, arcname='sign_update_dsa')


if __name__ == '__main__':
    main()
