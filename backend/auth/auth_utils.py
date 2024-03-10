def get_authenticated_user_details(request_headers):
    # Return a default, non-authenticated user object
    user_object = {
        'user_principal_id': 'default_user',
        'user_name': 'Guest',
        'auth_provider': 'None',
        'auth_token': 'None',
        'client_principal_b64': 'None',
        'aad_id_token': 'None'
    }

    return user_object
