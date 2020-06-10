from django.db import models
from django.core.validators import RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class Subject(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class Chapter(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject,related_name="chapters",on_delete=models.CASCADE)
    class Meta:
        unique_together=('name','subject')
    def __str__(self):
        return self.name

class Concept(models.Model):
    name = models.CharField(max_length=100)
    chapter = models.ForeignKey(Chapter,related_name="concepts",on_delete=models.CASCADE)
    class Meta:
        unique_together=('name','chapter')
    def __str__(self):
        return self.name

class SubConcept(models.Model):
    name = models.CharField(max_length=100)
    concept = models.ForeignKey(Concept,related_name="subConcepts",on_delete=models.CASCADE)
    class Meta:
        unique_together=('name','concept')
    def __str__(self):
        return self.name
DURATION_CHOICES=((i,i) for i in range(15,121,15))
DIFFICULTY_CHOICES=((i,i) for i in range(1,6))
IMPORTANCE_CHOICES=((i,i) for i in range(1,6))

TARGET_EXAM_CHOICES=TARGET_EXAM=(("IIT","IIT"),("NEET","NEET"))

class Theory(models.Model):
    userId=models.IntegerField()
    concept=models.ForeignKey(Concept,related_name="Theory",on_delete=models.CASCADE)
    subConcept=models.ForeignKey(SubConcept,related_name="Theory",on_delete=models.CASCADE)
    
    theory = RichTextUploadingField(null=True, blank=True)
    easyExampleQues1=RichTextUploadingField(null=True, blank=True)
    easyExampleSol1=RichTextUploadingField(null=True, blank=True)
    easyExampleQues2=RichTextUploadingField(null=True, blank=True)
    easyExampleSol2=RichTextUploadingField(null=True, blank=True)
    easyExampleQues3=RichTextUploadingField(null=True, blank=True)
    easyExampleSol3=RichTextUploadingField(null=True, blank=True)
    easyExampleQues4=RichTextUploadingField(null=True, blank=True)
    easyExampleSol4=RichTextUploadingField(null=True, blank=True)
    easyExampleQues5=RichTextUploadingField(null=True, blank=True)
    easyExampleSol5=RichTextUploadingField(null=True, blank=True)

    mediumExampleQues1=RichTextUploadingField(null=True, blank=True)
    mediumExampleSol1=RichTextUploadingField(null=True, blank=True)
    mediumExampleQues2=RichTextUploadingField(null=True, blank=True)
    mediumExampleSol2=RichTextUploadingField(null=True, blank=True)
    mediumExampleQues3=RichTextUploadingField(null=True, blank=True)
    mediumExampleSol3=RichTextUploadingField(null=True, blank=True)
    mediumExampleQues4=RichTextUploadingField(null=True, blank=True)
    mediumExampleSol4=RichTextUploadingField(null=True, blank=True)
    mediumExampleQues5=RichTextUploadingField(null=True, blank=True)
    mediumExampleSol5=RichTextUploadingField(null=True, blank=True)
    
    hardExampleQues1=RichTextUploadingField(null=True, blank=True)
    hardExampleSol1=RichTextUploadingField(null=True, blank=True)
    hardExampleQues2=RichTextUploadingField(null=True, blank=True)
    hardExampleSol2=RichTextUploadingField(null=True, blank=True)
    hardExampleQues3=RichTextUploadingField(null=True, blank=True)
    hardExampleSol3=RichTextUploadingField(null=True, blank=True)
    hardExampleQues4=RichTextUploadingField(null=True, blank=True)
    hardExampleSol4=RichTextUploadingField(null=True, blank=True)
    hardExampleQues5=RichTextUploadingField(null=True, blank=True)
    hardExampleSol5=RichTextUploadingField(null=True, blank=True)
    
    difficulty=models.IntegerField(null=False,choices=DIFFICULTY_CHOICES)
    importance=models.IntegerField(null=False,choices=IMPORTANCE_CHOICES)

    duration=models.IntegerField(null=False)
    prerequisites=models.ManyToManyField(SubConcept,related_name="prerequisiteOf",blank=True)
    summary=RichTextUploadingField(null=True, blank=True)
    mnemonics=RichTextUploadingField(null=True, blank=True)
    twinConcepts=models.ManyToManyField(SubConcept,related_name="twinConceptOf",blank=True)
    videoUrl=models.URLField(max_length=200, null=False)
    targetExam=models.CharField(max_length=100,null=False,choices=TARGET_EXAM_CHOICES)
    
    wowTheory=RichTextUploadingField(blank=True)
    wowQues=RichTextUploadingField(blank=True)
    wowReason=RichTextUploadingField(blank=True)
    def get_absolute_url(self):
        return reverse('theory-details', kwargs={'pk': self.pk})
    def get_update_url(self):
        return reverse('theory-update',kwargs={'pk':self.pk})
