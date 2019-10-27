pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image '0x22b8/untilmybirthday'
                }
            }
            steps {
                sh 'python -m py_compile UntilTheBirthday/UntilMyBirthday.py UntilTheBirthday/delta.py'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml UntilTheBirthday/test_untilMyBirthday.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-linux:python2'
                }
            }
            steps {
                sh 'pyinstaller --onefile UntilTheBirthday/UntilMyBirthday.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/UntilMyBirthday'
                }
            }
        }
    }
}
