from app.landing import landing_bp

@landing_bp.route('/', methods=['GET'])
def home():
    return "This is the landing blueprint!"