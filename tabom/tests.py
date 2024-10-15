from django.test import TestCase

# Create your tests here.


class MyTest(TestCase):

    def test_simple(self) -> None:
        """
        Given: 테스트에 필요한 재료를 준비한다.
        When: 실제로 테스트 하고자 하는 대상을 호출한다.
        Then: when 에서 수행한 결과가 예상한 바와 일치하는지 검증한다.
            Then 에서 AssertionError 가 발생했다면 테스트 실패다.
            테스트 실행 도중에(Then 에서도) 아무런 에러도 발생하지 않는다면 테스트 성공이다.
        """
        # Given
        a = 1
        b = 3

        # When
        result = a + b

        # Then
        # Actual, Expected
        self.assertEqual(result, 4)
