from SRT import SRT
from dotenv import load_dotenv #dotenv는 환경변수 관리를 돕는 라이브러이이다.
import os

#SRT id와 pw노출 방지를 위해 이들을 별도의 .env파일로 뺐다. .env파일의 경로는 아무렇게나 놓아도 상관이 없다고 한다.
env_path = 'secret/.env'#.env파일이 루트 디렉터리와 다른 경로에 있을 때는 이렇게 경로를 설정해서 인수로 넣어줘야 한다.
load_dotenv(dotenv_path=env_path)

srt = SRT(os.getenv("SRT_ID"), os.getenv("SRT_PASSWORD"))#SRT클라이언트 클래스 인스턴스 생성, 인스턴스를 생성할 때 입력한 계정 아이디, 비밀번호로 자동으로 로그인함.
# Args:
#         srt_id (str): SRT 계정 아이디 (멤버십 번호, 이메일, 전화번호)
#         srt_pw (str): SRT 계정 패스워드
#         auto_login (bool): :func:`login` 함수 호출 여부
#         verbose (bool): 디버깅용 로그 출력 여부

dep = '천안아산'
arr = '동탄'
date = '20240909'
time = '144000'
trains = srt.search_train(dep, arr, date, time, available_only = False)
# Parameters:
# dep (str) – 출발역
# arr (str) – 도착역
# date (str, optional) – 출발 날짜 (yyyyMMdd) (default: 당일)
# time (str, optional) – 출발 시각 (hhmmss) (default: 0시 0분 0초)
# time_limit (str, optional) – 출발 시각 조회 한도 (hhmmss)
# available_only (bool, optional) – 매진되지 않은 열차만 검색합니다 (default: True)
# Returns:
# 열차 리스트
# Return type:
# list[SRTTrain]

print(trains)
print(trains[0])

#SRT클래스의 search_train함수를 실행하면 어딘가에서 api요청을 날려서 JSON을 받아오고, 그것을 response_data.py의 SRTResponseData클래스에서 받아서 json을 단순하게 파싱하고, 통신 성공 여부를 파악
#그리고 for루프로 각 열차정보를 train.py의 SRTTrain클래스로 넘겨서 실질적으로 파싱을 해서 [SRT] 09월 09일, 천안아산~동탄(15:29~15:45) 특실 매진 이런 형식으로 반환한다.
#SRTTrain클래스로 __str__ 함수로 출력될 때의 형식을 지정해놓았을 뿐(toString()오버라이딩이랑 비슷), 리스트에 담긴 각각의 요소들은 모두 SRTTrain클래스의 인스턴스이기 때문에 각 속성에 내가 직접 접근할 수도 있다.
print(trains[0].dep_time, trains[0].arr_time)

#내가 원하는 열차 정보만 조회해보자.
dep = '천안아산'
arr = '동탄'
date = '20240909'
time = '152900'
time_limit = '154500'
trains = srt.search_train(dep, arr, date, time, time_limit, available_only = False)
print(trains)
