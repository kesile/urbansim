def createNarrow(hour):
    narrowFunctions = [{
        "name": "schedule",
            "description": "Create a schedule.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        f"{hour}:00 Activity": {
                            "type": "string",
                            "description": f"What someone is doing at {hour}:00"
                        },
                        f"{hour}:00 Place": {
                            "type": "string",
                            "description": f"Where someone is at {hour}:00"
                        },
                        f"{hour}:05 Activity": {
                            "type": "string",
                            "description": f"What someone is doing at {hour}:05"
                        },
                        f"{hour}:05 Place": {
                            "type": "string",
                            "description": f"Where someone is at {hour}:05"
                        },
                        f"{hour}:10 Activity": {
                            "type": "string",
                            "description": f"What someone is doing at {hour}:10"
                        },
                        f"{hour}:10 Place": {
                            "type": "string",
                            "description": f"Where someone is at {hour}:10"
                        },
                        f"{hour}:15 Activity": {
                            "type": "string",
                            "description": f"What someone is doing at {hour}:15"
                        },
                        f"{hour}:15 Place": {
                            "type": "string",
                            "description": f"Where someone is at {hour}:15"
                        },
                        f"{hour}:20 Activity": {
                            "type": "string",
                            "description": f"What someone is doing at {hour}:20"
                        },
                        f"{hour}:20 Place": {
                            "type": "string",
                            "description": f"Where someone is at {hour}:20"
                        },
                        f"{hour}:25 Activity": {
                            "type": "string",
                            "description": f"What someone is doing at {hour}:25"
                        },
                        f"{hour}:25 Place": {
                            "type": "string",
                            "description": f"Where someone is at {hour}:25"
                        },
                        f"{hour}:30 Activity": {
                            "type": "string",
                            "description": f"What someone is doing at {hour}:30"
                        },
                        f"{hour}:30 Place": {
                            "type": "string",
                            "description": f"Where someone is at {hour}:30"
                        },
                        f"{hour}:35 Activity": {
                            "type": "string",
                            "description": f"What someone is doing at {hour}:35"
                        },
                        f"{hour}:35 Place": {
                            "type": "string",
                            "description": f"Where someone is at {hour}:35"
                        },
                        f"{hour}:40 Activity": {
                            "type": "string",
                            "description": f"What someone is doing at {hour}:40"
                        },
                        f"{hour}:40 Place": {
                            "type": "string",
                            "description": f"Where someone is at {hour}:40"
                        },
                        f"{hour}:45 Activity": {
                            "type": "string",
                            "description": f"What someone is doing at {hour}:45"
                        },
                        f"{hour}:45 Place": {
                            "type": "string",
                            "description": f"Where someone is at {hour}:45"
                        },
                        f"{hour}:50 Activity": {
                            "type": "string",
                            "description": f"What someone is doing at {hour}:50"
                        },
                        f"{hour}:50 Place": {
                            "type": "string",
                            "description": f"Where someone is at {hour}:50"
                        },
                        f"{hour}:55 Activity": {
                            "type": "string",
                            "description": f"What someone is doing at {hour}:55"
                        },
                        f"{hour}:55 Place": {
                            "type": "string",
                            "description": f"Where someone is at {hour}:55"
                        },
                    },
                    "required": [
                        f"{hour}:00 Place",
                        f"{hour}:05 Place",
                        f"{hour}:10 Place",
                        f"{hour}:15 Place",
                        f"{hour}:20 Place",
                        f"{hour}:25 Place",
                        f"{hour}:30 Place",
                        f"{hour}:35 Place",
                        f"{hour}:40 Place",
                        f"{hour}:45 Place",
                        f"{hour}:50 Place",
                        f"{hour}:55 Place",
                        f"{hour}:00 Activity",
                        f"{hour}:05 Activity",
                        f"{hour}:10 Activity",
                        f"{hour}:15 Activity",
                        f"{hour}:20 Activity",
                        f"{hour}:25 Activity",
                        f"{hour}:30 Activity",
                        f"{hour}:35 Activity",
                        f"{hour}:40 Activity",
                        f"{hour}:45 Activity",
                        f"{hour}:50 Activity",
                        f"{hour}:55 Activity"                    
                ]
                }
    }]
    return narrowFunctions