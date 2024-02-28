from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, 
                                        PermissionsMixin, 
                                        BaseUserManager)

# Create your models here.

class UserManager(BaseUserManager):
  def create_user(self, email, password, **extra_fields):
    if not email:
      raise ValueError('이메일 주소가 입력되지 않았습니동')
    # **extra_fields 는 적혀있는 값 외의 다른 입력값들도 보여줘라 뭐 그런 뜻
    user = self.model(email=email, **extra_fields)
    user.set_password(password) # 비밀번호 해쉬화
    user.save(using=self._db)

    return user
  
  def create_superuser(self, email, password):
    # if not email:
    #   raise ValueError('이메일 주소가 입력되지 않았습니둥')
    
    # user = self.model(email=self.email)
    # user.set_password(password)
    user = self.create_user(email, password) 
    # 같은 class 안에 있지만 이 함수 밖에 있는 함수를 사용하는 거기 때문에 self가 붙는다

    user.is_superuser = True
    user.is_staff = True

    user.save(using=self._db)

    return user

class User(AbstractBaseUser, PermissionsMixin):
  # - email:
  # email = models.EmailField(max_length=30, unique=True)
  email = models.CharField(max_length=30, unique=True)
  # - password: AbstractBaseUser에 기본으로 있기 떄문에 따로 코드를 작성할 필요가 없다
  # - nickname: 이메일을 유저네임필드로 지정했기 때문에 유저네임 대신 닉네임이 들어왔다
  nickname = models.CharField(max_length=255)
  # - is_business(boolean): personal, business
  is_business = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True) # 가입하자마자 유저를 슈퍼유저로 지정한다
  is_staff = models.BooleanField(default=False)

  USERNAME_FIELD = 'email' # 이메일을 유저네임으로 사용하겠다는 뜻

  objects = UserManager()

  def __str__(self):
    if self.is_staff == True:
      staff = 'King!'
    else:
      staff = None
    return f'email: {self.email}, nickname: {self.nickname} {staff}'
