import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from todo_service import get_tasks, add_task, update_task, delete_task
from tools_schema import tools

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def agent(query: str) -> str:
    """אייג'נט חכם שפונה ל-OpenAI עם function calling"""
    
    messages = [{"role": "user", "content": query}]
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools
        )
        
        message = response.choices[0].message
        
        if message.tool_calls:
            tool_call = message.tool_calls[0]
            function_name = tool_call.function.name
            parameters = json.loads(tool_call.function.arguments)
            
            if function_name == "get_tasks":
                result = get_tasks(**parameters)
            elif function_name == "add_task":
                result = add_task(**parameters)
            elif function_name == "update_task":
                result = update_task(**parameters)
            elif function_name == "delete_task":
                result = delete_task(**parameters)
            else:
                return "לא הצלחתי להבין"
            
            messages.append(message)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result, ensure_ascii=False)
            })
            
            final_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            
            return final_response.choices[0].message.content
        
        return message.content or "לא הצלחתי להבין"
        
    except Exception as e:
        return f"שגיאה: {str(e)}"
