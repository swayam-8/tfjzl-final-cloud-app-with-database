from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Course, Enrollment, Question, Choice, Submission

class ExamTests(TestCase):
    def setUp(self):
        self.user=User.objects.create_user('learner',password='local-fixture-only')
        self.course=Course.objects.create(name='Learning Django',description='Python web development')
        self.enrollment=Enrollment.objects.create(user=self.user,course=self.course)
        self.q=Question.objects.create(course=self.course,content='Is Django a Python framework?',grade=100)
        self.yes=Choice.objects.create(question=self.q,content='Yes',is_correct=True)
        self.no=Choice.objects.create(question=self.q,content='No')
        self.client.force_login(self.user)
    def test_correct_submission_passes(self):
        r=self.client.post(reverse('onlinecourse:submit',args=[self.course.id]),{'choice_'+str(self.yes.id):self.yes.id},follow=True)
        self.assertContains(r,'Congratulations')
        self.assertContains(r,'100/100')
        self.assertEqual(Submission.objects.count(),1)
    def test_selecting_extra_wrong_choice_fails(self):
        r=self.client.post(reverse('onlinecourse:submit',args=[self.course.id]),{'choice_'+str(self.yes.id):self.yes.id,'choice_'+str(self.no.id):self.no.id},follow=True)
        self.assertContains(r,'Failed.')
        self.assertContains(r,'0/100')
    def test_other_user_cannot_read_results(self):
        s=Submission.objects.create(enrollment=self.enrollment)
        other=User.objects.create_user('other')
        self.client.force_login(other)
        self.assertEqual(self.client.get(reverse('onlinecourse:exam_result',args=[self.course.id,s.id])).status_code,404)
    def test_unenrolled_user_cannot_submit(self):
        self.client.force_login(User.objects.create_user('unenrolled'))
        self.assertEqual(self.client.post(reverse('onlinecourse:submit',args=[self.course.id])).status_code,404)
    def test_get_cannot_submit(self):
        self.assertEqual(self.client.get(reverse('onlinecourse:submit',args=[self.course.id])).status_code,405)
