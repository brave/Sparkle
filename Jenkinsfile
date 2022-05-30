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
                    """)
                }
            }
        }
        stage('pack-binaries') {
            steps {
                script {
                    utils.run("tar czf binaries.tar.gz binaries")
                }
            }
        }
        stage("s3-upload") {
            script {
                utils.run("aws s3 cp --no-progress binaries.tar.gz s3://brave-build-deps-public/$(git rev-parse HEAD)/binaries.tar.gz")
            }
        }
}
