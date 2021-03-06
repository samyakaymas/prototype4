# Generated by Django 3.0.7 on 2020-06-09 06:11

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concepts', to='theoryTag.Chapter')),
            ],
            options={
                'unique_together': {('name', 'chapter')},
            },
        ),
        migrations.CreateModel(
            name='SubConcept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('concept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subConcepts', to='theoryTag.Concept')),
            ],
            options={
                'unique_together': {('name', 'concept')},
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('theory', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('easyExampleQues1', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('easyExampleSol1', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('easyExampleQues2', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('easyExampleSol2', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('easyExampleQues3', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('easyExampleSol3', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('easyExampleQues4', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('easyExampleSol4', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('easyExampleQues5', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('easyExampleSol5', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('mediumExampleQues1', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('mediumExampleSol1', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('mediumExampleQues2', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('mediumExampleSol2', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('mediumExampleQues3', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('mediumExampleSol3', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('mediumExampleQues4', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('mediumExampleSol4', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('mediumExampleQues5', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('mediumExampleSol5', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('hardExampleQues1', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('hardExampleSol1', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('hardExampleQues2', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('hardExampleSol2', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('hardExampleQues3', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('hardExampleSol3', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('hardExampleQues4', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('hardExampleSol4', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('hardExampleQues5', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('hardExampleSol5', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('difficulty', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('importance', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('duration', models.IntegerField()),
                ('summary', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('mnemonics', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('videoUrl', models.URLField()),
                ('targetExam', models.CharField(choices=[('IIT', 'IIT'), ('NEET', 'NEET')], max_length=100)),
                ('wowTheory', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('wowQues', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('wowReason', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('concept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Theory', to='theoryTag.Concept')),
                ('prerequisites', models.ManyToManyField(blank=True, related_name='prerequisiteOf', to='theoryTag.SubConcept')),
                ('subConcept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Theory', to='theoryTag.SubConcept')),
                ('twinConcepts', models.ManyToManyField(blank=True, related_name='twinConceptOf', to='theoryTag.SubConcept')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='theoryTag.Subject'),
        ),
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together={('name', 'subject')},
        ),
    ]
