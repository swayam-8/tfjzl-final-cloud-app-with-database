# Django Online Course Assessment
Based on the IBM tfjzl-final-cloud-app-with-database starter (Apache-2.0). AI-assisted implementation prepared for learner review.

Adds Question, Choice and Submission models, editable admin inlines, authenticated enrolled exam submissions, exact-match multi-choice scoring, and detailed results. Only the owner can read a submission; out-of-course choices cannot enter a submission.

Run: `python -m pip install -r requirements.txt`, `python manage.py migrate`, `python manage.py createsuperuser`, `python manage.py runserver`. Open /admin/ to add a course, lesson, questions and choices. Sign in at /onlinecourse/login/, enroll, then submit the course exam. Test with `python manage.py test`.

No personal credentials or database are committed. Set DJANGO_SECRET_KEY and DJANGO_ALLOWED_HOSTS before remote use. The final course declaration and submission belong to the learner.
