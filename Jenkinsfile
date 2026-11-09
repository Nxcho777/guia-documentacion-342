// Pipeline educativo para la Guia 3.4.2 de Ciberseguridad en desarrollo.
// En Jenkins configure el trabajo como "Pipeline script from SCM".
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        // Primera ejecucion: false para validar sin credenciales de escritura.
        // Para guardar los cambios EN GITHUB cambie a 'true' y agregue
        // la credencial github-docs-token (usuario + token) en Jenkins.
        PUSH_DOCS = 'true'
        TARGET_BRANCH = 'main'
        // Si el correo saliente de Jenkins esta configurado, escriba aqui su email.
        NOTIFY_EMAIL = ''
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                    set -eu
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r requirements.txt
                    .venv/bin/python -m compileall -q app.py
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    set -eu
                    mkdir -p reports
                    .venv/bin/python -m pytest -q --junitxml=reports/pytest.xml
                '''
            }
        }

        stage('Generate Documentation') {
            steps {
                sh '''
                    set -eu
                    doxygen Doxyfile
                    test -s docs/html/index.html
                '''
            }
        }

        stage('Version Control') {
            steps {
                sh '''
                    set -eu
                    git config user.name "Jenkins CI"
                    git config user.email "jenkins-ci@users.noreply.github.com"
                    git add docs/html
                    if git diff --cached --quiet; then
                        echo "Sin cambios nuevos en la documentacion."
                    else
                        git commit -m "docs: actualizar documentacion Doxygen [skip ci]"
                    fi
                    git log -1 --oneline
                '''
                script {
                    if (env.PUSH_DOCS == 'true') {
                        withCredentials([gitUsernamePassword(
                            credentialsId: 'github-docs-token',
                            gitToolName: 'Default'
                        )]) {
                            sh 'git push origin HEAD:${TARGET_BRANCH}'
                        }
                    } else {
                        echo 'Push remoto desactivado: se actualizo el historial Git local de Jenkins.'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                // Entorno de ensayo temporal dentro del workspace de Jenkins.
                // No publica la aplicacion en un servidor externo.
                sh '''
                    set -eu
                    mkdir -p staging
                    cp app.py requirements.txt staging/
                    cp -r docs/html staging/docs
                    .venv/bin/python - <<'PY'
from app import app
with app.test_client() as client:
    assert client.get('/health').status_code == 200
    assert client.get('/hello?name=Jenkins').get_data(as_text=True) == 'Hello, Jenkins!'
print('Smoke test del despliegue temporal: OK')
PY
                '''
            }
        }
    }

    post {
        always {
            junit testResults: 'reports/pytest.xml', allowEmptyResults: true
            archiveArtifacts artifacts: 'docs/html/**,staging/**', allowEmptyArchive: true, fingerprint: true
        }
        success {
            echo 'Pipeline completado. Guardar capturas de las 5 etapas y sus evidencias.'
        }
        failure {
            echo 'ALERTA: pipeline fallido. Revisar Console Output para identificar la etapa.'
            script {
                if (env.NOTIFY_EMAIL?.trim()) {
                    mail(
                        to: env.NOTIFY_EMAIL,
                        subject: "Fallo en Jenkins: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                        body: "La ejecucion fallo. Revisar: ${env.BUILD_URL}console"
                    )
                }
            }
        }
    }
}
