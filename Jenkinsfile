pipeline {
    libraries {
        lib('utils')
    }
    agent {
        label 'macos-ci'
    }
    stages {
        stage('init') {
            steps {
                script {
                    utils.run("git submodule update --init")
                }
            }
        }
        stage('dist') {
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
                    utils.run("tar -C binaries -czf binaries.tar.gz .")
                }
            }
        }
        stage("s3-upload") {
            steps {
                script {
                    withAWS(credentials: "mac-build-s3-upload-artifacts", region: "us-west-2") {
                        utils.run('''
                            aws s3 cp --no-progress binaries.tar.gz s3://${BRAVE_ARTIFACTS_S3_BUCKET}/sparkle/$(git rev-parse HEAD).tar.gz
                        ''')
                    }
                }
            }
        }
    }
}
