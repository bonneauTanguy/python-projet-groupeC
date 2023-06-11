import logging

logger = logging.getLogger(__name__)


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path_info.startswith(
            "/admin/"
        ) and not request.path_info.startswith("/accounts/"):
            if request.user.is_authenticated:
                username = request.user.username
                logger.info(f"Utilisateur {username} a accédé à la vue {request.path}")
            else:
                logger.info(
                    f"Un utilisateur non authentifié a accédé à la vue {request.path}"
                )

        response = self.get_response(request)
        return response
