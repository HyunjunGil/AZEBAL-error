# 1. High Level Architecture (상위 레벨 아키텍처)

* **Technical Summary (기술 요약)**
    * 본 아키텍처는 **Microsoft Azure** 플랫폼을 기반으로, **Azure Static Web Apps** 서비스를 활용하여 프론트엔드와 백엔드를 통합 배포하는 현대적인 서버리스 아키텍처를 채택합니다. 프론트엔드는 **Vue.js**로 빌드된 정적 웹 앱(SPA) 형태로 제공되며, 백엔드 API는 **Python FastAPI**를 사용하여 **Azure Functions**에서 실행됩니다. 이를 통해 인프라 관리 부담을 최소화하고, 신속한 프로토타입 개발 및 시연 목표 달성에 집중합니다.
* **Platform and Infrastructure (플랫폼 및 인프라)**
    * **Platform:** Microsoft Azure
    * **Key Services:**
        * **Azure Static Web Apps:** Vue 프론트엔드 호스팅 및 Azure Functions API 통합 관리
        * **Azure Functions:** FastAPI 백엔드 API 실행 환경
        * **GitHub Actions:** CI/CD 자동화를 통한 코드 배포
        * **Azure Database for PostgreSQL:** (향후 Phase 2용) 데이터베이스
* **Repository Structure (저장소 구조)**
    * **Structure:** Monorepo
    * **Tooling:** npm Workspaces 또는 Turborepo를 사용하여 프론트엔드와 백엔드 패키지를 관리합니다.

* **Architecture Diagram (아키텍처 다이어그램)**
    ```mermaid
    graph TD
        subgraph Internet
            U[User]
        end

        subgraph Azure
            SWA[Azure Static Web Apps]
            subgraph SWA
                V[Vue.js Frontend]
                F[Azure Functions: FastAPI]
            end
            DB[(PostgreSQL DB<br/>- Phase 2 -)]
        end

        U -- HTTPS --> V
        V -- API Request --> F
        F -- Mock Data --> V
        F -.-> DB
    ```
