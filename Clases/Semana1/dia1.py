data =[
  {
    "id": 1024,
    "username": "globetrotter_88",
    "active": True,
    "profile": {
      "first_name": "Elena",
      "last_name": "Rodriguez",
      "email": "elena.ro@example.com"
    },
    "travel_stats": {
      "countries_visited": 12,
      "total_miles": 45200.5
    },
    "tags": ["backpacker", "photography", "street-food"],
    "recent_trips": [
      {
        "destination": "Kyoto, Japan",
        "year": 2025,
        "rating": 5
      }
    ],
    "emergency_contact": None
  },
  {
    "id": 1025,
    "username": "marcus_mountains",
    "active": False,
    "profile": {
      "first_name": "Marcus",
      "last_name": "Chen",
      "email": "m.chen@example.com"
    },
    "travel_stats": {
      "countries_visited": 5,
      "total_miles": 12800.0
    },
    "tags": ["hiking", "camping"],
    "recent_trips": [
      {
        "destination": "Banff, Canada",
        "year": 2026,
        "rating": 5
      }
    ],
    "emergency_contact": {
      "name": "Sarah Chen",
      "relation": "Sister"
    }
  },
    {
    "id": 2222,
    "username": "sexo_man",
    "active":'Undefined',
    "profile": {
      "first_name": "Marcus",
      "last_name": "Chen",
      "email": "m.chen@example.com"
    },
    "travel_stats": {
      "countries_visited": 6,
      "total_miles": 666.0
    },
    "tags": ["hiking", "camping"],
    "recent_trips": [
      {
        "destination": "Banff, Canada",
        "year": 2026,
        "rating": 5
      }
    ],
    "emergency_contact": {
      "name": "Sarah Chen",
      "relation": "Sister"
    }
  },
      {
    "id": 2222,
    "username": "sexo_woman",
    "active":23,
    "profile": {
      "first_name": "sexo",
      "last_name": "Chen",
      "email": "m.chen@example.com"
    },
    "travel_stats": {
      "countries_visited": 6,
      "total_miles": 666.0
    },
    "tags": ["hiking", "camping"],
    "recent_trips": [
      {
        "destination": "Banff, Canada",
        "year": 2026,
        "rating": 5
      }
    ],
    "emergency_contact": {
      "name": "Sarah Chen",
      "relation": "Sister"
    }
  }


]

dictionaries = data[1]
active=[]
inactive = []
check=[]
try:

    for i in data:

        if i['active'] is True:
            active.append(i['username'])
            
        elif i["active"] is False:
            inactive.append(i['username'])
        else:
            check.append(i["username"])
    print(active)

    print(inactive)

    print(check)

except:
    print("No jalo padre")
    










    



     





 