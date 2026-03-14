import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=150)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='ecos')),
                ('fecha', models.DateField()),
            ],
        ),
    ]
