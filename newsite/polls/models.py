from django.db import models

# Create your models here.

#Created classes to create table in SQL database.

class Question(models.Model):
    """This will be a field that takes admin input

    Args:
        This will take in the title, body and date

    Returns:
        These will return a field in django admin to take in a new article
    """
    question_text = models.CharField(max_length=200)
    question_body = models.TextField(default='DEFAULT VALUE')
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        """This will return the string value

        Returns:
            This will return the atricle title
        """
        return self.question_text

