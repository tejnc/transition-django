from rest_framework import serializers


class CustomPasswordValidation:

    def validate_password(attrs, password, confirm_password):
        SPECIAL_SYMBOL = ['$', '@', '#', '%', '!', '^', '&', '*']
        print("password", password)
        print("confirm_password", confirm_password)

        if password != confirm_password:
            raise serializers.ValidationError(
                "Passwords did not match!"
            )
        if len(password)<8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long."
            )
        if len(password) > 12:
            raise serializers.ValidationError(
                "The new password should not be greater than 12 characters long."
            )
        first_isalpha = password[0].isalpha()
        if all(c.isalpha()==first_isalpha for c in password):
            raise serializers.ValidationError(
                "New password must be at least one letter and  at least one digit or punctuation character."
            )
        first_isupper = password[0].isupper()
        if all(c.isupper() == first_isupper for c in password):
            raise serializers.ValidationError(
                "The new password must contain at least one Uppercase Letter."
            )
        if not any(c in SPECIAL_SYMBOL for c in password):
            raise serializers.ValidationError(
                "The password must contain at least one Special Symbols."
            )
        return password
