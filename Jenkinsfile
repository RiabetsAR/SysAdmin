pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build Packages') {
            steps {
                sh 'chmod +x debian/rules'
                sh 'dpkg-buildpackage -us -uc'
                
                sh 'dos2unix rpm/etc-files.spec'
                sh 'mkdir -p rpmbuild/SOURCES rpmbuild/SPECS'
                sh 'cp rpm/etc-files.spec rpmbuild/SPECS/ && cp rpm/etc-files-1.0.tar.gz rpmbuild/SOURCES/'
                sh 'rpmbuild --define "_topdir $(pwd)/rpmbuild" -ba rpmbuild/SPECS/etc-files.spec'
                
                sh 'mkdir -p artifacts'
                sh 'cp ../etc-files_1.0-1_amd64.deb artifacts/ || true'
                sh 'cp rpmbuild/RPMS/noarch/etc-files-1.0-1.noarch.rpm artifacts/ || true'
            }
        }
        stage('Test DEB') {
            steps {
                sh '''
                ID=$(docker run -d ubuntu:22.04 sleep infinity)
                docker cp artifacts/etc-files_1.0-1_amd64.deb $ID:/tmp/package.deb
                docker exec $ID bash -c "apt-get update && apt-get install -y /tmp/package.deb && /usr/bin/script.sh"
                docker rm -f $ID
                '''
            }
        }
        stage('Test RPM') {
            steps {
                sh '''
                ID=$(docker run -d fedora:latest sleep infinity)
                docker cp artifacts/etc-files-1.0-1.noarch.rpm $ID:/tmp/package.rpm
                docker exec $ID bash -c "dnf install -y /tmp/package.rpm && /usr/bin/script.sh"
                docker rm -f $ID
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'artifacts/*.*', fingerprint: true
        }
    }
}
