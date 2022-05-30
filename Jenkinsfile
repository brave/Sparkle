pipeline {
    libraries {
        lib('utils')
    }
    agent {
        label 'master'
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
