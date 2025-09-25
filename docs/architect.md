## [초안] 스포츠 용품 추천 쇼핑몰 프로토타입 Fullstack Architecture

| 변경 날짜 | 버전 | 설명 | 작성자 |
| --- | --- | --- | --- |
| 2025-09-25 | 1.0 | 초기 초안 생성 (YOLO 모드) | Winston (Architect) |

## 1. High Level Architecture (상위 레벨 아키텍처)

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

## 2. Tech Stack (기술 스택)

| Category | Technology | Version | Purpose |
| --- | --- | --- | --- |
| **Frontend** | Vue.js | 3.x | 반응형 UI 개발 프레임워크 |
| **Styling** | Tailwind CSS | 3.x | 신속한 프로토타이핑을 위한 CSS 프레임워크 |
| **State Mgmt**| Pinia | 2.x | Vue의 공식 상태 관리 라이브러리 |
| **Backend** | Python | 3.10+ | 백엔드 개발 언어 |
| **API Framework**| FastAPI | 0.100+ | 고성능 Python API 프레임워크 |
| **Hosting** | Azure Static Web Apps | N/A | 프론트엔드 및 서버리스 API 통합 호스팅 |
| **CI/CD** | GitHub Actions | N/A | Azure와 연동된 자동 빌드/배포 |
| **Repo Mgmt** | npm Workspaces | 8.x+ | Monorepo 관리 |

## 3. Data Models & API Specification (데이터 모델 및 API 명세)

프로토타입 단계에서는 실제 DB 대신 Mock 데이터를 사용하므로, 데이터 구조는 TypeScript 인터페이스로 정의하여 프론트엔드와 (가상)백엔드 간의 계약으로 사용합니다.

* **TypeScript Interfaces (Mock 데이터 구조)**
    ```typescript
    interface Product {
      id: string;
      name: string;
      brand: string;
      price: number;
      imageUrl: string;
      description: string;
    }

    interface Review {
      id: string;
      author: string;
      rating: number;
      comment: string;
      videoUrl?: string;
    }
    ```
* **API Endpoints (핵심 API 엔드포인트)**
    FastAPI는 자동으로 OpenAPI (Swagger) 문서를 생성합니다. 프로토타입에서는 아래 엔드포인트만 구현합니다.

    * `GET /api/recommendations`: 사용자의 프로필 선택에 따라 `Product[]` 목록을 반환합니다.
    * `GET /api/products/{product_id}`: 특정 제품의 상세 정보(`Product`)와 관련 리뷰(`Review[]`)를 반환합니다.

## 4. Unified Project Structure (통합 프로젝트 구조)

`apps` 디렉토리 내에 프론트엔드와 백엔드 프로젝트를 분리하여 구성합니다.

```
/
├── apps/
│   ├── frontend/        # Vue.js Project
│   │   ├── public/
│   │   ├── src/
│   │   │   ├── components/
│   │   │   ├── views/
│   │   │   └── main.js
│   │   └── package.json
│   └── api/             # FastAPI Project
│       ├── app/
│       │   ├── main.py
│       │   └── routers/
│       ├── requirements.txt
├── package.json         # Monorepo Root
└── azure-static-web-apps.yml # 배포 설정 파일
```

## 5. Deployment Architecture (배포 아키텍처)

* **Strategy:** **Azure Static Web Apps**를 사용한 통합 CI/CD 전략을 사용합니다.
* **Process:**
    1.  개발자가 GitHub 리포지토리에 코드를 Push 합니다.
    2.  GitHub Actions가 자동으로 트리거됩니다.
    3.  `apps/frontend`의 Vue 프로젝트를 빌드하여 정적 파일(HTML, CSS, JS)을 생성합니다.
    4.  `apps/api`의 FastAPI 코드를 Azure Functions에 배포합니다.
    5.  빌드된 프론트엔드 파일과 배포된 API가 Azure Static Web Apps를 통해 단일 URL로 제공됩니다.