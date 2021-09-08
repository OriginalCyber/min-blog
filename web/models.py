from django.db import models


class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Student(models.Model):
    """Model definition for Student."""

    # TODO: Define fields here
    student_code = models.CharField(max_length=11)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Student."""

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        """Unicode representation of Student."""
        return self.first_name + " " + self.last_name


class Subject(models.Model):
    """Model definition for Subject."""

    # TODO: Define fields here
    Subject_code = models.CharField(max_length=25)
    subject_name_th = models.CharField(max_length=255)
    subject_name_en = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    student = models.ManyToManyField(Student, default=None, null=True, blank=True)



    class Meta:
        """Meta definition for Subject."""

        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        """Unicode representation of Subject."""
        return self.subject_name_th

