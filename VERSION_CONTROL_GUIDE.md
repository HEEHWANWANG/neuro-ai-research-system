# VersionControl Agent Setup Guide

## Overview

VersionControl Agent는 Git 및 GitHub을 통한 코드 버전 관리를 자동화합니다.
연구 코드의 체계적인 관리와 협업을 지원합니다.

## 사전 요구사항

### 1. Git 설치

```bash
# macOS
brew install git

# Ubuntu/Debian
sudo apt-get install git

# 버전 확인
git --version
```

### 2. Git 글로벌 설정

```bash
# 사용자 정보 설정
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 기본 브랜치 이름 설정
git config --global init.defaultBranch main

# 설정 확인
git config --list
```

### 3. GitHub CLI 설치 (선택사항, 추천)

```bash
# macOS
brew install gh

# Ubuntu/Debian
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# 인증
gh auth login
```

### 4. SSH 키 설정 (추천)

```bash
# SSH 키 생성
ssh-keygen -t ed25519 -C "your.email@example.com"

# SSH 에이전트 시작
eval "$(ssh-agent -s)"

# SSH 키 추가
ssh-add ~/.ssh/id_ed25519

# 공개 키 복사
cat ~/.ssh/id_ed25519.pub

# GitHub에 공개 키 등록
# https://github.com/settings/keys
```

## 환경 변수 설정

### `.env` 파일 편집

```bash
# GitHub Configuration
GITHUB_TOKEN=ghp_your_personal_access_token_here
GITHUB_USERNAME=your_username
GITHUB_DEFAULT_REPO=your_username/neuro-ai-research
GIT_USER_NAME=Your Name
GIT_USER_EMAIL=your.email@example.com
```

### GitHub Personal Access Token 생성

1. GitHub > Settings > Developer settings > Personal access tokens > Tokens (classic)
2. "Generate new token" 클릭
3. 권한 선택:
   - `repo` (전체)
   - `workflow`
   - `admin:org` (조직 사용 시)
4. 생성된 토큰을 `.env`의 `GITHUB_TOKEN`에 저장

## 저장소 초기화

### 신규 프로젝트

```bash
# 1. 로컬 Git 저장소 초기화
cd /path/to/neuro-ai-research-system
git init

# 2. 원격 저장소 연결 (GitHub에 미리 생성된 경우)
git remote add origin git@github.com:username/neuro-ai-research.git

# 3. 초기 커밋
git add .
git commit -m "feat: initial project setup"
git push -u origin main
```

### 기존 저장소

```bash
# 저장소 클론
git clone git@github.com:username/neuro-ai-research.git
cd neuro-ai-research
```

## Agent 사용 방법

### 시나리오 1: 새로운 기능 개발

```bash
# Supervisor를 통해 요청
@supervisor
"fMRI 데이터 로더 구현을 시작하고 싶어요"

# Supervisor가 자동으로:
1. @forge-coordinator 호출
2. @versioncontrol-agent가 브랜치 생성:
   - git checkout -b feature/fmri-dataloader
3. @datawrangler-agent가 코드 작성
4. @versioncontrol-agent가 커밋:
   - git add src/data/fmri_loader.py
   - git commit -m "feat: implement fMRI data loader"
5. @versioncontrol-agent가 푸시:
   - git push origin feature/fmri-dataloader
```

### 시나리오 2: 실험 결과 커밋

```bash
@supervisor
"실험 결과를 저장하고 커밋해줘"

# VersionControl Agent 수행:
1. 실험 결과 파일 확인
2. git add experiments/results/*
3. git commit -m "feat: add baseline experiment results"
4. git push
```

### 시나리오 3: Pull Request 생성

```bash
@versioncontrol-agent
"feature/fmri-dataloader 브랜치를 main에 병합하기 위한 PR을 생성해줘"

# Agent 수행:
1. 변경사항 요약 생성
2. gh pr create --title "Add fMRI data loader" \
                --body "Implements efficient fMRI data loading with preprocessing"
3. PR URL 반환
```

### 시나리오 4: 특정 버전으로 롤백

```bash
@versioncontrol-agent
"이전 실험 코드로 돌아가고 싶어. v1.2.0 태그로 이동해줘"

# Agent 수행:
1. git fetch --tags
2. git checkout v1.2.0
3. 현재 HEAD 위치 보고
```

## 브랜치 전략

### Gitflow 방식 (기본)

```
main (production-ready)
  └─ develop (integration)
       ├─ feature/new-feature
       ├─ feature/another-feature
       └─ bugfix/fix-issue

hotfix/critical-fix → main
```

### 브랜치 명명 규칙

```
feature/[description]    # 새로운 기능
  예: feature/vit-model
      feature/add-attention-mechanism

bugfix/[description]     # 버그 수정
  예: bugfix/fix-data-loader
      bugfix/memory-leak

hotfix/[description]     # 긴급 수정
  예: hotfix/critical-crash

experiment/[description] # 실험적 코드
  예: experiment/try-gnn
      experiment/test-new-architecture
```

## 커밋 메시지 규칙

### Conventional Commits

```
<type>: <subject>

[optional body]

[optional footer]
```

### Type 종류

```
feat:      새로운 기능 추가
fix:       버그 수정
docs:      문서 변경
style:     코드 포맷팅 (기능 변경 없음)
refactor:  코드 리팩토링
test:      테스트 추가/수정
chore:     빌드/설정 변경
perf:      성능 개선
```

### 예시

```bash
# 좋은 예
git commit -m "feat: implement ViT model for fMRI analysis"
git commit -m "fix: resolve memory leak in data loader"
git commit -m "docs: update installation guide"

# 나쁜 예
git commit -m "update"
git commit -m "fixed stuff"
git commit -m "asdf"
```

## 파일 관리

### `.gitignore` 설정

```bash
# Python
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/
.coverage

# Environment
.env
.venv/
venv/

# Data files
*.h5
*.pkl
*.npy
data/raw/
data/processed/

# Experiment results
experiments/*/checkpoints/
experiments/*/logs/
*.pth
*.ckpt

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Temporary
tmp/
temp/
*.tmp
```

### 대용량 파일 관리 (Git LFS)

```bash
# Git LFS 설치
brew install git-lfs  # macOS
sudo apt-get install git-lfs  # Ubuntu

# 초기화
git lfs install

# 대용량 파일 타입 추가
git lfs track "*.h5"
git lfs track "*.npy"
git lfs track "*.pkl"

# .gitattributes 커밋
git add .gitattributes
git commit -m "chore: configure Git LFS for large files"
```

## Agent와 수동 작업 혼용

### 수동으로 브랜치 생성 후 Agent 사용

```bash
# 수동으로 브랜치 생성
git checkout -b feature/my-feature

# Agent에게 알림
@versioncontrol-agent
"현재 feature/my-feature 브랜치에서 작업 중이야. 코드 커밋 도와줘"

# Agent가 자동으로:
- 현재 브랜치 확인
- 변경사항 스테이징
- 커밋 및 푸시
```

### Agent 작업 후 수동 검토

```bash
# Agent가 커밋한 후
git log --oneline -5  # 최근 커밋 확인
git show HEAD         # 마지막 커밋 상세 보기
git diff HEAD~1       # 이전 커밋과 비교

# 필요시 수정
git commit --amend -m "새로운 커밋 메시지"
```

## 문제 해결

### 충돌 해결

```bash
# Agent가 충돌 감지 시
@versioncontrol-agent
"브랜치를 병합하려고 하는데 충돌이 발생했어"

# Agent 응답:
⚠️ Merge Conflict Detected
Files with conflicts:
  - src/models/base_model.py
  
Manual resolution needed:
1. Open conflicted files
2. Resolve conflicts (choose between <<<< and >>>>)
3. Stage resolved files: git add [file]
4. Complete merge: git commit

# 수동으로 해결 후
git add src/models/base_model.py
git commit -m "fix: resolve merge conflict in base_model"
```

### 실수로 커밋한 경우

```bash
# 마지막 커밋 취소 (변경사항 유지)
git reset --soft HEAD~1

# 마지막 커밋 취소 (변경사항 삭제)
git reset --hard HEAD~1

# 특정 파일 unstage
git restore --staged file.py
```

### 푸시 전 커밋 수정

```bash
# 마지막 커밋 메시지 수정
git commit --amend -m "feat: correct commit message"

# 마지막 커밋에 파일 추가
git add forgotten_file.py
git commit --amend --no-edit
```

## 협업 워크플로우

### 코드 리뷰

```bash
# 1. PR 생성
@versioncontrol-agent
"feature 브랜치로 PR 생성해줘"

# 2. 리뷰 받기
# GitHub에서 리뷰어가 코멘트

# 3. 피드백 반영
@versioncontrol-agent
"리뷰 피드백을 반영한 변경사항을 커밋해줘"

# 4. 승인 후 병합
gh pr merge --squash  # 또는 --merge, --rebase
```

### 동기화

```bash
# 정기적으로 main 브랜치 업데이트
git checkout main
git pull origin main

# feature 브랜치에 main 변경사항 반영
git checkout feature/my-feature
git rebase main
# 또는
git merge main
```

## 모범 사례

1. **자주 커밋**: 논리적 단위로 작은 커밋 만들기
2. **명확한 메시지**: 변경 이유와 내용을 명확히
3. **브랜치 전략 준수**: 정해진 명명 규칙 따르기
4. **정기적 푸시**: 로컬에만 오래 보관하지 않기
5. **리뷰 요청**: 중요한 변경사항은 리뷰 받기
6. **테스트 후 커밋**: 작동하는 코드만 커밋
7. **민감정보 제외**: .env, 토큰 등은 절대 커밋 금지

## 시스템 통합

### Supervisor 워크플로우

```
User Request
    ↓
Supervisor
    ↓
VersionControl Agent (브랜치 생성)
    ↓
다른 Forge Agents (코드 작업)
    ↓
VersionControl Agent (커밋 & 푸시)
    ↓
VersionControl Agent (PR 생성)
    ↓
User (리뷰 & 병합)
```

### 자동화 예시

```python
# Forge Coordinator가 자동으로 호출
def implement_feature(feature_name: str):
    # 1. 브랜치 생성
    versioncontrol_agent.create_branch(f"feature/{feature_name}")
    
    # 2. 코드 작성
    pytorch_dev_agent.write_model()
    
    # 3. 커밋
    versioncontrol_agent.commit_changes(
        files=["models/new_model.py"],
        message=f"implement {feature_name}",
        type="feat"
    )
    
    # 4. 푸시
    versioncontrol_agent.push()
    
    # 5. PR 생성
    pr_url = versioncontrol_agent.create_pr(
        title=f"Add {feature_name}",
        description="Implementation details..."
    )
    
    return pr_url
```

## 참고 자료

- [Git Documentation](https://git-scm.com/doc)
- [GitHub CLI](https://cli.github.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [Git LFS](https://git-lfs.github.com/)

## 지원

문제가 있는 경우:
1. `git status`로 현재 상태 확인
2. `git log`로 히스토리 확인
3. VersionControl Agent에게 도움 요청
4. GitHub Issues에 문제 보고
