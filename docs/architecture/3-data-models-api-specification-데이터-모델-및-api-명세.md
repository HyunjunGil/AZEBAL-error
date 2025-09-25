# 3. Data Models & API Specification (데이터 모델 및 API 명세)

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
