from django.db import models
from django.contrib.auth.models import User
from exam.models import Question
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=500, blank=True, null=True)
    true_answer = models.CharField(max_length=500, blank=True, null=True)
    is_true = models.NullBooleanField(null=True)

    def __str__(self):
        return "user: {}, quest: {}, is_true: {}, quest_id: {}".format(self.user, self.question, self.is_true, self.question.id)


class Rank(models.Model):
    rank_img = models.ImageField(
        upload_to='rank_img/',
        blank=True
    )
    rank_img_disable = models.ImageField(
        upload_to='rank_img/',
        blank=True
    )
    rank_title = models.CharField(max_length=200)
    rank_description = models.CharField(max_length=200)
    rank_reward_point = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.rank_title)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True)
    points = models.IntegerField(default=0)
    user_avatar = models.ImageField(
        upload_to='profile_avatar/',
        default='profile_avatar/default.png',
        blank=True)
    birthday = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    last_mini_game = models.DateTimeField(default=timezone.now)
    last_password_update = models.DateTimeField(default=timezone.now)
    online_game_total_games = models.IntegerField(default=0)
    online_game_count_of_wins = models.IntegerField(default=0)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, default=1)
    rank_progress = models.IntegerField(default=100)

# ----- function for online-game
    def inc_points(self, points):
        self.points += points

    def dec_points(self, points):
        if (self.points - points >= 0):
            self.points -= points

    def get_statistic(self):
        return self.online_game_count_of_wins / self.online_game_total_games

    def insert_results(self, winner, points):
        self.online_game_total_games += 1
        if winner:
            self.online_game_count_of_wins += 1
            self.inc_points(points)
        else:
             self.dec_points(points)

# -----
    def __str__(self):
        return "profile: {}".format(self.user)

    class Meta:
        ordering = ['-points']


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

