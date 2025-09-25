## [초안] 스포츠 용품 추천 쇼핑몰 프로토타입 UI/UX 명세서

| 변경 날짜 | 버전 | 설명 | 작성자 |
| --- | --- | --- | --- |
| 2025-09-25 | 1.0 | 초기 초안 생성 (YOLO 모드) | Sally (UX Expert) |

## 1. Overall UX Goals & Principles (전체 UX 목표 및 원칙)

* **Target User Personas (타겟 사용자 페르소나)**
    * PRD에 정의된 **"이제 막 운동을 시작하는 장비 입문 직장인"**을 중심으로 설계합니다. 이들은 IT에 익숙하지만, 스포츠 장비 분야에서는 초보자임을 가정합니다.
* **Usability Goals (사용성 목표)**
    * **쉬운 학습:** 처음 방문한 사용자도 5분 안에 추천받기까지의 과정을 막힘없이 완료할 수 있습니다.
    * **높은 효율성:** 최소한의 클릭과 정보 입력으로 원하는 추천 결과를 얻을 수 있습니다.
* **Design Principles (디자인 원칙)**
    1.  **명확함 우선 (Clarity over cleverness):** 화려한 기교보다 쉽고 명확한 안내를 우선합니다.
    2.  **점진적 공개 (Progressive disclosure):** 사용자에게 한 번에 하나의 과업만 제시하여 인지적 부담을 줄입니다.
    3.  **일관된 경험 (Consistent patterns):** 사용자가 예측 가능한, 익숙한 UI 패턴을 사용하여 학습 비용을 최소화합니다.
    4.  **디테일의 즐거움 (Delight in the Details):** 친근한 문구와 부드러운 마이크로 인터랙션으로 긍정적인 경험을 제공합니다.

---
## 2. Information Architecture (IA - 정보 구조)

* **Site Map (프로토타입 화면 흐름)**
    * 프로토타입은 사용자가 핵심 가치를 경험하는 단일 경로에 집중합니다.

    ```mermaid
    graph TD
        A[시작: 프로필 선택] --> B[추천 결과 목록]
        B --> C{제품 선택}
        C --> D[제품 상세 및 리뷰]
        D --> E[가상 구매 완료]
    ```

---
## 3. User Flows (사용자 흐름)

* **핵심 흐름: 개인 맞춤 제품 추천 및 (가상)구매**
    * **User Goal:** 나에게 맞는 스포츠 용품을 추천받아 구매(처럼 보이는) 과정을 완료한다.
    * **Entry Point:** 프로토타입 메인 페이지 (프로필 선택 화면)
    * **Success Criteria:** 사용자가 막힘없이 '가상 구매 완료' 화면까지 도달한다.
    * **Flow Diagram:**
    ```mermaid
    sequenceDiagram
        participant User
        participant System

        User->>System: 프로필 선택 화면 진입
        User->>System: 자신의 플레이 스타일, 예산 등 선택
        System-->>User: 선택에 맞는 추천 결과 목록 표시 (Mock Data)
        User->>System: 마음에 드는 제품 클릭
        System-->>User: 제품 상세 및 리뷰 페이지 표시 (Mock Data)
        User->>System: '구매하기' 버튼 클릭
        System-->>User: '주문이 완료되었습니다'와 유사한 화면 표시
    ```

---
## 4. Wireframes & Mockups (와이어프레임 및 목업)

* **Primary Design Files:** 상세 디자인은 Figma와 같은 별도의 디자인 툴에서 진행될 것을 권장합니다.
* **Key Screen Layouts (핵심 화면 레이아웃):**
    * **프로필 선택:** 사용자가 쉽고 재미있게 자신의 성향을 선택할 수 있는 카드형 UI.
    * **추천 결과:** 추천된 제품들이 명확하게 비교될 수 있는 그리드 또는 리스트 뷰.
    * **제품 상세:** 리뷰(텍스트/영상) 콘텐츠가 강조되고, 제품 스펙과 가격 정보가 명확히 보이는 레이아웃.

---
## 5. Branding & Style Guide (브랜딩 및 스타일 가이드)

* **Color Palette (색상):**
    * **Primary:** `#007BFF` (신뢰감을 주는 파란색 계열)
    * **Secondary:** `#4CAF50` (활동적인 느낌의 녹색 계열)
    * **Neutral:** `#F8F9FA` (배경), `#6C757D` (본문 텍스트), `#212529` (제목)
* **Typography (글꼴):**
    * **Font Family:** Pretendard 또는 SUIT (가독성이 높고 현대적인 느낌의 한글 폰트)
    * **Scale:** H1(32px), H2(24px), Body(16px) 등 명확한 위계를 가진 폰트 스케일 적용

---
## 6. Next Steps (다음 단계)

* 이 UI/UX 명세서를 기반으로 **아키텍트(Architect)가 기술 아키텍처 설계를 시작**할 수 있습니다.
* 아키텍처 설계와 동시에, 디자이너는 이 명세서를 바탕으로 상세한 시각 디자인(Visual Design) 작업을 진행할 수 있습니다.