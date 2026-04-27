import os
import sys

# 0. 윈도우 터미널 한글 깨짐 및 인코딩 에러 방지 (핵심 해결책!)
sys.stdout.reconfigure(encoding='utf-8')

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent

# 1. API 키 설정 (본인의 키로 변경해 주세요)
os.environ["GOOGLE_API_KEY"] = "AIzaSyCbm35Gwr4EhPeXf3BOHh2cIBIiAyuK8TM"

# 2. 도구(손과 발) 준비: 웹 검색 도구
search_tool = DuckDuckGoSearchRun()
tools = [search_tool]

# 3. 두뇌(LLM) 준비: 최신 Gemini 모델
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 4. 에이전트 탄생!
agent_executor = create_react_agent(llm, tools)

# 5. 에이전트에게 임무 부여하기
print("--- 에이전트가 인터넷을 검색 중입니다... ---")
result = agent_executor.invoke({
    "messages": [("user", "주요 증권사가 삼성전자와 SK하이닉스의 2026년도 매출, 영업이익을 가장 최근에 추정한 값을 조사해서 알려줘.")]
})

# 6. 최종 답변 출력
print("\n[AI의 최종 답변]")
print(result["messages"][-1].content)