# Generated by Django 2.1.5 on 2019-01-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(related_name='books', to='book.Tags'),
        ),
    ]