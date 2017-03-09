from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils import timezone

class Campus(models.Model):
	location = models.CharField(max_length=255)
	number = models.CharField(max_length=2)

	def __str__(self):
		return 'Campus ' + self.number + ' - ' + self.location

class Category(models.Model):
	name = models.CharField(max_length=255)
	rules = models.TextField()
	need_score = models.BooleanField(default=False)
	need_time = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Tournament(models.Model):
	location = models.ForeignKey(Campus, on_delete=models.CASCADE, default=None, null=True)
	responsible = models.ForeignKey(User, null=True)
	start = models.DateField()
	end = models.DateField()

	def status(self):
		now = date.today()
		if now < self.start:
			return 'status-waiting'
		elif now <= self.end:
			return 'status-in-progress'
		else:
			return 'status-ended'

	def __str__(self):
		return str(self.start.year)

class Competition(models.Model):
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="competitions", null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.category.name

	def status(self):
		pass


class Participant(models.Model):
	user = models.ForeignKey(User, null=True)
	name = models.CharField(max_length=255)
	code = models.CharField(max_length=12)
	email = models.EmailField(max_length=255)
	course = models.CharField(max_length=255)
	leader = models.BooleanField(default=False)

	def __str__(self):
		return self.name + ' - ' + self.course


class Group(models.Model):
	name = models.CharField(max_length=255)
	depth = models.IntegerField(default=0)
	competition = models.ForeignKey(Competition, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Team(models.Model):
	name = models.CharField(max_length=255)
	score = models.IntegerField(default=0)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	participants = models.ManyToManyField(Participant, related_name='team_participants')
	group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return self.name
	
	def str_participants(self):
		return ', '.join([p.name for p in self.participants.all()])


class Match(models.Model):
	competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='matchs', null=True)
	campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True)
	responsible = models.ForeignKey(User, null=True)
	date = models.DateField(default=date.today)
	start = models.TimeField(default=timezone.now)
	end = models.TimeField(default=timezone.now)
	location = models.CharField(max_length=255)
	teams = models.ManyToManyField(Team, related_name='teams')
	intercampi = models.BooleanField(default=False)
	first_place = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='first_place', blank=True, null=True)

	def status(self):
		now = datetime.now()
		start = datetime.combine(self.date, self.start)
		end = datetime.combine(self.date, self.end)
		if now < start:
			return 'status-waiting'
		elif now <= end:
			return 'status-in-progress'
		else:
			return 'status-ended'

	def type(self):
		if self.intercampi:
			return "Final"
		else:
			return "Seletiva"

	def __str__(self):
		return self.competition.category.name + ' (' + self.campus.__str__() + ')'

	def matches_ready_to_publish_result(matches):
		MATCHES = []
		for match in matches:
			match_score = MatchScore.objects.all().filter(match=match)
			if match.teams.count()==match_score.count() and not match.first_place and match_score.count()!=0:
				MATCHES.append(match)
		return MATCHES

	def match_not_ready(matches):
		MATCHES = []
		for match in matches:
			match_score = MatchScore.objects.all().filter(match=match)
			if match.teams.count()!=match_score.count() or match_score.count()==0:
				MATCHES.append(match)
		return MATCHES


	def match_already_published(matches):
		MATCHES = []
		for match in matches:
			match_score = MatchScore.objects.all().filter(match=match)
			if match.teams.count()==match_score.count() and match_score.count()!=0 and match.first_place:
				MATCHES.append(match)
		return MATCHES


class MatchScore(models.Model):
	match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='scores')
	team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
	score = models.IntegerField(default=0, blank=True, null=True)
	time = models.TimeField(default='00:00', blank=True, null=True)
	judge = models.ForeignKey(User, null=True)
	date_time = models.DateTimeField(null=True)

	def __str__(self):
		return self.team.__str__() + ' - ' + self.match.__str__()
