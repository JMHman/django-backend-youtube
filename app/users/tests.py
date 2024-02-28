from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class UserTestCase(TestCase):
  # 회원가입을 가정하고 => 회원가입 함수 테스트 코드를 작성하려고 합니다.
  # 이메일과 패스워드를 입력받고, 회원가입이 정상젇으로 잘 이뤄졌는지 체크

  def test_create_user(self):
    email = 'joenmh0710@gmail.com'
    password = 'password123'
    
    user = get_user_model().objects.create_user(
      email=email, password=password
    )

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))
    self.assertFalse(user.is_superuser)




  def test_create_superuser(self):
    email = 'super_joenmh0710@gmail.com'
    password = 'password123'

  
    super_user = get_user_model().objects.create_superuser(
      email=email, 
      password=password
    )

    # self.assertEqual(superuser.email, email)
    # self.assertEqual(superuser.password, password)
    self.assertTrue(super_user.is_superuser)
    self.assertTrue(super_user.is_staff)
