import logging

log = logging.getLogger(__name__)


def send_password_reset_email(recipient: str, token: str) -> None:
    """Placeholder email sender for password reset.

    In a production environment this function should be replaced with an actual
    email provider integration (SMTP, SendGrid, Mailgun, etc.). The placeholder
    deliberately does **not** log or expose the raw reset token.

    Args:
        recipient: The email address of the user.
        token: The password‑reset token (JWT). The function does not use the
            token – it is kept only to illustrate where a real implementation
            would embed the token in a reset link.
    """
    # NOTE: No logging of the token – we only note that an email would be sent.
    log.info(
        "Password‑reset email placeholder – would send reset link to %s.",
        recipient,
    )

