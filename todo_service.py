from datetime import datetime
from typing import List, Dict, Optional

# מערך לשמירת המשימות
tasks = []
task_counter = 1

def get_tasks(status: Optional[str] = None, task_type: Optional[str] = None, 
              start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Dict]:
    """שליפת משימות עם סינונים שונים"""
    filtered_tasks = tasks
    
    if status:
        filtered_tasks = [t for t in filtered_tasks if t.get('status') == status]
    if task_type:
        filtered_tasks = [t for t in filtered_tasks if t.get('type') == task_type]
    if start_date:
        filtered_tasks = [t for t in filtered_tasks if t.get('start_date') >= start_date]
    if end_date:
        filtered_tasks = [t for t in filtered_tasks if t.get('end_date') <= end_date]
    
    return filtered_tasks

def add_task(title: str, description: str = "", task_type: str = "", 
             start_date: str = "", end_date: str = "", status: str = "pending") -> Dict:
    """הוספת משימה חדשה"""
    global task_counter
    
    task = {
        "id": task_counter,
        "title": title,
        "description": description,
        "type": task_type,
        "start_date": start_date,
        "end_date": end_date,
        "status": status
    }
    
    tasks.append(task)
    task_counter += 1
    
    return task

def update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                task_type: Optional[str] = None, start_date: Optional[str] = None,
                end_date: Optional[str] = None, status: Optional[str] = None) -> Optional[Dict]:
    """עדכון משימה קיימת"""
    for task in tasks:
        if task['id'] == task_id:
            if title is not None:
                task['title'] = title
            if description is not None:
                task['description'] = description
            if task_type is not None:
                task['type'] = task_type
            if start_date is not None:
                task['start_date'] = start_date
            if end_date is not None:
                task['end_date'] = end_date
            if status is not None:
                task['status'] = status
            return task
    
    return None

def delete_task(task_id: int) -> bool:
    """מחיקת משימה"""
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks.pop(i)
            return True
    
    return False
