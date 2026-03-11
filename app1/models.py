from django.db import models

class Student(models.Model):
    stud_id = models.CharField(max_length=10, primary_key=True)
    stud_name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20, unique=True)
    dep_name = models.CharField(max_length=100)

    def __str__(self):
        return self.stud_name


class Project(models.Model):
    project_id = models.CharField(max_length=10, primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    coordinator_name = models.CharField(max_length=100)

    def __str__(self):
        return self.project_title


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name


class Task(models.Model):
    task_id = models.CharField(max_length=10, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200) 
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_id


class Assignment(models.Model):
    assignment_id = models.CharField(max_length=10, primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assigned_date = models.DateField()

    def __str__(self):
        return self.assignment_id


class Status(models.Model):
    status_id = models.CharField(max_length=10, primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    updated_date = models.DateField()

    def __str__(self):
        return f"{self.task.task_id} - {self.status}"