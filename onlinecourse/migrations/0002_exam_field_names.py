from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [('onlinecourse', '0001_initial')]
    operations = [
        migrations.RenameField('question', 'content', 'question_text'),
        migrations.RenameField('choice', 'content', 'choice_text'),
    ]
