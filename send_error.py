def send_error(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if DEBUG:
            return func(request, *args, **kwargs)
        else:
            try:
                return func(request, *args, **kwargs)
            except Exception as e:
                current_url = resolve(request.path_info).route

                error: str = f'username: {request.user.username}\n url: {current_url}\n' \
                             f'data: {json.dumps(request.data, indent=4, sort_keys=True)} ' \
                             f'\n error: {traceback.format_exc()}'
                return Response(status=500, data=f.encrypt(error.encode('utf-8')))

    return wrapper
