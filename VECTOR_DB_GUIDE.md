# Vector Database Setup Guide

## Overview

이 시스템은 ChromaDB를 로컬 파일 시스템에 영구 저장소로 사용합니다. 
모든 벡터 데이터는 `.claude/workspace/memory/vector_db/` 디렉토리에 저장됩니다.

## 설치

```bash
# ChromaDB 설치
pip install chromadb sentence-transformers

# 또는 requirements.txt 사용
pip install -r requirements.txt
```

## 설정

### 1. 환경 변수 설정

`.env` 파일을 생성하고 다음 내용을 추가:

```bash
# Vector Database Configuration
VECTOR_DB_TYPE=chromadb
VECTOR_DB_PATH=.claude/workspace/memory/vector_db
EMBEDDING_MODEL=all-MiniLM-L6-v2
```

### 2. 데이터베이스 초기화

```bash
# 자동 초기화 (시스템 시작 시)
python system_manager.py status

# 또는 직접 초기화
python vector_db_manager.py init
```

## 사용 방법

### Python API 사용

```python
from vector_db_manager import VectorDBManager

# DB 매니저 초기화
db = VectorDBManager()

# 컬렉션 생성
collection = db.create_collection("research_papers")

# 문서 추가
db.add_documents(
    collection_name="research_papers",
    documents=[
        "Vision Transformers for fMRI analysis...",
        "Graph Neural Networks for brain connectivity..."
    ],
    metadatas=[
        {"source": "arxiv", "year": 2024},
        {"source": "nature", "year": 2023}
    ]
)

# 검색
results = db.query_documents(
    collection_name="research_papers",
    query_texts=["transformer for neuroimaging"],
    n_results=5
)

print(results)
```

### CLI 사용

```bash
# 컬렉션 목록 보기
python vector_db_manager.py list

# 컬렉션 생성
python vector_db_manager.py create --name literature_review

# 컬렉션 통계
python vector_db_manager.py stats --name literature_review

# 백업 생성
python vector_db_manager.py backup

# 특정 경로에 백업
python vector_db_manager.py backup --path ./backups/my_backup

# 백업 복원
python vector_db_manager.py restore --path ./backups/my_backup

# 컬렉션 내보내기 (JSON)
python vector_db_manager.py export --name literature_review --path ./export.json

# 컬렉션 가져오기
python vector_db_manager.py import --path ./export.json --name new_collection

# 데이터베이스 리셋 (주의!)
python vector_db_manager.py reset
```

## 파일 구조

```
.claude/workspace/memory/
├── vector_db/                    # ChromaDB 로컬 저장소
│   ├── chroma.sqlite3           # 메인 데이터베이스 파일
│   ├── [collection_id]/         # 각 컬렉션의 데이터
│   │   ├── data_level0.bin
│   │   ├── header.bin
│   │   ├── index_metadata.pickle
│   │   └── length.bin
│   └── ...
│
└── backups/                      # 백업 디렉토리
    ├── vectordb_20250101_120000/
    │   ├── vector_db/
    │   └── metadata.json
    └── ...
```

## Agent 통합

### Hypothesis Engine에서 사용

```python
# Literature review 저장
@neurolit-agent가 논문 검색 후:
1. 논문 내용을 vector_db의 "neuroscience_papers" 컬렉션에 저장
2. 메타데이터 (DOI, 저자, 연도) 함께 저장

# 가설 생성 시 참조
@evolution-agent가 가설 진화 시:
1. vector_db에서 관련 논문 검색
2. 유사한 이전 가설 검색
3. 컨텍스트로 활용
```

### Forge에서 사용

```python
# 코드 스니펫 저장
@pytorch-dev-agent가 모델 구현 후:
1. 코드를 "code_snippets" 컬렉션에 저장
2. 모델 아키텍처, 성능 메트릭 메타데이터 포함

# 재사용
@hypertune-agent가 최적화 시:
1. 이전 실험 결과 검색
2. 유사한 설정의 하이퍼파라미터 참조
```

### Scribe에서 사용

```python
# 참고문헌 관리
@biblio-agent:
1. 인용한 논문을 "citations" 컬렉션에 저장
2. BibTeX 정보와 함께 저장
3. 중복 방지 및 빠른 검색
```

## 데이터 백업 전략

### 자동 백업 (권장)

```bash
# 매일 자동 백업 스크립트
#!/bin/bash
DATE=$(date +%Y%m%d)
python vector_db_manager.py backup --path ./backups/auto_$DATE
```

### 프로젝트 완료 시

```bash
# 프로젝트 아카이브와 함께 백업
python system_manager.py archive --project "my-research"
python vector_db_manager.py backup --path .claude/workspace/archive/[project]/vectordb
```

## 성능 최적화

### 대용량 문서 처리

```python
# 배치 처리 사용
batch_size = 100
for i in range(0, len(documents), batch_size):
    batch = documents[i:i+batch_size]
    db.add_documents(
        collection_name="large_corpus",
        documents=batch,
        metadatas=metadatas[i:i+batch_size]
    )
```

### 검색 성능

```python
# 메타데이터 필터 사용
results = db.query_documents(
    collection_name="papers",
    query_texts=["transformer architecture"],
    n_results=10,
    where={"year": {"$gte": 2023}}  # 2023년 이후만
)
```

## 문제 해결

### DB 파일이 생성되지 않는 경우

```bash
# 1. 디렉토리 권한 확인
ls -la .claude/workspace/memory/

# 2. 수동으로 디렉토리 생성
mkdir -p .claude/workspace/memory/vector_db

# 3. DB 재초기화
python vector_db_manager.py init
```

### 손상된 DB 복구

```bash
# 1. 백업에서 복원
python vector_db_manager.py restore --path ./backups/latest

# 2. 또는 DB 리셋 후 재구축
python vector_db_manager.py reset
# 그 다음 컬렉션 재생성
```

### 용량 관리

```bash
# DB 크기 확인
du -sh .claude/workspace/memory/vector_db/

# 불필요한 컬렉션 삭제
python vector_db_manager.py delete --name old_collection

# 백업 정리 (30일 이상 된 것)
find .claude/workspace/memory/backups/ -mtime +30 -type d -exec rm -rf {} +
```

## 시스템 상태 확인

```bash
# 전체 시스템 상태 (Vector DB 포함)
python system_manager.py vectordb

# 출력 예시:
{
  "initialized": true,
  "path": "/path/to/.claude/workspace/memory/vector_db",
  "collections": 3,
  "collection_names": [
    "neuroscience_papers",
    "code_snippets",
    "citations"
  ],
  "size_mb": 45.67
}
```

## 모범 사례

1. **정기적 백업**: 중요한 연구 데이터는 주기적으로 백업
2. **명확한 컬렉션 이름**: 용도를 알 수 있는 이름 사용
3. **메타데이터 활용**: 검색 성능 향상을 위해 충분한 메타데이터 포함
4. **주기적 정리**: 불필요한 컬렉션은 삭제하여 용량 관리
5. **버전 관리**: 중요한 변경 전 백업 생성

## 고급 사용

### 커스텀 임베딩 모델

```python
from sentence_transformers import SentenceTransformer

# 커스텀 모델 사용
model = SentenceTransformer('all-mpnet-base-v2')

def custom_embedding(texts):
    return model.encode(texts).tolist()

collection = db.create_collection(
    name="custom_embeddings",
    embedding_function=custom_embedding
)
```

### 다중 컬렉션 동시 검색

```python
# 여러 컬렉션에서 동시 검색
collections = ["papers_2023", "papers_2024", "papers_2025"]
all_results = []

for col in collections:
    results = db.query_documents(
        collection_name=col,
        query_texts=["attention mechanism"],
        n_results=5
    )
    all_results.append(results)

# 결과 병합 및 정렬
# (거리 기반으로 정렬)
```

## 참고 자료

- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [Vector Database Best Practices](https://www.pinecone.io/learn/vector-database/)

## 지원

문제가 있는 경우:
1. `python vector_db_manager.py list`로 상태 확인
2. 로그 파일 확인: `.claude/workspace/system.log`
3. 백업 복원 시도
4. GitHub Issues에 문제 보고
