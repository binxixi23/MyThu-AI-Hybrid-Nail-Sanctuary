import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class MyThuAgent:
    def __init__(self, api_key):
        # Thiết lập Agent với độ sáng tạo cao để tư vấn thẩm mỹ
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.7, api_key=api_key)
        
        self.system_template = """
        Bạn là 'Mỹ Thủ' - Trợ lý AI của một nghệ nhân Nail có 20 năm kinh nghiệm.
        NHIỆM VỤ:
        1. Phân tích màu da (Ngăm, Trắng, Vàng) để tư vấn màu móng.
        2. Gợi ý các mẫu vẽ 3D phù hợp với xu hướng nhưng vẫn sang trọng.
        3. Giải thích lý do tại sao mẫu này lại hợp với khách (Dựa trên hình thể móng).
        
        PHONG CÁCH: Chuyên nghiệp, tinh tế, sử dụng ngôn ngữ của một stylist cao cấp.
        
        Khách hàng hỏi: {input}
        Mỹ Thủ phản hồi:"""
        
        self.prompt = PromptTemplate(input_variables=["input"], template=self.system_template)

    def consult(self, user_query):
        formatted_prompt = self.prompt.format(input=user_query)
        return self.llm.predict(formatted_prompt)

# Thử nghiệm tư vấn
# agent = MyThuAgent(api_key="sk-...")
# print(agent.consult("Da mình hơi ngăm, đi tiệc cưới nên làm mẫu gì sang?"))
