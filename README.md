# 스포츠 용품 추천 쇼핑몰 프로토타입

개인 맞춤형 스포츠 용품 추천 쇼핑몰 프로토타입입니다. Azure 배포를 목표로 하는 풀스택 웹 애플리케이션입니다.

## 🎯 프로젝트 개요

**목표**: '개인 맞춤형 스포츠 용품 추천'이라는 핵심 아이디어의 사업적 가치를 검증하는 시연 가능한 프로토타입

**타겟 사용자**: 사내 동호회 입문 직장인 (MZ세대)

**핵심 기능**:
- 개인 프로필 기반 맞춤 추천
- 신뢰성 있는 리뷰 시스템
- 직관적인 구매 경험 흐름

## 🏗️ 기술 스택

### Frontend
- **Framework**: Vue.js 3 (Composition API)
- **Styling**: Tailwind CSS v4
- **State Management**: Pinia
- **Routing**: Vue Router
- **Build Tool**: Vite

### Backend  
- **Framework**: FastAPI (Python 3.11)
- **Server**: Uvicorn
- **Data**: Mock JSON data (PostgreSQL 준비)

### Infrastructure
- **Repository**: Monorepo 구조
- **Deployment**: Microsoft Azure (Static Web Apps + Functions)

## 📁 프로젝트 구조

```
/
├── apps/
│   ├── frontend/          # Vue.js Frontend
│   │   ├── src/
│   │   │   ├── components/
│   │   │   ├── views/     # 4개 핵심 화면
│   │   │   ├── stores/    # Pinia 스토어
│   │   │   ├── services/  # API 통신
│   │   │   └── data/      # Mock 데이터
│   │   ├── package.json
│   │   └── vite.config.js
│   └── api/               # FastAPI Backend
│       ├── app/
│       │   ├── main.py
│       │   ├── models.py
│       │   ├── data.py
│       │   └── routers/
│       └── requirements.txt
├── docs/                  # 설계 문서
└── README.md
```

## 🚀 실행 방법

### 사전 요구사항
- Node.js 18+ 
- Python 3.11+
- Conda (권장)

### 1. 프로젝트 클론
```bash
git clone <repository-url>
cd azure-error
```

### 2. Backend 실행
```bash
cd apps/api

# Conda 환경 생성 (최초 1회)
conda create -n sports-api python=3.11 -y
conda activate sports-api

# 의존성 설치
pip install -r requirements.txt

# 서버 실행
uvicorn app.main:app --reload --port 8000 --host 0.0.0.0
```

### 3. Frontend 실행
```bash
cd apps/frontend

# 의존성 설치 (최초 1회)
npm install

# 개발 서버 실행
npm run dev
```

### 4. 애플리케이션 접속
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API 문서**: http://localhost:8000/docs (Swagger UI)

## 🎮 사용자 흐름

1. **프로필 선택** (`/`)
   - 스포츠 종목 선택 (테니스, 배드민턴, 축구, 농구, 러닝)
   - 스타일 선택 (캐주얼, 프로페셔널, 초보자친화, 퍼포먼스)
   - 예산 선택 (합리적, 중간, 프리미엄)

2. **추천 결과** (`/recommendations`)
   - 맞춤 추천 제품 목록
   - 필터링 및 정렬 기능

3. **제품 상세** (`/product/:id`)
   - 제품 상세 정보
   - 사용자 리뷰 (텍스트, 동영상)
   - 구매하기 버튼

4. **구매 완료** (`/purchase-complete`)
   - 주문 완료 안내
   - 피드백 수집

## 🔌 API 엔드포인트

### 제품 관련
- `GET /api/products` - 전체 제품 목록
- `GET /api/products/{product_id}` - 제품 상세 정보 + 리뷰

### 추천 관련  
- `POST /api/recommendations` - 개인화 추천
- `GET /api/recommendations/{sport}/{style}/{budget}` - 파라미터 기반 추천

### 시스템
- `GET /health` - 서버 상태 확인
- `GET /` - API 정보

## 🎨 UI/UX 특징

- **한국어 인터페이스**: 한국 사용자를 위한 친근한 언어
- **브랜드 컬러**: Primary #007BFF, Secondary #4CAF50
- **반응형 디자인**: 모바일, 태블릿, 데스크톱 지원
- **접근성**: 키보드 내비게이션, 스크린 리더 지원
- **마이크로 인터랙션**: 부드러운 애니메이션과 피드백

## 🧪 테스트

### Backend 자동 테스트 (pytest)
```bash
cd apps/api
conda activate sports-api

# 모든 테스트 실행
python -m pytest tests/ -v

# 코드 커버리지와 함께 실행
python -m pytest tests/ --cov=app --cov-report=term-missing

# 특정 테스트 파일만 실행
python -m pytest tests/test_products.py -v

# 마크된 테스트만 실행 
python -m pytest tests/ -m unit -v
```

**테스트 현황**:
- ✅ **28개 테스트** 모두 통과
- ✅ **100% 코드 커버리지** 달성
- ✅ API 엔드포인트 테스트
- ✅ 데이터 검증 테스트  
- ✅ 추천 알고리즘 로직 테스트
- ✅ 에러 처리 테스트

### Backend 수동 테스트
```bash
# Health check
curl http://localhost:8000/health

# Products API
curl http://localhost:8000/api/products

# Recommendations API
curl -X POST http://localhost:8000/api/recommendations \
  -H "Content-Type: application/json" \
  -d '{"profile": {"sport": "tennis", "style": "professional", "budget": "medium"}}'
```

### Frontend 빌드 및 테스트
```bash
cd apps/frontend
npm run build
npm run preview
```

### 통합 테스트
```bash
# 1. 백엔드 시작
cd apps/api && conda activate sports-api && uvicorn app.main:app --reload --port 8000

# 2. 프론트엔드 시작 (새 터미널)
cd apps/frontend && npm run dev

# 3. 브라우저에서 전체 플로우 테스트
# - 프로필 선택 → 추천 결과 → 제품 상세 → 구매 완료
```

## 🚢 Azure 배포 준비

### Static Web Apps 구성
1. Frontend 빌드 디렉토리: `apps/frontend/dist`
2. API 디렉토리: `apps/api`
3. 배포 설정 파일: `azure-static-web-apps.yml`

### 환경 변수
- `API_BASE_URL`: 프로덕션 API 엔드포인트
- `CORS_ORIGINS`: 허용된 도메인 목록

## 📊 Mock 데이터

현재 6개 제품 데이터 포함:
- 테니스 라켓 (Wilson, Babolat)
- 배드민턴 라켓 (Yonex)
- 러닝화 (Nike)
- 축구화 (Adidas)
- 농구화 (Jordan)

각 제품별 리뷰 데이터 및 평점 시스템 포함

## 🔧 개발 도구

### Frontend
```bash
npm run dev      # 개발 서버
npm run build    # 프로덕션 빌드
npm run preview  # 빌드 미리보기
```

### Backend
```bash
uvicorn app.main:app --reload           # 개발 모드
uvicorn app.main:app --host 0.0.0.0     # 프로덕션 모드
```

## 🐛 문제 해결

### 포트 충돌
- Frontend: 포트 3000이 사용 중이면 자동으로 3001, 3002 사용
- Backend: 포트 8000 고정, 필요시 `--port` 옵션으로 변경

### CORS 에러
- API 서버의 CORS 설정에서 Frontend URL 확인
- 개발 환경에서는 localhost:3000-3002 허용됨

### 의존성 문제
```bash
# Frontend
rm -rf node_modules package-lock.json
npm install

# Backend  
conda env remove -n sports-api
conda create -n sports-api python=3.11 -y
pip install -r requirements.txt
```

## 📝 다음 단계

- [ ] 실제 데이터베이스 연동 (PostgreSQL)
- [ ] 사용자 인증 시스템
- [ ] 결제 시스템 연동
- [ ] 관리자 페이지
- [ ] Azure 자동 배포 파이프라인
- [ ] 성능 모니터링 및 분석

## 👥 기여

1. 이슈 생성
2. Feature 브랜치 생성
3. 커밋 및 푸시
4. Pull Request 생성

## 📄 라이선스

MIT License

---

**프로토타입 버전**: 1.0.0  
**마지막 업데이트**: 2025-09-25  
**개발팀**: John (PM), Winston (Architect), Sally (UX Expert)
