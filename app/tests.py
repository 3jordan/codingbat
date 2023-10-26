from django.test import TestCase


# Create your tests here.
class Test_warmup_one_view(TestCase):
    def test_93_near_hundred(self):
        response = self.client.get("/warmup-1/near-hundred/93")
        self.assertContains(response, "True")

    def test_90_near_hundred(self):
        response = self.client.get("/warmup-1/near-hundred/90")
        self.assertContains(response, "True")

    def test_89_near_hundred(self):
        response = self.client.get("/warmup-1/near-hundred/89")
        self.assertContains(response, "False")


class Test_warmup_two_view(TestCase):
    def test_Code(self):
        response = self.client.get("/warmup-2/string-splosion/Code")
        self.assertContains(response, "CCoCodCode")

    def test_Code(self):
        response = self.client.get("/warmup-2/string-splosion/abd")
        self.assertContains(response, "aababc")

    def test_Code(self):
        response = self.client.get("/warmup-2/string-splosion/aab")
        self.assertContains(response, "aab")


class Test_cat_dog_view(TestCase):
    def test_catdog(self):
        response = self.client.get("/string-2/cat-dog/catdog")
        self.assertContains(response, "True")

    def test_catdog(self):
        response = self.client.get("/string-2/cat-dog/catcat")
        self.assertContains(response, "False")

    def test_catdog(self):
        response = self.client.get("/string-2/cat-dog/1cat1cadodog")
        self.assertContains(response, "True")


class Test_logic_two_view(TestCase):
    def test_123(self):
        response = self.client.get("/logic-2/lone-sum/1/2/3/")
        self.assertContains(response, "6")

    def test_123(self):
        response = self.client.get("/logic-2/lone-sum/3/2/3/")
        self.assertContains(response, "2")

    def test_123(self):
        response = self.client.get("/logic-2/lone-sum/3/3/3/")
        self.assertContains(response, "0")
