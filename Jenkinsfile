pipeline {
    libraries {
        lib('utils')
    }
    agent {
        label 'mac'
    }
    stages {
        stage('build') {
            steps {
                script {
                    utils.run("python3 build_sparkle_framework.py")
                }
            }
        }
    }
}
