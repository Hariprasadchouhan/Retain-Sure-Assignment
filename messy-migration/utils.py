def serialize_user(row):
    # Assumes columns: id, name, email
    return {
        "id": row[0],
        "name": row[1],
        "email": row[2]
    }

def validate_user_data(data):
    if not isinstance(data, dict):
        return False, "Invalid data format"
    for field in ['name', 'email', 'password']:
        if not data.get(field):
            return False, f"Missing required field: {field}"
    return True, ""
