def Read(file: str):
    existing = {}
        
    try:
        with open(file, "r") as f:
            for i in f:
                name, points = i.strip().split(" | ")
                existing[name] = points
            
            return existing
    except Exception as e:
        print(f"Exception Occured: {e}")
        return

def Save(file: str, users: list):
    try:
        existing = {}
        
        try:
            with open(file, "r") as f:
                for i in f:
                    name, points = i.strip().split(" | ")
                    existing[name] = points
        except FileNotFoundError:
            pass
        
        for user in users:
            existing[user.name] = user.points
        
        with open(file, "w") as f:
            for name, points in existing.items():
                f.write(f"{name} | {points}\n")
    except Exception as e:
        print(f"Exception Occured: {e}")
        return