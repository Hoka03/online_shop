from django.core.validators import ValidationError


def phone_validate(phone_numb_validate: str) -> None:
    if (len(phone_numb_validate) != 13 or not phone_numb_validate.startswith('+998') or
            not phone_numb_validate[1:].isdigit()):
        raise ValidationError('Phone number was valid')