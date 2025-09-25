## [초안] 스포츠 용품 추천 쇼핑몰 프로토타입 PRD (제품 요구사항 정의서)

| 변경 날짜 | 버전 | 설명 | 작성자 |
| --- | --- | --- | --- |
| 2025-09-25 | 1.0 | 초기 초안 생성 (YOLO 모드) | John (PM) |

## 1. Goals and Background Context (목표 및 배경)

* **Goals (목표)**
    1.  '개인 맞춤형 스포츠 용품 추천'이라는 핵심 아이디어의 사업적 가치를 검증한다.
    2.  Azure에 배포된 시연 가능한 프로토타입을 통해, 내부 이해관계자의 승인을 얻어 실제 제품 개발 단계를 진행한다.
* **Background Context (배경)**
    * 기존 쇼핑몰의 정보 과잉과 신뢰도 부족 문제를 해결하기 위해, '사내 동호회 입문 직장인'을 핵심 타겟으로 설정한다. Mock 데이터를 활용한 인터랙티브 프로토타입을 개발하여, '친근한 리뷰'와 '간단한 맞춤 추천' 경험을 제공함으로써 핵심 컨셉의 시장성을 검증하는 것을 목표로 한다.

---
## 2. Requirements (요구사항)

* **Functional (기능 요구사항)**
    * FR1: 사용자는 개인 프로필(선호 스포츠, 스타일 등)을 선택할 수 있다.
    * FR2: 시스템은 선택된 프로필에 따라 미리 정의된 Mock 데이터를 기반으로 추천 제품 목록을 화면에 표시한다.
    * FR3: 사용자는 추천된 제품을 클릭하여 Mock 데이터로 구성된 상세 정보 및 리뷰(텍스트, 영상) 페이지를 조회할 수 있다.
    * FR4: 사용자는 상품 상세 페이지에서 '구매하기'와 유사한 버튼을 통해, 실제 결제는 이루어지지 않는 구매 완료 화면까지의 흐름을 경험할 수 있다.
* **Non-Functional (비기능 요구사항)**
    * NFR1: 프로토타입은 반드시 Microsoft Azure 플랫폼에 배포되어야 한다.
    * NFR2: 사용자가 실제 서비스처럼 느낄 수 있도록, 페이지 전환 및 상호작용은 2초 이내에 반응해야 한다.

---
## 3. User Interface Design Goals (UI 디자인 목표)

* **Overall UX Vision (전체 UX 비전)**
    * 타겟 고객인 MZ세대 직장인에게 어필할 수 있는, 간결하고 직관적인 디자인을 추구한다. '친한 친구가 추천해주는 듯한' 친근하고 신뢰감 있는 톤앤매너를 유지한다.
* **Core Screens and Views (핵심 화면)**
    * 개인 프로필 선택 화면
    * 추천 결과 목록 화면
    * 제품 상세 및 리뷰 조회 화면
    * (가상)구매 완료 화면

---
## 4. Technical Assumptions (기술 가정)

* **Repository Structure:** Monorepo
* **Frontend:** Vue.js
* **Backend:** Python FastAPI
* **Database:** PostgreSQL (실제 DB 연동은 없으나, 향후 확장성을 고려한 모델 설계)
* **Hosting/Infrastructure:** Microsoft Azure

---
## 5. Epic and Story Structure (에픽 및 스토리 구조)

프로토타입 개발 전체를 하나의 에픽으로 구성합니다.

#**Epic 1: 핵심 컨셉 검증 프로토타입 개발**

* **Epic Goal:** '개인 맞춤 추천'과 '신뢰성 있는 리뷰'라는 핵심 가치를 시연할 수 있는, Azure에 배포된 인터랙티브 프로토타입을 완성한다.

* **Stories:**
    * **Story 1.1: 프로젝트 초기 설정**
        * As a 개발팀, I want Monorepo 구조 설정 및 Vue(Frontend), FastAPI(Backend) 기본 프로젝트를 생성하여, 개발을 시작할 수 있는 환경을 구축한다.
    * **Story 1.2: Mock 데이터 및 모델 정의**
        * As a 개발팀, I want 프로토타입에 사용할 제품, 리뷰, 추천 결과 등 Mock 데이터 구조를 정의하고 JSON 파일 형태로 생성하여, 화면에 표시할 데이터를 확보한다.
    * **Story 1.3: 추천 흐름 UI 개발**
        * As a 사용자, I want 개인 프로필(스타일, 예산 등)을 선택하고, 그 결과에 따른 Mock 추천 제품 목록을 화면에서 확인할 수 있다.
    * **Story 1.4: 콘텐츠 조회 UI 개발**
        * As a 사용자, I want 추천된 제품을 클릭하여, Mock 데이터로 채워진 상세 정보와 리뷰(텍스트, 영상) 콘텐츠를 볼 수 있다.
    * **Story 1.5: (가상)구매 흐름 UI 개발**
        * As a 사용자, I want 구매 버튼을 눌러, 실제 결제는 없지만 구매가 완료되었다는 화면까지의 흐름을 경험할 수 있다.
    * **Story 1.6: Azure 배포 및 시연 환경 구축**
        * As a 개발팀, I want 완성된 프로토타입을 Azure에 배포하여, 외부에서 접속 가능한 시연용 URL을 확보한다.

---
## 6. BMad Orchestrator Integration (BMad 오케스트레이터 통합)

### 6.1 Agent Command Interface (에이전트 명령 인터페이스)

* **Command Structure (명령 구조)**
    * 모든 명령은 `*` 접두사로 시작 (예: `*help`, `*agent`, `*workflow`)
    * 사용자에게 명령 사용법을 명확히 안내하는 것이 중요
    * 번호가 매겨진 선택 목록을 통해 사용자 경험 향상

* **Core Commands (핵심 명령)**
    * `*help`: 사용 가능한 에이전트 및 워크플로우 가이드 표시
    * `*chat-mode`: 상세한 지원을 위한 대화 모드 시작
    * `*kb-mode`: 전체 BMad 지식 베이스 로드
    * `*status`: 현재 컨텍스트, 활성 에이전트, 진행 상황 표시
    * `*exit`: BMad로 돌아가거나 세션 종료

* **Agent & Task Management (에이전트 및 작업 관리)**
    * `*agent [name]`: 전문 에이전트로 변환 (이름 없으면 목록 표시)
    * `*task [name]`: 특정 작업 실행 (에이전트 필요)
    * `*checklist [name]`: 체크리스트 실행 (에이전트 필요)

### 6.2 User Experience Requirements (사용자 경험 요구사항)

* **Command Interface UX (명령 인터페이스 UX)**
    * 명령어는 직관적이고 기억하기 쉬워야 함
    * 도움말은 명확하고 구조화되어야 함
    * 에이전트 전환은 매끄럽고 명확해야 함

* **Help Display Template (도움말 표시 템플릿)**
    ```
    === BMad Orchestrator Commands ===
    모든 명령은 * (별표)로 시작해야 함

    핵심 명령:
    *help ............... 이 가이드 표시
    *chat-mode .......... 상세한 지원을 위한 대화 모드
    *kb-mode ............ 전체 BMad 지식 베이스 로드
    *status ............. 현재 컨텍스트, 활성 에이전트, 진행 상황 표시
    *exit ............... BMad로 돌아가거나 세션 종료

    에이전트 및 작업 관리:
    *agent [name] ....... 전문 에이전트로 변환 (이름 없으면 목록)
    *task [name] ........ 특정 작업 실행 (에이전트 필요)
    *checklist [name] ... 체크리스트 실행 (에이전트 필요)
    ```

### 6.3 Workflow Integration (워크플로우 통합)

* **Workflow Commands (워크플로우 명령)**
    * `*workflow [name]`: 특정 워크플로우 시작 (이름 없으면 목록)
    * `*workflow-guidance`: 맞는 워크플로우 선택을 위한 개인화된 도움
    * `*plan`: 시작 전 상세한 워크플로우 계획 생성
    * `*plan-status`: 현재 워크플로우 계획 진행 상황 표시
    * `*plan-update`: 워크플로우 계획 상태 업데이트

* **Agent Transformation Requirements (에이전트 변환 요구사항)**
    * 사용자 요구사항에 맞는 최적의 에이전트 추천
    * 에이전트 전환 시 명확한 안내 제공
    * 현재 상태 추적 및 다음 단계 가이드

---

## 7. Next Steps (다음 단계)

* **UX Expert Prompt (UX 전문가에게)**
    * 이 PRD를 기반으로, Story 1.3, 1.4, 1.5에 해당하는 핵심 화면들에 대한 와이어프레임 및 UI/UX 명세서 작성을 시작해주세요. MZ세대 직장인 타겟에 맞는 친근하고 직관적인 디자인이 필요합니다.
* **Architect Prompt (아키텍트에게)**
    * 이 PRD에 명시된 기술 스택(Vue, FastAPI, Monorepo)과 Azure 배포 목표를 바탕으로, 각 Story를 구현하기 위한 상세 기술 아키텍처 설계를 시작해주세요. 특히, 프론트엔드와 백엔드 간의 (가상) API 통신 방식과 Azure 배포 전략에 대한 정의가 필요합니다.