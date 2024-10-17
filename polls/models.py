from django.db import models
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    question_text = models.CharField(_("Question Text"), max_length=50)
    pub_date = models.DateTimeField(_("Date Published"))
    
    def __str__(self):
        # return self.pub_date.strftime("%Y-%m-%d %H:%M:%S")
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name=_("Related Question"), on_delete=models.CASCADE)
    choice_text = models.CharField(_("Choice Text"), max_length=50)
    votes = models.IntegerField(_("Vote Count"), default=0)

    def __str__(self):
        return self.choice_text
