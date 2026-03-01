tools = [
    {
        "type": "function",
        "function": {
            "name": "get_tasks",
            "description": "שליפת משימות עם אפשרות לסינון לפי סטטוס, סוג, תאריך התחלה ותאריך סיום",
            "parameters": {
                "type": "object",
                "properties": {
                    "status": {
                        "type": "string",
                        "description": "סטטוס המשימה (pending, in_progress, completed)"
                    },
                    "task_type": {
                        "type": "string",
                        "description": "סוג המשימה"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "תאריך התחלה (YYYY-MM-DD)"
                    },
                    "end_date": {
                        "type": "string",
                        "description": "תאריך סיום (YYYY-MM-DD)"
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_task",
            "description": "הוספת משימה חדשה למערכת",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "כותרת המשימה"
                    },
                    "description": {
                        "type": "string",
                        "description": "תיאור המשימה"
                    },
                    "task_type": {
                        "type": "string",
                        "description": "סוג המשימה"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "תאריך התחלה (YYYY-MM-DD)"
                    },
                    "end_date": {
                        "type": "string",
                        "description": "תאריך סיום (YYYY-MM-DD)"
                    },
                    "status": {
                        "type": "string",
                        "description": "סטטוס המשימה (pending, in_progress, completed)"
                    }
                },
                "required": ["title"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_task",
            "description": "עדכון משימה קיימת במערכת",
            "parameters": {
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "integer",
                        "description": "מזהה המשימה לעדכון"
                    },
                    "title": {
                        "type": "string",
                        "description": "כותרת חדשה למשימה"
                    },
                    "description": {
                        "type": "string",
                        "description": "תיאור חדש למשימה"
                    },
                    "task_type": {
                        "type": "string",
                        "description": "סוג חדש למשימה"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "תאריך התחלה חדש (YYYY-MM-DD)"
                    },
                    "end_date": {
                        "type": "string",
                        "description": "תאריך סיום חדש (YYYY-MM-DD)"
                    },
                    "status": {
                        "type": "string",
                        "description": "סטטוס חדש (pending, in_progress, completed)"
                    }
                },
                "required": ["task_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_task",
            "description": "מחיקת משימה מהמערכת",
            "parameters": {
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "integer",
                        "description": "מזהה המשימה למחיקה"
                    }
                },
                "required": ["task_id"]
            }
        }
    }
]
