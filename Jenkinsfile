pipeline {
    libraries {
        lib('utils')
    }
    agent {
        label 'mac'
    }
    stages {
        stage('init-submodule') {
            steps {
                script {
                    utils.run("git submodule update --init")
                }
            }
        }
        stage('build') {
            steps {
                script {
                    utils.run("""
                        xcodebuild -target Sparkle -configuration Release CONFIGURATION_BUILD_DIR=binaries build
                        xcodebuild -target BinaryDelta -configuration Release CONFIGURATION_BUILD_DIR=binaries build
                        xcodebuild -target generate_keys -configuration Release CONFIGURATION_BUILD_DIR=binaries build
                        xcodebuild -target sign_update -configuration Release CONFIGURATION_BUILD_DIR=binaries build
                        cp bin/old_dsa_scripts/sign_update binaries/sign_update_dsa
                    """)
                }
            }
        }
        stage('pack-binaries') {
            steps {
                script {
                    utils.run("tar -C binaries czf binaries.tar.gz .")
                }
            }
        }
        stage("s3-upload") {
            steps {
                withAWS(credentials: "mac-build-s3-upload-artifacts", region: "us-west-2") {
                    sh '''
                        aws s3 cp --no-progress binaries.tar.gz s3://brave-build-deps-public/sparkle/$(git rev-parse HEAD).tar.gz
                    '''
                }
            }
        }
    }
}
