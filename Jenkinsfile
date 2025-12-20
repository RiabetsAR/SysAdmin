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
            }
        }
        stage('Test DEB in Docker') {
            steps {
                sh '''
                DEB_PATH=$(find /var/jenkins_home/workspace/Pipeline -name "*.deb" | head -n 1)
                echo "Found DEB at: $DEB_PATH"
                
                docker run --rm -v /var/jenkins_home/workspace:/data ubuntu:22.04 bash -c "
                apt-get update && 
                dpkg -i /data/Pipeline/../etc-files_1.0-1_amd64.deb || apt-get install -fy
                /usr/bin/etc-files
                "
                '''
            }
        }
        stage('Test RPM in Docker') {
            steps {
                sh '''
                docker run --rm -v $(pwd)/rpmbuild/RPMS/noarch:/apps fedora:latest bash -c "
                dnf install -y /apps/etc-files-1.0-1.noarch.rpm
                /usr/bin/etc-files
                "
                '''
            }
        }
    }
}
