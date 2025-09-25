# 4. Unified Project Structure (통합 프로젝트 구조)

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
