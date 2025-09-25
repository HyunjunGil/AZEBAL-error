# 5. BMad Orchestrator Architecture (BMad 오케스트레이터 아키텍처)

## 5.1 Agent System Architecture (에이전트 시스템 아키텍처)

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

## 5.2 Command Processing Architecture (명령 처리 아키텍처)

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

## 5.3 Workflow Management Architecture (워크플로우 관리 아키텍처)

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

## 5.4 Data Management Architecture (데이터 관리 아키텍처)

* **Dependency Management (의존성 관리)**
    * **File Resolution:** `.bmad-core/{type}/{name}` 형식으로 의존성 매핑
    * **Type Categories:** `tasks`, `templates`, `checklists`, `data`, `utils` 등
    * **Lazy Loading:** 명령 실행 시에만 필요한 파일 로드

* **Knowledge Base Integration (지식 베이스 통합)**
    * **KB Mode Behavior:** `*kb-mode` 호출 시 `kb-mode-interaction` 작업 사용
    * **Contextual Responses:** 모든 KB 내용을 즉시 덤프하지 않고 주제 영역 제시 후 사용자 선택 대기
    * **Focused Responses:** 집중적이고 맥락적인 응답 제공

## 5.5 Agent Transformation Architecture (에이전트 변환 아키텍처)

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
