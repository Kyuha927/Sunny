# 안티그래비티 채팅 날라기는 이유Antigravity구글 안티그래비티의 채팅이 날아가는 건 현재 널리 알려진 버그로 여러 원인이 복합적으로 작용합니다 Protocol Buffer 손상 채팅 기록이 바이너리 pb 파일Protocol Buffer 형식로 저장되는데 이 파일이 쉽게 손상됩니다 노트패드로 열면 한자처럼 보이는 이진 데이터가 출력되는 것이 이 증상입니다 업데이트 후 인덱스 초기화 특히 118x  119x 버전 및 2026년 2월 19일 업데이트 이후 ChatSessionStore 인덱스가 리셋되면서 기존 대화가 사라지는 현상이 대량 보고됐습니다 앱 강제 종료  크래시 앱이 비정상 종료될 경우 마지막 대화가 디스크에 저장되지 않고 날아갑니다 정상적으로 종료해야 저장됩니다 워크스페이스 없이
URL: https://www.perplexity.ai/search/antigeuraebiti-caeting-nalragi-go6hM7uzRlqqSbWcLxsujw

답변
링크
이미지
비디오
공유
안티그래비티 채팅 날라기는 이유
1 단계 완료

Antigravity(구글 안티그래비티)의 채팅이 날아가는 건 현재 널리 알려진 버그로, 여러 원인이 복합적으로 작용합니다.

주요 원인

Protocol Buffer 손상: 채팅 기록이 바이너리 .pb 파일(Protocol Buffer 형식)로 저장되는데, 이 파일이 쉽게 손상됩니다. 노트패드로 열면 한자처럼 보이는 이진 데이터가 출력되는 것이 이 증상입니다.
discuss.google
+1

업데이트 후 인덱스 초기화: 특히 1.18.x / 1.19.x 버전 및 2026년 2월 19일 업데이트 이후 ChatSessionStore 인덱스가 리셋되면서 기존 대화가 사라지는 현상이 대량 보고됐습니다.
discuss.google
+1

앱 강제 종료 / 크래시: 앱이 비정상 종료될 경우 마지막 대화가 디스크에 저장되지 않고 날아갑니다. 정상적으로 종료해야 저장됩니다.
reddit
​

워크스페이스 없이 사용 시: 폴더/워크스페이스를 열지 않은 "Scratch" 세션에서 생성한 대화는 히스토리에 인덱싱되지 않습니다.
discuss.google
​

Undo 버튼 버그: Agent Manager에서 첫 메시지가 아닌 메시지에 Undo를 누르면 대화 전체가 삭제됩니다.
discuss.google
​

1주일 이상 된 대화 자동 삭제: 최신 업데이트 이후 오래된 대화가 자동으로 삭제되는 동작이 추가된 것으로 보고되고 있습니다.
reddit
​

데이터 복구 방법

실제 데이터는 로컬에 남아있는 경우가 많습니다.
discuss.google
​

Windows 경로 확인: C:\Users\<유저명>\.gemini\antigravity\conversations (또는 brain) 폴더에 파일이 있는지 확인
discuss.google
​

AI에게 복구 요청: 새 채팅창에서 아래 프롬프트를 입력해 UI 강제 리프레시 가능:
discuss.google
​

text
I need you to use your list_dir tool on ~/.gemini/antigravity/brain 
and then call list_dir on every single subdirectory inside it.
Reply: "Done" when finished.


오픈소스 복구 툴 사용: 커뮤니티에서 만든 복구 스크립트가 GitHub에 공개되어 있습니다(antigravity-conversation-fix).
reddit
+1

이전 버전으로 다운그레이드: 더 안정적인 구버전 설치 후 히스토리가 자동 인덱싱됩니다.
discuss.google
​

임시 예방법

대화 후 반드시 정상 종료하고, 중요한 내용은 따로 복사해 두는 것이 현재로선 가장 확실한 방법입니다. 구글이 아직 공식 수정 패치를 배포하지 않은 상태라 커뮤니티 수준에서 워크어라운드를 공유하고 있는 상황입니다.
reddit
+1

Claude Sonnet 4.6 Thinking(으)로 준비됨
15개 출처
Protocol Buffer 저장 및 백업 방법
3 단계 완료

Antigravity의 채팅 히스토리는 .pb (Protocol Buffer) 바이너리 파일로 로컬에 저장되며, 이를 안전하게 백업하는 방법은 아래와 같습니다.

파일 저장 위치 (OS별)
OS	Brain 폴더	Conversations 폴더
Windows	%USERPROFILE%\.gemini\antigravity\brain\	%USERPROFILE%\.gemini\antigravity\conversations\
macOS	~/.gemini/antigravity/brain/	~/.gemini/antigravity/conversations/
Linux	~/.gemini/antigravity/brain/	~/.gemini/antigravity/conversations/

conversations/ — {UUID}.pb 형식의 대화 원본 바이너리 파일
reddit
​

brain/ — 각 대화별 .md 요약 파일과 컨텍스트 메타데이터
reddit
​

수동 백업 (가장 확실한 방법)

가장 확실한 방법은 위 두 폴더를 주기적으로 통째로 복사하는 것입니다.
reddit
​

bash
# Windows (PowerShell)
$src = "$env:USERPROFILE\.gemini\antigravity"
$dst = "D:\Backups\antigravity_backup_$(Get-Date -f 'yyyyMMdd_HHmm')"
Copy-Item -Recurse $src $dst

# macOS / Linux
cp -r ~/.gemini/antigravity ~/Backups/antigravity_backup_$(date +%Y%m%d_%H%M)


Windows에서는 %APPDATA%\antigravity\User\globalStorage\state.vscdb (SQLite DB)도 함께 백업하면 인덱스까지 보전됩니다.
discuss.ai.google
​

자동화 툴 활용

Antigravity Storage Manager (VS Code 확장): 구글 드라이브와 자동 E2E 암호화 동기화, ZIP 일괄 내보내기, 다중 기기 충돌 해결 기능 제공. Ctrl+Shift+P → Antigravity Storage: Backup All Conversations 명령으로 원클릭 ZIP 백업 가능.
marketplace.visualstudio
​

antigravity-history (PyPI 패키지): .pb 파일 파싱 및 내보내기 지원.
piwheels
​

Antigravity Database Manager (오픈소스): 손상된 인덱스를 .pb 파일에서 강제 재구축.
discuss.google
​

다른 PC로 이전 시

Antigravity가 종료된 상태에서 아래 3개 폴더를 통째로 새 기기에 복사하면 됩니다 :

~/.gemini — 대화 원본 및 Brain 데이터

~/.antigravity — IDE 설정 (다른 아키텍처 이전 시 extensions/ 폴더는 제외)

~/Library/Application Support/Antigravity/User/ (macOS) 또는 %APPDATA%\antigravity\User\ (Windows) — 워크스페이스 상태 및 UUID 인덱스

히스토리가 보이지 않으면 채팅창에 "migrate my Antigravity setup... re-link conversation files" 프롬프트를 입력해 에이전트가 .pb 파일을 재인덱싱하게 할 수 있습니다 .

핵심 예방 수칙

앱 종료 전 반드시 정상 종료 (강제 종료 시 마지막 세션 미저장)
reddit
​

conversations/ + state.vscdb 를 매일 또는 매주 정기 백업
reddit
​

중요 대화는 brain/ 폴더의 .md 파일로도 확인 가능 (사람이 읽을 수 있는 형식)

Claude Sonnet 4.6 Thinking(으)로 준비됨
16개 출처
우분투에서는 그냥 시스템종료하면 프로그램이 안전하게 종료되지 않는가
1 단계 완료

Ubuntu에서 **정상적인 시스템 종료(전원 메뉴에서 종료, shutdown -h now 등)**를 하면, 일반적으로 프로그램들은 “안전하게 종료”되도록 설계된 절차를 거칩니다.

Ubuntu 종료 시 내부 동작

systemd가 모든 프로세스에 먼저 SIGTERM(정상 종료 요청) 신호를 보내고, 잠시 대기합니다.
discourse.ubuntu
+1

앱이 이 신호를 처리해서 파일 저장, 세션 마무리 등을 한 뒤 종료할 수 있습니다.
discourse.gnome
+1

정해진 시간 내에 종료되지 않으면 SIGKILL(강제 종료)로 남은 프로세스를 죽입니다.
stackoverflow
+1

즉, 이론적으로는 “그냥 시스템 종료”도 대부분의 정상적인 앱에는 안전한 종료 기회를 줍니다.

하지만 100% 안전하지 않은 이유

앱이 SIGTERM 핸들링을 제대로 구현 안 했거나, 내부적으로 비정상 상태(무한 루프, Deadlock 등)에 있으면, SIGTERM을 받아도 정리 작업을 못 하고 있다가 SIGKILL로 강제 종료될 수 있습니다.
stackoverflow
​

UI 프레임워크/GNOME 쪽에서 세션 종료 순서 문제로 앱에 충분한 시간이나 이벤트가 전달되지 않는 사례도 있습니다.
discourse.ubuntu
+1

이 경우 파일 flush가 끝나기 전에 강제 종료되면서, Protocol Buffer 같은 바이너리 파일이 부분만 기록된 손상 상태로 남을 수 있습니다.

실무적으로 어떻게 생각하면 되나

“GUI로 종료 버튼 눌렀다” = 일반적으로 정상 종료 시도로 간주해도 되지만,

중요한 상태(AG 채팅 .pb 파일, DB, 긴 작업 결과 등)는

가능하면 앱을 먼저 직접 종료하고

백업 스크립트/rsync 등으로 복사해 둔 뒤

마지막에 시스템 종료
순서로 가는 게 더 안전합니다.

지금 AG 쪽에서 .pb가 자주 깨지는 증상까지 겹쳐 있으니, 중요한 세션이 많은 날은 AG 먼저 끄고 → 백업 → 그 다음에 Ubuntu 종료 흐름으로 쓰는 게 좋을 것 같습니다.

Ubuntu에서 쓰는 방식 기준으로, 보통은 GUI 종료만 쓰시는지, 아니면 WSL이나 서버처럼 CLI에서 shutdown 쓰는 환경도 같이 쓰시는지 알려주실 수 있나요?

10개 출처
후속 조치
우분투 셧다운 프로세스에서 SIGTERM 핸들링 실패하는 프로그램 유형과 대처 방법
심층 리서치
시스템 종료 시 SIGTERM 무시하는 프로그램 어떻게 처리하나
systemd 서비스 안전 종료 설정 방법
우분투 셧다운 지연이나 동결 해결법
Linux 종료 과정에서 sync와 umount 역할




후속 질문하기
모델