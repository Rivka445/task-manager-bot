import json
import os
import requests
from dotenv import load_dotenv
from todo_service import get_tasks, add_task, update_task, delete_task
from tools_schema import tools
from datetime import datetime, timedelta

load_dotenv()

def call_gemini(prompt: str, use_tools: bool = False) -> dict:
    """קריאה ל-Gemini API"""
    api_key = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={api_key}"
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    if use_tools:
        payload["tools"] = tools
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"שגיאה: {response.status_code} - {response.text}"}
    except Exception as e:
        return {"error": f"שגיאה: {str(e)}"}

def agent(query: str) -> str:
    """אייג'נט חכם שפונה ל-Gemini עם function calling"""
    
    # שליחת השאילתה עם tools
    response = call_gemini(query, use_tools=True)
    
    if "error" in response:
        return response["error"]
    
    try:
        candidate = response["candidates"][0]
        content = candidate["content"]
        
        # בדיקה אם יש function call
        if "parts" in content:
            for part in content["parts"]:
                if "functionCall" in part:
                    func_call = part["functionCall"]
                    function_name = func_call["name"]
                    parameters = func_call.get("args", {})
                    
                    # הפעלת הפונקציה
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
                    
                    # שליחת התוצאה חזרה ל-Gemini לניסוח תשובה
                    final_prompt = f"""
User asked: "{query}"
Function executed: {function_name}
Result: {json.dumps(result, ensure_ascii=False)}

Write a friendly Hebrew response explaining what happened.
"""
                    final_response = call_gemini(final_prompt, use_tools=False)
                    if "error" in final_response:
                        return final_response["error"]
                    
                    return final_response["candidates"][0]["content"]["parts"][0]["text"]
        
        # אם אין function call, החזר תשובה רגילה
        return content["parts"][0].get("text", "לא הצלחתי להבין")
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"שגיאה: {str(e)}"
