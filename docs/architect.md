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

## 5. BMad Orchestrator Architecture (BMad 오케스트레이터 아키텍처)

### 5.1 Agent System Architecture (에이전트 시스템 아키텍처)

* **Core Architecture Principles (핵심 아키텍처 원칙)**
    * **Dynamic Agent Loading:** 필요할 때만 에이전트 파일을 로드하는 런타임 로딩 방식
    * **Resource Lazy Loading:** 리소스를 미리 로드하지 않고 실행 시점에 발견 및 로드
    * **Agent Transformation:** 요구사항에 따라 동적으로 전문 에이전트로 변환
    * **State Management:** 현재 상태 추적 및 다음 단계 가이드 제공

* **Agent Configuration Structure (에이전트 구성 구조)**
    ```yaml
    agent:
      name: BMad Orchestrator
      id: bmad-orchestrator
      title: BMad Master Orchestrator
      icon: 🎭
      whenToUse: Use for workflow coordination, multi-agent tasks, role switching guidance
    ```

### 5.2 Command Processing Architecture (명령 처리 아키텍처)

* **Command Resolution System (명령 해석 시스템)**
    * **Prefix Requirement:** 모든 명령은 `*` 접두사로 시작
    * **Fuzzy Matching:** 85% 신뢰도 임계값을 사용한 유연한 명령 매칭
    * **Numbered Lists:** 불확실한 경우 번호가 매겨진 선택 목록 제공
    * **Request Resolution:** 사용자 요청을 명령/의존성에 유연하게 매칭

* **Command Categories (명령 카테고리)**
    * **Core Commands:** `*help`, `*chat-mode`, `*kb-mode`, `*status`, `*exit`
    * **Agent Management:** `*agent [name]`, `*task [name]`, `*checklist [name]`
    * **Workflow Management:** `*workflow [name]`, `*workflow-guidance`, `*plan`
    * **Utility Commands:** `*yolo`, `*party-mode`, `*doc-out`

### 5.3 Workflow Management Architecture (워크플로우 관리 아키텍처)

* **Workflow Discovery System (워크플로우 발견 시스템)**
    * 런타임에 번들에서 사용 가능한 워크플로우를 동적으로 발견
    * 각 워크플로우의 목적, 옵션, 결정 지점을 이해
    * 워크플로우 구조에 기반한 명확한 질문 제공
    * 여러 옵션이 있을 때 사용자를 통한 워크플로우 선택 가이드

* **Workflow Guidance Process (워크플로우 가이드 프로세스)**
    1. 사용 가능한 모든 워크플로우를 간단한 설명과 함께 나열
    2. 워크플로우의 구조에 기반한 명확한 질문 제공
    3. 적절한 경우 상세한 워크플로우 계획 생성 제안
    4. 분기 경로가 있는 워크플로우의 경우 올바른 경로 선택 지원

### 5.4 Data Management Architecture (데이터 관리 아키텍처)

* **Dependency Management (의존성 관리)**
    * **File Resolution:** `.bmad-core/{type}/{name}` 형식으로 의존성 매핑
    * **Type Categories:** `tasks`, `templates`, `checklists`, `data`, `utils` 등
    * **Lazy Loading:** 명령 실행 시에만 필요한 파일 로드

* **Knowledge Base Integration (지식 베이스 통합)**
    * **KB Mode Behavior:** `*kb-mode` 호출 시 `kb-mode-interaction` 작업 사용
    * **Contextual Responses:** 모든 KB 내용을 즉시 덤프하지 않고 주제 영역 제시 후 사용자 선택 대기
    * **Focused Responses:** 집중적이고 맥락적인 응답 제공

### 5.5 Agent Transformation Architecture (에이전트 변환 아키텍처)

* **Transformation Process (변환 프로세스)**
    1. **Assessment:** 사용자 목표를 사용 가능한 에이전트 및 워크플로우와 비교
    2. **Recommendation:** 에이전트 전문성에 대한 명확한 매치가 있는 경우 `*agent` 명령으로 변환 제안
    3. **Project Orientation:** 프로젝트 지향적인 경우 `*workflow-guidance`로 옵션 탐색 제안
    4. **Transformation:** 에이전트 변환 시 변환 발표 및 해당 에이전트의 원칙 우선 적용

* **State Tracking (상태 추적)**
    * 현재 컨텍스트, 활성 에이전트, 진행 상황 추적
    * 명시적인 활성 페르소나 및 현재 작업 표시
    * 다음 논리적 단계로의 가이드 제공

---

## 6. Deployment Architecture (배포 아키텍처)

* **Strategy:** **Azure Static Web Apps**를 사용한 통합 CI/CD 전략을 사용합니다.
* **Process:**
    1.  개발자가 GitHub 리포지토리에 코드를 Push 합니다.
    2.  GitHub Actions가 자동으로 트리거됩니다.
    3.  `apps/frontend`의 Vue 프로젝트를 빌드하여 정적 파일(HTML, CSS, JS)을 생성합니다.
    4.  `apps/api`의 FastAPI 코드를 Azure Functions에 배포합니다.
    5.  빌드된 프론트엔드 파일과 배포된 API가 Azure Static Web Apps를 통해 단일 URL로 제공됩니다.