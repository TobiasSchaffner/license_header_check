//
// This Jenkinsfile configures how this project is build on Jenkins
//
// Copyright (c) 2020 Mixed Mode GmbH
//
// ALL RIGHTS RESERVED - Unauthorized copying of this file, via any medium is strictly prohibited.
//
library "pipeline-utils@stable"

pipeline {

    agent {
        label 'buildsrvmm3'
    }

    options {
        timeout(time: 30, unit: "MINUTES")
        buildDiscarder(logRotator(numToKeepStr: "15"))
        gitLabConnection('jenkins-in-gitlab-connection')
        gitlabBuilds(builds: ['build'])
    }

    stages {
        stage('Tox') {
            steps {
                sh('tox -e ALL')

                cobertura (
                    coberturaReportFile: 'artifacts/cov.xml',
                    onlyStable: true,
                    failNoReports: true,
                    failUnhealthy: true,
                    failUnstable: true,
                    autoUpdateHealth: false,
                    autoUpdateStability: false,
                    zoomCoverageChart: true,
                    maxNumberOfBuilds: 0,
                    lineCoverageTargets: '15, 15, 15',
                    conditionalCoverageTargets: '0, 0, 0',
                    classCoverageTargets: '40, 40, 40',
                    fileCoverageTargets: '40, 40, 40',
                )
            }
        }
    }

    post {
        success {
            updateGitlabCommitStatus name: 'build', state: 'success'
        }

        unstable {
            updateGitlabCommitStatus name: 'build', state: 'failed'
        }

        failure {
            updateGitlabCommitStatus name: 'build', state: 'failed'
        }

        always {
            script {
                junit 'artifacts/unittest_report.xml'
            }

            recordIssues(
                tool: flake8(pattern: 'artifacts/flake8_report.txt'),
            )

            archiveArtifacts 'artifacts/**'

            sendBuildStatusEmails()
            cleanWs()
        }
    }
}
