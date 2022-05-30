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
                        xcodebuild -target Sparkle -configuration Release build
                        xcodebuild -target BinaryDelta -configuration Release build
                        xcodebuild -target generate_keys -configuration Release build
                        xcodebuild -target sign_update -configuration Release build
                    """)
                }
            }
        }
    }
}
