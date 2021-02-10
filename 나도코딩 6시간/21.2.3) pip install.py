# pip로 패키지 설치하기

# 구글에서 pypi 검색해서 링크 받아서
# 아래 터미널 쪽에 붙여놓고 엔터치기  # beatifulsoup4 받아옴
# 아래 터미널에 pip.list 치면 사용중인 패키지 버전 나온다
# pip show beautifulsoup4   bs4 패키지에 대한 설명 나온다.
# 패키지 업그레이드가 필요할 경우  pip install --upgrade ~~(beautifulsoup4)
# 패키지 삭제하려면  pip uninstall beautifulsoup4  

import inspect
from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())



print(inspect.getfile(BeautifulSoup))


# 5. 패키지 등 다운로드 방법
#   1) cmd창을 실행한다
#   2) "pip install numpy(패키지명)" 을 작성한다.
