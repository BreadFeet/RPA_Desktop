# 자동화 시키는 동안 작업을 로그로 남겨서 추후 확인할 수 있도록 함
import logging

# debug 이상의 level은 다 출력하도록 설정
# # 시간 [로그레벨] 메세지 형태로 출력
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# # log level) debug < info < warning < error < critical
# logging.debug("아 이거 누가 만든거임???")    # 개발단계에서 사용하는 방법
# logging.info("자동화 수행 준비")            # 사용자도 확인할 수 있는 방법
# logging.warning("경고문: 실행 오류")
# logging.error("에러 발생 코드: xxx")
# logging.critical("복구 불가능한 심각한 문제 발생")

# 터미널과 파일에 함께 로그 남기기
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")    
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 터미널 스트림에 로그 출력
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일에 로그 남기기
from datetime import datetime

filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그 남기기 테스트")





