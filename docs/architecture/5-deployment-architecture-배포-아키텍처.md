# 5. Deployment Architecture (배포 아키텍처)

* **Strategy:** **Azure Static Web Apps**를 사용한 통합 CI/CD 전략을 사용합니다.
* **Process:**
    1.  개발자가 GitHub 리포지토리에 코드를 Push 합니다.
    2.  GitHub Actions가 자동으로 트리거됩니다.
    3.  `apps/frontend`의 Vue 프로젝트를 빌드하여 정적 파일(HTML, CSS, JS)을 생성합니다.
    4.  `apps/api`의 FastAPI 코드를 Azure Functions에 배포합니다.
    5.  빌드된 프론트엔드 파일과 배포된 API가 Azure Static Web Apps를 통해 단일 URL로 제공됩니다.