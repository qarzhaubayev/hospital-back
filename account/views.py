from rest_framework.authtoken.views  import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response         import Response

from doctor.models import Doctor
from patient.models import Patient

class UserObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.errors)
        user           = serializer.validated_data['user']
        print(user.iin_num)
        token, created = Token.objects.get_or_create(user=user)
        try:
            doctor = Doctor.objects.get(iin_num = user.iin_num)
            return Response({'token': token.key, 'who': 'doctor', 'user': user.iin_num})
        except Doctor.DoesNotExist:
            try:
                patient = Patient.objects.get(iin_num = user.iin_num)
                return Response({'token': token.key, 'who': 'patient', 'user_iin': user.iin_num})
            except Patient.DoesNotExist:
                return Response({'token': token.key})


obtain_auth_token = UserObtainAuthToken.as_view()
