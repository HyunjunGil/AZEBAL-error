# 6. BMad Orchestrator Integration (BMad 오케스트레이터 통합)

## 6.1 Agent Command Interface (에이전트 명령 인터페이스)

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

## 6.2 User Experience Requirements (사용자 경험 요구사항)

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

## 6.3 Workflow Integration (워크플로우 통합)

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
